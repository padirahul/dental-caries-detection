from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
from PIL import Image
import os

app = Flask(__name__)
model = tf.keras.models.load_model(r"C:\caries_1\teeth_model.h5")

# Ensure the upload folder exists
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Preprocessing function
def preprocess_image(image_path):
    image = Image.open(image_path).convert('RGB')  # Convert to RGB (3 channels)
    image = image.resize((128, 128))  # Resize to match model input
    image = np.array(image) / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    image = preprocess_image(file_path)
    prediction = model.predict(image)[0][0]

    result = "Healthy Teeth" if prediction > 0.5 else "Caries Detected"
    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
