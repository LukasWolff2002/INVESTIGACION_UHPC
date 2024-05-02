import matplotlib.pyplot as plt
import os
from pypylon import genicam, pylon
import sys
import datetime
from PIL import Image
import cv2
import os

# Creamos la clase para listas concatenadas
class node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

# Creamos la clase linked_list
class linked_list: 
    def __init__(self):
        self.head = None
    
    # Método para agregar elementos en el frente de la linked list
    def add_at_front(self, data):
        self.head = node(data=data, next=self.head)  

    # Método para verificar si la estructura de datos esta vacia
    def is_empty(self):
        return self.head == None

    # Método para agregar elementos al final de la linked list
    def add_at_end(self, data):
        if not self.head:
            self.head = node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node(data=data)
    
    # Método para eleminar nodos
    def delete_node(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    # Método para obtener el ultimo nodo
    def get_last_node(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        return temp.data

    # Método para imprimir la lista de nodos
    def print_list( self ):
        node = self.head
        while node != None:
            print(node.data, end =" => ")
            node = node.next

    # Método para recorrer la lista de nodos
    def traverse(self):
        current_node = self.head
        
        while current_node:

            img = current_node.data.GetArray()
            img = cv2.equalizeHist(img)
            camara = current_node.data.GetCameraContext()
            tiempo = current_node.data.GetTimeStamp()

            # Carpeta donde se almacenarán las imágenes
            folder_path = f'FOTOS/{RPM}/{camara}'
            print(folder_path)

            # Crear la carpeta si no existe
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Nombre del archivo de la imagen
            file_name = f'{tiempo}.png'

            # Ruta completa del archivo de la imagen
            file_path = os.path.join(folder_path, file_name)

            # Crear una imagen PIL a partir de la matriz de la imagen
            image = Image.fromarray(img)

            # Guardar la imagen como PNG
            image.save(file_path)

            print(f"Imagen guardada: {file_path}")
            current_node = current_node.next

#---------------------
# DETERMINO EL NOMBRE DE CARPETA
RPM = 8362

# DETERMINO CANTIDAD DE IMAGENES A SACAR
countOfImagesToGrab = 10000
#---------------------

buffer = 5000
RPM = str(RPM)

# Se crea la lista concatenada
s = linked_list() 

# Limits the amount of cameras used for grabbing.
maxCamerasToUse = 2

# The exit code of the sample application.
exitCode = 0

try:
    # Get the transport layer factory.
    tlFactory = pylon.TlFactory.GetInstance()

    # Get all attached devices and exit application if no device is found.
    devices = tlFactory.EnumerateDevices()
    if len(devices) == 0:
        raise pylon.RuntimeException("No camera present.")

    # Create an array of instant cameras for the found devices and avoid exceeding a maximum number of devices.
    cameras = pylon.InstantCameraArray(min(len(devices), maxCamerasToUse))

    # Create and attach all Pylon Devices.
    for i, cam in enumerate(cameras):
       
        cam.Attach(tlFactory.CreateDevice(devices[i]))

        # Open the camera to set parameters
        cam.Open()

        # Buffer Size Adjustment
        cam.MaxNumBuffer = buffer  # Adjust buffer size as needed
        
        # Configure camera settings
        cam.AcquisitionFrameRateEnable.SetValue(True)
        cam.AcquisitionFrameRate.SetValue(200)
        cam.ExposureTime.SetValue(100)  # Set exposure time to 100000 microseconds

        # Close the camera after setting parameters
        cam.Close()

    # Starts grabbing for all cameras starting with index 0.

    print(' ')
    print('COMIENZA EL TRIGGER')
    print(' ')

    #----------------------
    # Disparo las camaras
    cameras.StartGrabbing()
    #----------------------
    

    for i in range(countOfImagesToGrab):
        if not cameras.IsGrabbing():
            break

        #recibo la foto y la guardo como array y en la lista concatenada
        grabResult = cameras.RetrieveResult(40000, pylon.TimeoutHandling_ThrowException)
        s.add_at_front(grabResult)
        
finally:
    for cam in cameras:
        cam.StopGrabbing()
        cam.Close()

s.traverse()
print("Fotos Guardadas")

# Para probar codigo y borrar fotos automaticamente en mac activar este comando
#os.system('rm -r FOTOS')