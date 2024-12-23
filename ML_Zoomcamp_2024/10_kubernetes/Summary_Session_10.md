![ML Zoomcamp Illustration](https://github.com/maxim-eyengue/Python-Codes/blob/main/ML_Zoomcamp_2024/zoomcamp.jpg)
---


# 📚 **Session 10 Summary - Machine Learning Zoomcamp**

## 10.1 🚀 **Kubernetes and Tensorflow Serving**

In this session, we will serve an **image classifier** to help users categorize clothes 🧥👕👗 as in the last session.  

### **Tools and Process**  
1️⃣ We'll use **TensorFlow Serving**, a specialized tool from the TensorFlow ecosystem, built just for **serving machine learning models**. 🚀  
   - It's a **C++ library** that focuses only on **inference** (i.e., making predictions).  
   - It takes an image as an input (in the form of a matrix, 📊) and returns an **array of scores** 🧮, representing predictions for each category.  

2️⃣ TensorFlow Serving communicates using **gRPC**, a high-performance protocol developed by Google 🌐. It's super-efficient and lightning-fast ⚡ for sending and receiving data.  

3️⃣ To make this system easy for users, we'll build a **gateway** using **Flask** 🐍:  
   - The gateway will allow users to input an **image link**.  
   - It downloads the image, resizes it, converts it to the right format (a NumPy array), and sends it to TensorFlow Serving for prediction.  
   - Once TensorFlow Serving responds with scores, the gateway converts them into a **JSON response** 📝 that shows the **categories** and their corresponding **probabilities**.  

4️⃣ On the **website**, users will only need to provide the image link 🌐📸, and they’ll get the image classification as the output 🎯.  

### **Deployment Architecture**  
🏗 Both components, **Flask Gateway** and **TensorFlow Serving**, will run inside **Kubernetes**. Kubernetes makes it easier to:  
   - Scale the system as needed 🔄.  
   - Ensure smooth communication between the gateway and TensorFlow Serving.  

### **How It Works**  
- **Gateway (Flask)**:  
  - 📥 Downloads and processes images.  
  - 🔄 Converts them to the required format (NumPy array).  
  - ⚙️ Post-processes predictions into user-friendly JSON.  
  - **Runs on CPUs** because the tasks are lightweight.  

- **TensorFlow Serving**:  
  - 🚀 Performs fast predictions using a pre-trained model.  
  - **Runs on GPUs** for high-speed computations.  

### **Scalability with Kubernetes**  
With Kubernetes, we can independently scale these components for maximum efficiency:  
- 🖥 **5 CPU instances** of the Flask Gateway for processing images.  
- 🎮 **2 GPU instances** of TensorFlow Serving for making predictions.  

This example setup ensures a smooth user experience while handling different workloads seamlessly 💡.  

---

## 10.2 TensorFlow Serving 🚀

TensorFlow Serving is a tool provided by TensorFlow for serving machine learning models in production environments. To use TensorFlow Serving, the Keras model trained earlier needs to be converted into a specific format called `saved_model`.

### Steps to Serve the Model:
1. **Model Conversion:**
   Convert the Keras model to the `saved_model` format by running the appropriate export command or using Keras' `model.save()` function with the `saved_model` format. 🛠️
   
2. **Inspect the Model:**
   After conversion, inspect the saved model to gather input and output information using the following command:
   ```bash
   !saved_model_cli show --dir clothing-model --all
   ```
   This command displays details such as input and output tensor names, which are crucial for running the model. 🔍

3. **Run the Model with Docker:**
   Use Docker to run the model by executing the following command:
   ```docker
   docker run -it --rm \
      -p 8500:8500 \  # Port mapping 🌐
      -v "$(pwd)/clothing-model:/models/clothing-model/1" \  # Volume mounting (maps the model directory) 📂
      -e MODEL_NAME="clothing-model" \  # Set the model name as an environment variable 🧩
      tensorflow/serving:2.7.0  # TensorFlow Serving Docker image 🐳
   ```
   - **`-p 8500:8500`**: Maps port 8500 on the host to port 8500 in the container, allowing external access.
   - **`-v`**: Mounts the local `clothing-model` directory into the container's `/models/clothing-model/1` path.
   - **`-e MODEL_NAME`**: Specifies the model name, allowing TensorFlow Serving to recognize and load it.

4. **Notebook Integration:**
   After launching the Docker container, create a [notebook](code/zoomcamp/tf_serving.ipynb) to connect to TensorFlow Serving and make predictions. 📓

### Notes:
- gRPC will be used to establish an insecure channel for communication. ⚡
- When components are deployed in Kubernetes, TensorFlow Serving will not be accessible externally by default, making insecure channels acceptable for internal communication. 🛡️

---

## 10.3 Creating a pre-processing service
We will turn the jupyter noteboook created into a flask application.

docker run -it --rm \
   -p 8500:8500 \  
   -v "$(pwd)/clothing-model:/models/clothing-model/1" \  
   -e MODEL_NAME="clothing-model" \ 
   tensorflow/serving:2.7.0 





* Converting the notebook to a Python script
* Wrapping the script into a Flask app
* Creating the virtual env with Pipenv
* Getting rid of the tensorflow dependency

## 10.4 Running everything locally with Docker-compose

* Preparing the images 
* Installing docker-compose 
* Running the service 
* Testing the service

## 10.5 Introduction to Kubernetes

* The anatomy of a Kubernetes cluster

## 10.6 Deploying a simple service to Kubernetes

* Create a simple ping application in Flask
* Installing kubectl
* Setting up a local Kubernetes cluster with Kind
* Creating a deployment
* Creating a service 

## 10.7 Deploying TensorFlow models to Kubernetes

* Deploying the TF-Serving model
* Deploying the Gateway
* Testing the service

## 10.8 Deploying to EKS

* Publishing the image to ECR
x'][8uuozg a EKS cluster on AWS

## 10.9 Summary

* TF-Serving is a system for deploying TensorFlow models
* When using TF-Serving, we need a component for pre-processing 
* Kubernetes is a container orchestration platform
* To deploy something on Kubernetes, we need to specify a deployment and a service
* You can use Docker compose and Kind for local experiments



---

# 🎯 **Key Takeaways** 







   
---