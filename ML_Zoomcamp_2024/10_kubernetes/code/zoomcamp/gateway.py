#!/usr/bin/env python
# coding: utf-8

### Tensorflow-Serving

# Necessary import
import grpc
import tensorflow as tf
from keras_image_helper import create_preprocessor
from tensorflow_serving.apis import predict_pb2, prediction_service_pb2_grpc
from flask import Flask, request, jsonify

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
# address where tf-serving is running
host = 'localhost:8500'
# Channel to access the port
channel = grpc.insecure_channel(host) # use secure when not running locally to add authentication
# To communicate with the service for making predictions
stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)
# Batch images preprocessor
preprocessor = create_preprocessor('xception', target_size = (299, 299))

# Function to turn data into protobuf format for sending requests
def np_to_protobuf(data):
    return tf.make_tensor_proto(data, shape = data.shape)

# Function to prepare requests
def prepare_request(X):
    # Initialize the request
    pb_request = predict_pb2.PredictRequest()

    # Specify the model name
    pb_request.model_spec.name = 'clothing-model'
    # Specify the name of the signature
    pb_request.model_spec.signature_name = 'serving_default'
    # Specify the input data
    pb_request.inputs['inputs'].CopyFrom(np_to_protobuf(X))

    # return request
    return pb_request

# Funstion to prepare response
def prepare_response(pb_response):
    # Get predictions
    preds = pb_response.outputs['output_0'].float_val
    # return classes and predictions
    return dict(zip(classes, preds))

# Function for makig predictions
def predict(url):
    # Input batch
    X = preprocessor.from_url(url)
    # Prepare request
    pb_request = prepare_request(X)

    # Send request for making predictions
    pb_response = stub.Predict(pb_request, timeout = 20.0)
    # Get predictions
    response = prepare_response(pb_response)

    # output
    return response


# Initialize the app
app = Flask('gateway')

# Flask service
@app.route('/predict', methods = ['POST'])
def predict_endpoint():
    # Get the data
    data = request.get_json()
    # Get url
    url = data['url']
    # Get result
    result = predict(url)
    # output
    return jsonify(result)

# Check file name
if __name__ == '__main__':
    # run app
    app.run(debug = True, host = '0.0.0.0', port = 9696)

    ### For testing quickly comment the line above
    ### and uncomment the following ones
    # Get url
    # url = 'http://bit.ly/mlbookcamp-pants'
    # Get response
    # response = predict(url)
    # output
    # print(result)


# ---