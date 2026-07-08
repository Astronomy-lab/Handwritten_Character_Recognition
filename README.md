# ✍️ Handwritten Character Recognition using CNN

## 📌 Project Overview

This project is a Deep Learning-based Handwritten Character Recognition system that recognizes handwritten digits using a Convolutional Neural Network (CNN). The model is trained on the MNIST dataset and performs image preprocessing, feature extraction, classification, and performance evaluation with high accuracy.

This project demonstrates the complete workflow of an image classification task, including data preprocessing, CNN model development, training, evaluation, and prediction.

---

## 🎯 Objective

Develop a deep learning model capable of accurately recognizing handwritten digits from grayscale images using Convolutional Neural Networks (CNN).

---

## 🚀 Features

- Handwritten digit recognition
- Image preprocessing and normalization
- Convolutional Neural Network (CNN)
- Data augmentation
- Model training and validation
- Performance evaluation
- Accuracy and loss visualization
- Confusion Matrix
- Classification Report
- Save and load trained model
- Extendable to handwritten alphabet recognition using EMNIST

---

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- NumPy
- Pandas
- Matplotlib
- OpenCV
- Scikit-learn

---

## 📂 Dataset

This project uses the **MNIST Handwritten Digits Dataset**, which is automatically downloaded using TensorFlow.

**Dataset Details**

- Total Images: 70,000
- Training Images: 60,000
- Testing Images: 10,000
- Image Size: 28 × 28 pixels
- Image Type: Grayscale
- Classes: 10 (Digits 0–9)

Dataset loading:

```python
from tensorflow.keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()
```

---

## 📁 Project Structure

```
Handwritten_Character_Recognition/

│── train.ipynb
│── handwritten_character_recognition.keras
│── handwritten_character_cnn.keras
│── requirements.txt
│── README.md
│── sample.png
│
├── images/
│   ├── accuracy.png
│   ├── loss.png
│   ├── confusion_matrix.png
│   └── prediction.png
│
└── .gitignore
```

---

## ⚙️ Project Workflow

1. Import Required Libraries
2. Load the MNIST Dataset
3. Perform Data Preprocessing
4. Normalize Pixel Values
5. Reshape Images for CNN
6. Apply Data Augmentation
7. Build CNN Architecture
8. Compile the Model
9. Train the Model
10. Evaluate Performance
11. Generate Predictions
12. Save the Trained Model

---

## 🧠 CNN Architecture

- Conv2D (32 Filters, ReLU)
- Batch Normalization
- MaxPooling2D
- Conv2D (64 Filters, ReLU)
- Batch Normalization
- MaxPooling2D
- Flatten Layer
- Dense Layer (128 Neurons)
- Dropout Layer
- Output Layer (Softmax)

---

## 📊 Model Evaluation

The trained model is evaluated using the following metrics:

- Accuracy
- Loss
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Classification Report

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Handwritten-Character-Recognition.git
```

Navigate to the project directory:

```bash
cd Handwritten-Character-Recognition
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Open and run all cells in:

```text
train.ipynb
```

The notebook will:

- Download the MNIST dataset
- Preprocess the images
- Train the CNN model
- Evaluate model performance
- Save the trained model as:

```text
handwritten_character_recognition.keras
```

---

## 📈 Results

- Achieves high classification accuracy on handwritten digits.
- Learns meaningful image features using CNN.
- Demonstrates strong performance on unseen test images.
- Generates evaluation metrics and visual performance graphs.

---

## 🔮 Future Improvements

- Recognize handwritten alphabets using the EMNIST dataset.
- Support handwritten word recognition.
- Implement CRNN for sentence recognition.
- Improve performance using transfer learning.
- Extend to multilingual handwritten character recognition.

---

## 📚 Learning Outcomes

This project demonstrates:

- Image preprocessing techniques
- Convolutional Neural Networks (CNN)
- Deep learning model development
- Image classification
- Model evaluation
- Performance visualization
- Saving and loading trained models

---

## Author
** Aditya Vikram Singh **
