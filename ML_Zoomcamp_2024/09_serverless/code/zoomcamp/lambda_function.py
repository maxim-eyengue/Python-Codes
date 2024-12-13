#!/usr/bin/env python
# coding: utf-8
### Inference with TF-lite model

# Necessary import
import tflite_runtime.interpreter as tflite_int # to avoid depending on tensorflow
from keras_image_helper import create_preprocessor

# Initialize data preprocessor
preprocessor = create_preprocessor('xception', target_size = (299, 299))

# Load the model
interpreter = tflite_int.Interpreter(model_path = 'clothing-model.tflite')
# Load the weights from the model to memory (necessary with tf-lite models)
interpreter.allocate_tensors()

# Specify the input
input_index = interpreter.get_input_details()[0]['index']
# Specify the output
output_index = interpreter.get_output_details()[0]['index']

# image url
url = 'http://bit.ly/mlbookcamp-pants'
# Target classes
classes = [
    'dress',
    'hat',
    'longsleeve',
    'outwear',
    'pants',
    'shirt',
    'shoes',
    'shorts',
    'skirt',
    't-shirt'
]

# function for making inference
def predict(url):
    # preprocess image
    X = preprocessor.from_url(url)

    # Initialize the input of the interpreter
    interpreter.set_tensor(input_index, X)
    # Invoke computations in the neural network
    interpreter.invoke()
    # Fetch predictions
    preds = interpreter.get_tensor(output_index)
    # Get float predictions as usual python list (json serializable)
    float_predictions = preds[0].tolist()

    # return classes and predicted probabilities 
    return dict(zip(classes, float_predictions))

# Lambda function handler
def lambda_handler(event, context = None):
    # image url
    url = event['url']
    # Compute prediction
    result = predict(url)
    # output
    return result


# ---