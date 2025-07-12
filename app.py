import streamlit as st
from PIL import Image
import torch
from ultralytics import YOLO
import tempfile
import os

# Load YOLOv8 model (replace with your .pt path if needed)
model = YOLO("Walmart_version1.pt")  # e.g., 'last.pt' or 'Walmart_version1.pt'

st.title("🛒 Vegetable Detection App")
st.markdown("Upload an image and click **'Run Detection'** to identify vegetables using YOLOv8.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Save uploaded image temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        temp_file.write(uploaded_file.getvalue())
        temp_path = temp_file.name

    # Show uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Run detection button
    if st.button("🚀 Run Detection"):
        with st.spinner("Running YOLOv8 inference..."):
            results = model(temp_path)

            # Save result with bounding boxes
            result_img_path = results[0].save(filename=temp_path)

            # Show annotated image
            result_image = Image.open(result_img_path)
            st.image(result_image, caption='Detection Result', use_column_width=True)

            # Show detected classes with confidence
            boxes = results[0].boxes
            if boxes is not None:
                st.subheader("📦 Detected Objects:")
                for box in boxes:
                    cls = int(box.cls[0])
                    conf = float(box.conf[0])
                    class_name = model.names[cls]
                    st.write(f"🔹 {class_name} — {conf:.2%} confidence")
