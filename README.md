# Face Detection and Cropping Script

This script automates the detection and cropping of faces from images in a specified directory. It uses OpenCV for face and eye detection and PIL for resizing the cropped image to passport size.

## Features

- Automatically detects faces with two eyes in an image.
- Crops the face along with shoulders and resizes it to passport size (826x1026 pixels).
- Processes all supported image formats (`.png`, `.jpg`, `.jpeg`, `.bmp`, `.tiff`) in a directory.
- Saves the cropped images to a specified output directory.

## Usage

### Prerequisites

- Python 3.x installed on your system.
- Required libraries (`opencv-python` and `Pillow`) installed. You can install these using pip:

  ```bash
  pip install opencv-python Pillow
  ```

### Setup

1. Clone the repository or download the script (`face_cropper.py`) to your local machine.

2. Ensure that the necessary Haar Cascade XML files for face and eye detection (`haarcascade_frontalface_default.xml` and `haarcascade_eye.xml`) are available in the `cv2` data directory.

3. Open a terminal or command prompt.

4. Navigate to the directory containing `face_cropper.py`.

### Execution

Replace `path/to/input/folder` and `path/to/output/folder` in the script with the actual paths to your input and output directories.

```bash
python face_cropper.py
```

### Output

After execution, the script will save the cropped passport-size photos in the specified output directory.

## Notes

- Ensure you have appropriate permissions to read from the input folder and write to the output folder.
- The script will only crop faces where two eyes are detected.
- Back up your images before running the script, especially if the images are critical.

Feel free to customize the script according to your needs and preferences. If you encounter any issues or have suggestions for improvement, please feel free to create an issue or contribute to the development.
