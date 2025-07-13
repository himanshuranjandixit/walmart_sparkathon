# 🥦 Walmart Sparkathon 2025 – AI-Powered Rotten vs Fresh Produce Detection

Welcome to our submission for the **Walmart Sparkathon 2025**, under the theme **"Building a Sustainable Future"**.

This project presents an AI-powered computer vision system designed to **automatically detect whether fruits and vegetables are fresh or rotten** across **16 detailed produce categories**. It supports real-time image/video input to enable proactive decisions around quality control, shelf management, and waste reduction—directly aligning with Walmart’s goal of building a more sustainable retail ecosystem.

---

## 🌍 Why It Matters: Supporting Walmart's Sustainability Vision

Walmart is leading the retail industry in applying AI to reduce food waste, ensure produce freshness, and improve shelf life. As noted in [Walmart Global Tech’s blog](https://tech.walmart.com/content/walmart-global-tech/en_us/blog/post/how-walmart-plans-to-use-ai-to-reduce-waste.html):

> "AI is being used to automatically detect produce nearing expiration and make recommendations—whether it’s a markdown, donation, or return."

Our solution contributes directly to this mission by detecting **rotting produce in real time**, allowing for timely actions that prevent waste and improve the customer experience.

---

## 🎯 Project Goals

- 🧠 Automatically classify produce as **fresh** or **rotten**
- 🧺 Support **16 fine-grained product classes**
- 📷 Enable **real-time detection** from camera feeds or uploaded images
- ♻️ Help Walmart **reduce food waste** and optimize freshness
- 📊 Assist in automating decisions like **markdown**, **removal**, or **donation**

---

## 📦 Classification Categories

We use **16 sub-classes** grouped under 4 broad freshness categories:

| Category            | Sub-Classes (Example)                                      |
|---------------------|----------------------------------------------------------  |
| 🍎 Fresh Fruits      | `fresh_apple`, `fresh_banana`, `fresh_orange` , etc      |
| 🍌 Rotten Fruits     | `rotten_apple`, `rotten_banana`, `rotten_orange`,etc     |
| 🥕 Fresh Vegetables  | `fresh_tomato`, `FreshCarrot`, `fresh_potato`, etc       |
| 🥬 Rotten Vegetables | `rotten_tomato`, `RottenCarrot`, `rotten_potato`, etc    |

---

## 🧠 Workflow Overview

### 🖼️ 1. Data Labeling

- Labeled **6,000+ images** using **Roboflow**
- Each image includes bounding boxes with one of the **16 class labels**
- Exported in **YOLOv8 format** for object detection training

### 🧼 2. Preprocessing

| Step                | Description                            |
|---------------------|----------------------------------------|
| 📏 Resize           | Resized to `640×640` (stretched)       |
| 🎚️ Contrast Stretching | Enhances image detail visibility     |

### 🔁 3. Data Augmentation

| Augmentation                  | Purpose                                               |
|-------------------------------|--------------------------------------------------------|
| 🔄 Horizontal/Vertical Flip   | Orientation robustness                                |
| ↪️ Rotation (-15° to +15°)    | Simulates camera angles                               |
| ✨ Gaussian Noise (0.15%)     | Simulates sensor/camera artifacts                     |
| 🔭 Perspective Shift (±10°)   | Adds pitch and yaw variability                        |
| 🔍 Random Crop (0–20%)        | Simulates zoom/translation of produce                 |
| 🌫️ Gaussian Blur             | Resilience to camera focus issues                     |

---

## 🧪 Model Training

- 📦 Model: YOLOv8 (Ultralytics)
- 🧠 Framework: PyTorch
- 🧾 Dataset Format: YOLOv8 (Roboflow export)
- 📊 Train/Val/Test Split: 80% / 10% / 10%
- 🖼️ Input Size: `640 × 640`
- 📉 Loss Functions: Combined bounding box + class confidence loss

---

## 🚀 Running the Project

### 1. Clone the Repository

```bash
git clone https://github.com/himanshuranjandixit/walmart_sparkathon.git
cd walmart_sparkathon
