import os
gstreamer_path = os.environ.get("GSTREAMER_PATH", r"C:\Program Files\gstreamer\1.0\msvc_x86_64\bin")
os.add_dll_directory(gstreamer_path)

import cv2

print( cv2.__version__ )