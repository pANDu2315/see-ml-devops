from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
import cv2

app = Flask(__name__)

# Load trained model
model = tf.keras.models.load_model("ml/model/mnist_cnn_model.h5")

def preprocess_image(file):
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (28, 28))
    img = img / 255.0
    img = img.reshape(1, 28, 28, 1)
    return img

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        if "file" not in request.files:
            return render_template("index.html", prediction="No file uploaded")

        file = request.files["file"]

        if file.filename == "":
            return render_template("index.html", prediction="No file selected")

        img = preprocess_image(file)
        pred = model.predict(img)
        prediction = np.argmax(pred)

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
