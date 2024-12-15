#!/usr/bin/env python
# coding: utf-8

### Inference with TF-lite model

# Necessary import
import os
import numpy as np
import tflite_runtime.interpreter as tflite_int
from urllib import request
from io import BytesIO
from PIL import Image

# Model name
model_name = os.getenv('Model_Name', 'model_2024_hairstyle_v2.tflite')
# Load the model
interpreter = tflite_int.Interpreter(model_path = model_name)
# Load the weights from the model to memory (necessary with tf-lite models)
interpreter.allocate_tensors()

# Specify the input
input_index = interpreter.get_input_details()[0]['index']
# Specify the output
output_index = interpreter.get_output_details()[0]['index']

# Function for downloading the image
def download_image(url):
    # Open url link as a file object
    with request.urlopen(url) as resp:
        # read te link as a string
        buffer = resp.read()
    # Manipulate string in memory
    stream = BytesIO(buffer)
    # Load image
    img = Image.open(stream)
    # return image
    return img

# Function to prepare the image
def prepare_image(img, target_size):
    # If the image is not in RGB mode
    if img.mode != 'RGB':
        # Convert it
        img = img.convert('RGB')
    # Resize the image
    img = img.resize(target_size, Image.NEAREST)
    # return image
    return img

# function for making inference
def predict(url):
    # download image
    img = download_image(url)
    # Prepare the image
    img = prepare_image(img, (200, 200))

    # Convert the image into array
    x = np.array(img, dtype = "float32")
    # Get batch of images
    X = np.array([x])
    # Preprocess input batch of images
    X = X / 255

    # Initialize the input of the interpreter
    interpreter.set_tensor(input_index, X)
    # Invoke computations in the neural network
    interpreter.invoke()
    # Fetch predictions
    preds = interpreter.get_tensor(output_index)
    # Get float prediction as usual python float number
    float_prediction = float(preds[0, 0])

    # return predicted probability
    return float_prediction

# Lambda function handler
def lambda_handler(event, context):
    # image url
    url = event['url']
    # Compute prediction
    pred = predict(url)
    # result
    result = {"prediction": pred}
    # output
    return result

# ---