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

## 10.2 Tensorflow Serving

It is the tool from tensorflow that can be used for serving models. For this to work we need to convert the
keras model that we have trained previously, to special format: saved_model. We will load th





* The saved_model format
* Running TF-Serving locally with Docker
* Invoking the model from Jupyter





---

## 10.3 Creating a pre-processing service

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

* Creating a EKS cluster on AWS
* Publishing the image to ECR

## 10.9 Summary

* TF-Serving is a system for deploying TensorFlow models
* When using TF-Serving, we need a component for pre-processing 
* Kubernetes is a container orchestration platform
* To deploy something on Kubernetes, we need to specify a deployment and a service
* You can use Docker compose and Kind for local experiments



---

# 🎯 **Key Takeaways** 







   
---