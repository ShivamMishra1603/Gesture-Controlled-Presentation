# Gesture-Based Presentation System

This project introduces a gesture-based presentation system that enhances user engagement and interactivity during presentations. By leveraging computer vision and hand tracking, it enables presenters to control slides, annotate content, and interact with their presentations through intuitive hand gestures, eliminating the need for physical devices like clickers or keyboards.

## Key Features
- **Gesture-Based Slide Control:** Navigate through slides using simple hand gestures.
- **Dynamic Annotations:** Draw and annotate slides in real time.
- **Pointer Functionality:** Highlight specific areas on slides using gestures.
- **Cost-Effective Solution:** Works with a standard webcam and free, open-source libraries.
- **Real-Time Responsiveness:** Minimal latency for a seamless user experience.

## Technologies Used
- **OpenCV:** For video capture, image processing, and slide rendering.
- **MediaPipe Hands:** For hand detection and tracking, enabling gesture recognition.
- **CVZone:** Simplifies hand tracking and gesture interpretation.
- **NumPy:** Handles mathematical operations for gesture scaling and responsiveness.

## System Workflow

![alt text](assets\images\image.png)

1. **Video Capture:** Frames are captured from the webcam using OpenCV.
2. **Gesture Recognition:** MediaPipe and CVZone process gestures in real time.
3. **Slide Interaction:** Detected gestures trigger slide navigation, annotations, or pointer actions.
4. **Dynamic Feedback:** Slides update dynamically with gestures and annotations displayed in real time.

## Modules Overview
- **`config.py`:** Centralized configuration management for system parameters.
- **`hand_tracking.py`:** Detects hand movements and interprets gestures for slide control and annotations.
- **`slide_controller.py`:** Handles loading, navigation, and display of presentation slides.
- **`annotations.py`:** Allows users to draw and interact with slides dynamically.
- **`main.py`:** Integrates all modules, managing video input, gesture detection, and slide updates.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/ShivamMishra1603/Gesture-Controlled-Presentation.git
   cd Gesture-Controlled-Presentation

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the application
   ```bash
   python main.py

## Presentation

- Hand detection and landmark tracking
![alt text](assets\images\image-1.png)
- Pointer using index finger
![alt text](assets\images\image-2.png)
- Move to next slide
![alt text](assets\images\image-3.png)
- Move to previous slide
![alt text](assets\images\image-4.png)
- Draw on slide
![alt text](assets\images\image-5.png)
- Delete drawing from slide
![alt text](assets\images\image-6.png)

## Testing and Validation

The system was tested under controlled conditions with the following results:

- Gesture Recognition Accuracy: 95% in optimal lighting, 74% in poor lighting.
- Latency: Minimal delay (~50ms) ensures real-time responsiveness.
- User-Friendly Design: Intuitive gestures reduce the learning curve for new users.

## Limitations

- Performance is sensitive to lighting conditions; low light may reduce accuracy.
- Camera positioning and resolution can impact gesture detection.

## Future Enhancements

- Customizable Gestures: Allow users to define and train custom gestures.
- Multi-Presenter Support: Enable simultaneous interaction for collaborative presentations.
- Advanced Annotation Tools: Add features like shape drawing, line thickness adjustment, and color selection.
- Zoom and Pan Gestures: Implement gestures for slide zooming and panning.


## Conclusion
This project demonstrates the potential of gesture-based systems to redefine how presentations are delivered. It enhances both the presenter’s experience and audience engagement, providing a futuristic, touch-free alternative to traditional presentation tools.