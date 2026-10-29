# 👁️ Seeing the World in Code — My OpenCV Journey

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg?logo=python&logoColor=white)](https://python.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8.svg?logo=opencv&logoColor=white)](https://opencv.org)
[![NumPy](https://img.shields.io/badge/NumPy-Array%20Processing-013243.svg?logo=numpy&logoColor=white)](https://numpy.org)

Welcome to my hands-on computer vision playground! Here, I document my complete journey of learning **OpenCV** from scratch, building real projects, tweaking parameters, and turning raw pixels into intelligent code.

---

## 🎨 Major Project Milestones

- 🎭 **Cartoonifier:** Transform real images into stylized, cartoonish art.
- 🌫️ **Face Blur:** Real-time privacy blur on detected faces.
- ✋ **Gesture Control:** Controlling applications using computer vision.
- 🎯 **Object & Color Tracking:** Tracking specific targets based on HSV color spaces.

---

## 🗺️ Learning Roadmap & Course Progress

```text
       [ 🚀 Phase 0: Getting Ready ]
                    │
       [ 🖼️ Phase 1: Image Basics ]
                    │
       [ ✂️ Phase 2: Transformations ]
                    │
       [ 🎨 Phase 3: Basic Drawing ]
                    │
       [ 📹 Phase 4: Video & Webcam ]
                    │
       [ 🌀 Phase 5: Image Filtering ]
                    │
       [ 📐 Phase 6: Edge Detection ]
                    │
       [ 🔍 Phase 7: Contours & Shapes ]
                    │
       [ 👤 Phase 8: Face & Object Detection ]
```

---

## 📑 Syllabus & Key Concepts Covered

### Phase 0: Getting Ready for OpenCV
- Introduction to OpenCV & Computer Vision Ecosystem
- Real-world applications and use cases
- Key features & setting up Python, tools, and dependencies

### Phase 1: Getting Started with OpenCV
- Installing OpenCV (`cv2`)
- Reading, displaying, and saving images
- Understanding image dimensions, channels (BGR vs. RGB)
- Grayscale conversion and pixel manipulations

### Phase 2: Image Transformations & Manipulation
- Resizing & scaling images proportionally
- Cropping regions of interest (ROI) using NumPy slicing
- Rotating and flipping images
- Drawing shapes (lines, circles) & adding text on images

### Phase 3: Basic Image Drawing Techniques
- Drawing precise lines, rectangles, and circles
- Customizing fonts, colors, and line thickness
- Creating custom graphic overlays on images

### Phase 4: Working with Video & Webcam
- Capturing video streams using `cv2.VideoCapture`
- Frame-by-frame real-time image processing
- Applying live filters to video feeds
- Exporting and saving video streams with `cv2.VideoWriter`

### Phase 5: Image Filtering & Blurring
- Gaussian blur and Median blur algorithms
- Custom sharpening kernels & noise reduction filters
- Smoothing noisy images to enhance visual clarity

### Phase 6: Edge Detection & Thresholding
- Canny Edge Detection algorithm
- Binary and Adaptive Thresholding methods
- Bitwise logical operations (`AND`, `OR`, `NOT`, `XOR`)
- Extracting outlines from complex background textures

### Phase 7: Contours & Shape Detection
- Finding, analyzing, and drawing contours
- Polygon approximation using `approxPolyDP`
- Detecting basic shapes (triangles, squares, circles)
- Core concepts of geometry-based object recognition

### Phase 8: Face & Object Detection
- Haar Cascade Classifiers overview
- Real-time face, eye, and smile detection
- Working with pre-trained XML models
- Drawing dynamic bounding boxes around detected regions

---

## ⚙️ Tech Stack

| Technology | Purpose |
| :--- | :--- |
| **Python** | Core Language |
| **OpenCV (`cv2`)** | Computer Vision & Image Processing |
| **NumPy** | High-performance Array & Matrix Operations |
| **Matplotlib** | Data & Image Visualization |

---

## ⚡ How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/your-username/your-repo-name.git

# 2. Navigate into the directory
cd your-repo-name

# 3. Install required packages
pip install opencv-python numpy matplotlib

# 4. Run a script
python phase_1/read_image.py
```

---

*⭐ Feel free to star this repository if you find it helpful!*