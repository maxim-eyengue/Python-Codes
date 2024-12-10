![ML Zoomcamp Illustration](https://github.com/maxim-eyengue/Python-Codes/blob/main/ML_Zoomcamp_2024/zoomcamp.jpg)
---


# 📚 **Session 9 Summary - Machine Learning Zoomcamp**

# 🚀 **Serverless Deep Learning**

This session focuses on deploying the clothes classification model we trained in the previous session. The model categorizes images of clothing items (e.g., 👕 t-shirts, 👖 pants, etc.) uploaded by users on a website. Deployment will be done using **AWS Lambda**, a serverless solution to execute code without managing servers.

---

## **9.1 🌐 Introduction to Serverless**

In the last session, we built and trained deep learning models using `Keras` and `TensorFlow` in the `Saturn Cloud` environment. This week, we move forward to deployment with **AWS Lambda**.  

### 💡 **What is AWS Lambda?**
AWS Lambda is a serverless compute service by AWS that lets you run applications and models without provisioning or managing servers. For this use case, Lambda will process image classification requests, where users provide 🌟 **image URLs**, and the deployed model returns 🔍 **categories** and 📊 **confidence scores**.


### **Topics to cover:**
- **🔀 AWS Lambda vs. Other Deployment Approaches** :
   Learn about serverless architecture and its benefits over traditional methods.

- **📦 Introduction to TensorFlow Lite** :
   Discover how TensorFlow Lite is optimized for lightweight, serverless environments.

- **🔄 Model Conversion to TensorFlow Lite** :
   Convert the trained model from TensorFlow to TensorFlow Lite for improved compatibility and performance.

- **🐋 Packaging with Docker** :
   Containerize the TensorFlow Lite model and dependencies using Docker for seamless deployment.

- **☁️ Deploying to AWS Lambda** :
   Step-by-step deployment of the Dockerized model to AWS Lambda.

- **🌐 Exposing Lambda with API Gateway** :
   Set up an API Gateway to make the Lambda function accessible as a user-friendly web service.
   
---


## 9.2 AWS Lambda

* Intro to AWS Lambda
* Serverless vs serverfull


## 9.3 TensorFlow Lite

* Why not TensorFlow
* Converting the model
* Using the TF-Lite model for making predictions


## 9.4 Preparing the Lambda code

* Moving the code from notebook to script
* Testing it locally


## 9.5 Preparing a Docker image

* Lambda base images
* Preparing the Dockerfile
* Using the right TF-Lite wheel


## 9.6 Creating the lambda function

* Publishing the image to AWS ECR
* Creating the function
* Configuring it
* Testing the function from the AWS Console
* Pricing


## 9.7 API Gateway: exposing the lambda function

* Creating and configuring the gateway


## 9.8 Summary 

* AWS Lambda is way of deploying models without having to worry about servers
* Tensorflow Lite is a lightweight alternative to Tensorflow that only focuses on inference
* To deploy your code, package it in a Docker container
* Expose the lambda function via API Gateway


## 9.9 Explore more

* Try similar serverless services from Google Cloud and Microsoft Azure
* Deploy cats vs dogs and other Keras models with AWS Lambda
* AWS Lambda is also good for other libraries, not just Tensorflow. You can deploy Scikit-Learn and XGBoost models with it as well.

---

# 🎯 **Key Takeaways**
This session demonstrates how to:  
✅ Build a scalable, cost-effective, and lightweight deployment pipeline.  
✅ Leverage serverless solutions to optimize performance and simplify infrastructure management.  
✅ Package and deploy machine learning models effectively with modern tools like Docker, TensorFlow Lite, and AWS Lambda.
---
