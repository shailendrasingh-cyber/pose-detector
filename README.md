# Pose Detector Streamlit App

## Overview

This Streamlit application allows users to detect poses in images and live video feeds using MediaPipe Pose. Users can choose between uploading an image or accessing a live video feed from their camera. The app processes the input to detect human poses and displays the results.

## Features

- **Image Upload Mode**: Upload an image file (JPG, JPEG, or PNG) to detect poses.
- **Live Video Mode**: Access your camera to get a live video feed with pose detection.
- **Interactive Interface**: Select between image upload and live video modes from the dropdown menu.
- **User Guide**: Instructions are provided in the sidebar on how to use each mode.

## Requirements

- Python 3.7 or later
- Streamlit
- OpenCV
- Mediapipe
- Pillow
- NumPy

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/shailendrasingh-cyber/pose-detector
    ```

2. **Navigate to the project directory:**

    ```bash
    cd pose-detector
    ```

3. **Install the required packages:**

    ```bash
    pip install streamlit opencv-python mediapipe pillow numpy
    ```

## Usage

1. **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

2. **Access the app:**
   - Open the provided URL in your browser to start using the app.

3. **Choose a mode:**
   - **Upload Image**: Select this mode to upload an image file and see pose detection results.
   - **Live Video**: Select this mode to start the live video feed. Click **'Stop'** to end the video feed.

## How to Use

### Live Video Mode
1. Select **'Live Video'** from the dropdown menu.
2. Allow the app to access your camera.
3. Click **'Stop'** to end the video feed.

### Upload Image Mode
1. Select **'Upload Image'** from the dropdown menu.
2. Upload an image file (JPG, JPEG, or PNG).
3. The app will process and display the image with detected poses.

### Note
- Make sure your camera is properly connected if using the live video mode.
- The app will display error messages if there are issues with accessing the camera or processing the video frames.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Made by Shailendra Singh

Feel free to reach out if you have any questions or feedback!
portfolio:- https://ssinghportfolio.netlify.app/

