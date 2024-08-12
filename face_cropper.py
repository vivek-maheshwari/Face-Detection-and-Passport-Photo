import cv2
from PIL import Image
import os

def detect_and_crop_face(image_path, output_path, face_cascade_path="haarcascade_frontalface_default.xml", eye_cascade_path="haarcascade_eye.xml"):
    if not os.path.isfile(image_path):
        print(f"Error: The file '{image_path}' does not exist.")
        return
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Failed to load the image '{image_path}'.")
        return
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + face_cascade_path)
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + eye_cascade_path)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    if len(faces) == 0:
        print(f"No face detected in the image '{image_path}'.")
        return
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes) >= 2:
            break
    else:
        print(f"No face with two eyes detected in the image '{image_path}'.")
        return
    buffer_top = int(0.5 * h)
    buffer_bottom = int(1.0 * h)
    buffer_left = int(0.5 * w)
    buffer_right = int(0.5 * w)
    x_start = max(0, x - buffer_left)
    y_start = max(0, y - buffer_top)
    x_end = min(image.shape[1], x + w + buffer_right)
    y_end = min(image.shape[0], y + h + buffer_bottom)
    face_and_shoulders = image[y_start:y_end, x_start:x_end]
    face_pil = Image.fromarray(cv2.cvtColor(face_and_shoulders, cv2.COLOR_BGR2RGB))
    passport_size = (826, 1026)
    face_pil = face_pil.resize(passport_size, Image.Resampling.LANCZOS)
    background = Image.new('RGB', passport_size, (255, 255, 255))
    background.paste(face_pil, (0, 0))
    background.save(output_path)
    print(f"Cropped passport-size photo saved as {output_path}")

def process_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{filename}")
            detect_and_crop_face(input_path, output_path)

input_folder = r'path/to/input/folder'
output_folder = r'path/to/output/folder'
process_folder(input_folder, output_folder)
