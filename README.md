# ✍️ Handwritten Character Recognition using CNN

## 📌 Project Overview

This project is a Deep Learning-based Handwritten Character Recognition system that classifies handwritten digits using a Convolutional Neural Network (CNN). It performs image preprocessing, model training, evaluation, and deployment through a Streamlit web application.

The model is trained on the MNIST dataset and is designed to recognize handwritten digits with high accuracy. The project can be extended to recognize handwritten alphabets using the EMNIST dataset and complete words using CRNN.

---

## 🎯 Objective

Develop an intelligent system capable of recognizing handwritten characters from images using image processing and deep learning techniques.

---

## 🚀 Features

- Handwritten digit recognition
- Image preprocessing
- Convolutional Neural Network (CNN)
- Data augmentation
- Model evaluation
- Confusion Matrix
- Classification Report
- Accuracy and Loss visualization
- Save and load trained model
- Streamlit web application for prediction
- Easy to extend for alphabet recognition (EMNIST)

---

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- NumPy
- Pandas
- Matplotlib
- OpenCV
- Scikit-learn
- Streamlit

---

## 📂 Dataset

### MNIST Dataset

- 70,000 grayscale handwritten digit images
- Image Size: 28 × 28 pixels
- Training Images: 60,000
- Testing Images: 10,000
- Classes: 10 (Digits 0–9)

Future Enhancement:
- EMNIST Dataset (Characters & Alphabets)

---

## 📁 Project Structure

```
Handwritten_Character_Recognition/
│
├── app.py
├── train.ipynb
├── handwritten_character_recognition.keras
├── requirements.txt
├── README.md
├── sample.png
│
├── images/
│   ├── accuracy.png
│   ├── loss.png
│   ├── confusion_matrix.png
│   └── app_screenshot.png
│
└── .gitignore
```

---

## ⚙️ Workflow

1. Import Libraries
2. Load Dataset
3. Data Preprocessing
4. Build CNN Model
5. Compile Model
6. Train Model
7. Evaluate Model
8. Generate Predictions
9. Save Model
10. Deploy using Streamlit

---

## 🧠 CNN Architecture

- Conv2D (32 Filters)
- Batch Normalization
- MaxPooling2D
- Conv2D (64 Filters)
- Batch Normalization
- MaxPooling2D
- Flatten Layer
- Dense Layer (128 Neurons)
- Dropout
- Output Layer (Softmax)

---

## 📊 Model Evaluation

Evaluation Metrics:

- Accuracy
- Loss
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Classification Report

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Handwritten-Character-Recognition.git
```

Move into the project folder

```bash
cd Handwritten-Character-Recognition
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Train the model

```bash
python train.py
```

Run Streamlit

```bash
streamlit run app.py
```

---

## 📈 Results

- High recognition accuracy on handwritten digit images
- Real-time prediction using Streamlit
- Robust CNN architecture with image preprocessing
- Easy deployment and user-friendly interface

---

## 🔮 Future Improvements

- Support handwritten alphabets using EMNIST
- Handwritten word recognition
- Sentence recognition using CRNN
- Real-time webcam prediction
- Mobile application deployment
- Model optimization for faster inference

---

## 💡 Learning Outcomes

Through this project, I learned:

- Image preprocessing
- Deep Learning fundamentals
- CNN architecture design
- Model training and evaluation
- Performance visualization
- Streamlit deployment
- Image classification workflow

---

