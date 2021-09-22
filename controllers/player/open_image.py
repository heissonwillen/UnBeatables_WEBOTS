from PIL import Image
import numpy as np
import cv2

for camera in sensor_measurements.cameras:
    img_array = np.frombuffer(camera.image, np.uint8).reshape(
        camera.height, camera.width, 3)
    cv2.imshow('image', img_array)
    cv2.waitKey(0)

cv2.destroyAllWindows()
