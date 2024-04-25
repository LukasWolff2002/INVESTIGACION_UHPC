import matplotlib.pyplot as plt
import os
from pypylon import genicam, pylon
import sys
import datetime
from PIL import Image
import cv2

#---------------------
#DETERMINO EL NOMRE DE CARPETA
RPM = 12055
#---------------------

RPM = str(RPM)

# Number of images to be grabbed.
countOfImagesToGrab =  20

# Limits the amount of cameras used for grabbing.
maxCamerasToUse = 2

# The exit code of the sample application.
exitCode = 0

imagenes = []

try:
    # Get the transport layer factory.
    tlFactory = pylon.TlFactory.GetInstance()

    # Get all attached devices and exit application if no device is found.
    devices = tlFactory.EnumerateDevices()
    
    if len(devices) == 0:
        raise pylon.RuntimeException("No camera present.")
    
    for elementos in devices:
        print(elementos)

    # Create an array of instant cameras for the found devices and avoid exceeding a maximum number of devices.
    cameras = pylon.InstantCameraArray(min(len(devices), maxCamerasToUse))

    # Create and attach all Pylon Devices.
    for i, cam in enumerate(cameras):
        cam.Attach(tlFactory.CreateDevice(devices[i]))

        cam.Open()
        
        cam.AcquisitionFrameRateEnable.SetValue(True)
        cam.AcquisitionFrameRate.SetValue(200)
        cam.ExposureTime.SetValue(100)  # 100000 microsecond
        cam.Close()

    # Starts grabbing for all cameras starting with index 0.
    cameras.StartGrabbing()

    print(' ')
    print('COMIENZA EL TRIGGER')
    print(' ')
    # Grab countOfImagesToGrab from the cameras.
    for i in range(countOfImagesToGrab):
        if not cameras.IsGrabbing():
            break
        
        grabResult = cameras.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
        imagenes.append(grabResult)
        

except genicam.GenericException as e:
    # Error handling
    print("An exception occurred.", e)
    exitCode = 1


for i, elementos in enumerate(imagenes):
    img = elementos.GetArray()
    img = cv2.equalizeHist(img)
    camara = elementos.GetCameraContext()
    tiempo = elementos.GetTimeStamp()

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
