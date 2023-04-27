from werkzeug.utils import secure_filename
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

from flask import Flask, request, make_response


# Load the model
model = load_model('coffeeDripper.h5')

# Note Classes
note_classes = ['Origami Dripper', 'Kalita Wave Dripper', 'Clever Dripper', 'Flower Dripper', 'V60 Dripper']

def predict(pillow_image_path):
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(pillow_image_path)
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    label0 = np.argmax(prediction)
    return note_classes[prediction.argmax()]


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        f = request.files['file']
        f.save(secure_filename(f.filename))
        print('file uploaded successfully')
        pillow_image_path = (os.path.realpath(f.filename))
        prediction = predict(pillow_image_path)
        print(str(prediction))
        os.remove(pillow_image_path)
        response = make_response(prediction, 200)
        response.mimetype = "text/plain"
        return response
    else:
        return "hello world"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)