import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import Face_Extraction

def predicted_label():
    face = np.load("extracted_face1.npy")
    face = tf.image.resize(face, [224, 224])       # Resize to match training input size
    face = face / 255.0                           # Normalize
    face = np.expand_dims(face, axis=0)          # Add batch dimension: (1, 32, 32, 3)

    # Load model
    model = load_model("C:/Users/rkkab/Downloads/Face_detector/model_face.keras")


    # Define class names (or load from dataset)
    # Replace with actual labels
    import json

    with open("class_names.json", "r") as f:
        class_names = json.load(f)

    # Predict
    prediction = model.predict(face)
    predicted_class = np.argmax(prediction)

    predicted_name = class_names[predicted_class]
    print("Predicted label:", predicted_name)

    return predicted_name 
if __name__ == "__main__":
    detected_image=Face_Extraction
print(predicted_label())