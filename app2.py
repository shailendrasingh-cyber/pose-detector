import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
from PIL import Image


mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

def process_image(image):
    
    image_rgb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    
    with mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        
        results = pose.process(cv2.cvtColor(image_rgb, cv2.COLOR_BGR2RGB))

        
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(image_rgb, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        
    return Image.fromarray(cv2.cvtColor(image_rgb, cv2.COLOR_BGR2RGB))

def main():
    st.title('Pose Detector')

    
    mode = st.selectbox(
        "Choose mode:",
        ["Upload Image", "Live Video"]
    )

    
    st.sidebar.header('How to Use:')
    st.sidebar.markdown(
        """
        ### Live Video Mode
        1. Select **'Live Video'** from the dropdown.
        2. Allow the app to access your camera.
        3. Click **'Stop'** to end the video feed.

        ### Upload Image Mode
        1. Select **'Upload Image'** from the dropdown.
        2. Upload an image file (JPG, JPEG, or PNG).
        3. The app will process and display the image with detected poses.
        4. Made by Shailendra Singh 
        """
    )

    if mode == "Upload Image":
        uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
        if uploaded_image is not None:
            image = Image.open(uploaded_image)
            processed_image = process_image(image)
            st.image(processed_image, caption='Processed Image with Pose Detection', use_column_width=True)
    elif mode == "Live Video":
        
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            st.error("Error: Unable to access camera. Please check if the camera is connected and try again.")
            return

        frame_window = st.image([])

        
        if 'stop_button_pressed' not in st.session_state:
            st.session_state.stop_button_pressed = False

        if st.button('Stop'):
            st.session_state.stop_button_pressed = True

        
        with mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while not st.session_state.stop_button_pressed:
                ret, frame = cap.read()
                if not ret:
                    st.error("Error: Unable to capture video frame. Please check the camera connection.")
                    break

                
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                
                results = pose.process(frame_rgb)

                
                if results.pose_landmarks:
                    mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

                
                frame_window.image(frame, channels='BGR')

                
                if st.session_state.stop_button_pressed:
                    break

        
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
