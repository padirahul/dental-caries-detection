# Dental Caries Detection using CNN and Flask

## Project Overview
This project is a **dental caries detection** system using **Convolutional Neural Networks (CNNs)**. The model is trained to classify **dental X-ray images** as having cavities or not. The trained model is deployed as a **Flask web application**, allowing users to upload dental X-ray images and receive a diagnosis.

## Features
- **Deep Learning Model**: CNN-based model trained on labeled dental X-ray images.
- **Flask Web App**: Simple UI for users to upload images and get predictions.
- **Automated Preprocessing**: Images are resized and normalized before prediction.
- **Bounding Box Detection (Optional)**: Model can highlight areas of cavities if trained for object detection.

---

## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/dental-caries-detection.git
cd dental-caries-detection
```

### 2. Install Dependencies
Ensure you have Python 3.8+ installed. Then install the required libraries:
```sh
pip install -r requirements.txt
```

### 3. Download the Model
Place the trained model (`dental_caries_cnn.h5`) in the project directory. If you haven't trained a model yet, you need to train it first (see Training section).

---

## Usage
### 1. Run the Flask Application
```sh
python app.py
```
By default, the app will run at `http://127.0.0.1:5000/`

### 2. Upload an X-ray Image
- Open a web browser and go to `http://127.0.0.1:5000/`
- Upload a dental X-ray image.
- Get the prediction: **"Cavity Detected"** or **"No Cavity"**.

---

## Model Training (Optional)
To train your own CNN model for dental caries detection:

### 1. Prepare Dataset
- Organize images into `train`, `valid`, and `test` directories.
- Ensure labels are available for classification.

### 2. Train the Model
Run `train.py` (if available) or modify and execute your training script:
```sh
python train.py
```

### 3. Save the Model
After training, save the model:
```python
model.save("dental_caries_cnn.h5")
```

---

## Troubleshooting
### 1. Model Not Loading
- Ensure the correct model path is set in `app.py`:
  ```python
  MODEL_PATH = "dental_caries_cnn.h5"
  ```
- Check if the `.h5` file exists in the directory.

### 2. Flask App Not Running
- Make sure Flask is installed:
  ```sh
  pip install flask
  ```
- Run the app in the correct directory.

### 3. Model Predicts "No Cavity" for Everything
- Try adjusting the prediction threshold in `app.py`:
  ```python
  threshold = 0.6  # Experiment with different values
  result = "Cavity Detected" if prediction > threshold else "No Cavity"
  ```
- Check preprocessing consistency between training and inference.
- Retrain the model with more balanced data.

---

## Folder Structure
```
/dental-caries-detection
│── static/
│   ├── uploads/         # Stores uploaded images
│   ├── styles.css       # CSS for UI (optional)
│── templates/
│   ├── index.html       # Upload page
│   ├── result.html      # Results page
│── app.py               # Flask application
│── train.py             # Model training script (if applicable)
│── dental_caries_cnn.h5 # Trained CNN model
│── requirements.txt     # Dependencies
│── README.md            # Project documentation
```

---

## Contributing
Feel free to contribute to this project by:
- Improving the model architecture.
- Enhancing the web UI.
- Adding new features like real-time X-ray analysis.

---

## License
This project is licensed under the **MIT License**.

---

## Contact
For any queries, reach out via GitHub Issues or email me at [rahulpadi963@gmail.com].

