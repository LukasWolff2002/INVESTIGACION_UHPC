from pypylon import pylon
import cv2
import os
import time
from datetime import datetime

# Create an instance of the transport layer factory
tlFactory = pylon.TlFactory.GetInstance()

# Get all attached devices and exit application if no device is found
devices = tlFactory.EnumerateDevices()
if len(devices) == 0:
    raise pylon.RUNTIME_EXCEPTION("No camera present.")
print(devices)
# Create and attach all Pylon Devices
cameras = pylon.InstantCameraArray(min(len(devices), 3))

for i, cam in enumerate(cameras):
    cam.Attach(tlFactory.CreateDevice(devices[i]))

# Starts grabbing for all cameras
cameras.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
converter = pylon.ImageFormatConverter()

# converting to opencv bgr format
converter.OutputPixelFormat = pylon.PixelType_BGR8packed
converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

# Directory to save images and timestamps
save_dir = "captured_images3"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

while cameras.IsGrabbing():
    for i, cam in enumerate(cameras):
        grabResult = cam.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

        if grabResult.GrabSucceeded():
            # Access the image data
            image = converter.Convert(grabResult)
            img = image.GetArray()
            windowTitle = 'Camera ' + str(i)
            cv2.namedWindow(windowTitle, cv2.WINDOW_NORMAL)
            cv2.imshow(windowTitle, img)

        k = cv2.waitKey(1)
        if k == 27:  # Escape keys
            cameras.StopGrabbing()
            break
        elif k == ord('s'):  # Press 's' to save images from all cameras
          
            for j, cam in enumerate(cameras):
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                grabResult = cam.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
                if grabResult.GrabSucceeded():
                    image = converter.Convert(grabResult)
                    img = image.GetArray()
                    filename = os.path.join(save_dir, f'Camera_{j}Image{timestamp}.png')
        
                    cv2.imwrite(filename, img)
                grabResult.Release()

        grabResult.Release()

# Releasing the resources
cameras.StopGrabbing()
cv2.destroyAllWindows()