# Face Detection and Cropping Script

This Python script detects faces in images, crops the face region with additional space for shoulders, and resizes the cropped image to a passport-size photo. The processed images are then saved to the specified output directory.

## Features
- **Face Detection:** Utilizes OpenCV's Haar cascades to detect faces and ensure at least two eyes are present in the detected face.
- **Cropping:** Crops the face region with additional buffers on all sides to include shoulders.
- **Resizing:** Resizes the cropped image to passport-size dimensions (826x1026 pixels).
- **Batch Processing:** Processes all images in a specified input folder and saves the results in the output folder.

## Requirements

- Python 3.x
- OpenCV
- Pillow

You can install the required packages using pip:

```bash
pip install opencv-python pillow```


### Usage
Place your images in a folder. Supported formats are .png, .jpg, .jpeg, .bmp, and .tiff.

Update the paths: Modify the input_folder and output_folder variables in the script to point to your image folder and desired output folder, respectively.

```Run the script:
python face_cropper.py```
