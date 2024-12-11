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


## 9.2 AWS Lambda 🌟

AWS Lambda is a **serverless computing service** that lets you execute code without worrying about managing servers. Here's an overview of how it works and its benefits:  


### **Setting Up a Lambda Function 🛠️**
1. **Accessing Lambda:**
   - Go to the AWS Management Console and search for the `Lambda` service.

2. **Creating a Function:**
   - Choose the `Author from scratch` option.
   - Name your function (e.g., `mlzoomcamp-test`).
   - Select the runtime environment (e.g., `Python 3.9`) and architecture (`x86_64`).

3. **Understanding Function Parameters:**
   - **`event`:** Contains the input data passed to the function (e.g., a JSON payload).
   - **`context`:** Provides details about the invocation, configuration, and execution environment.

4. **Updating the Default Function:**
   - Edit `lambda_function.py` with custom logic. Example:  
     ```python
     def lambda_handler(event, context):
         print("Parameters:", event) # Print input parameters
         url = event["url"]  # Extract URL from input
         return {"prediction": "clothes"}  # Sample response
     ```

### **Testing and Deployment 🚀**
1. **Create a Test Event:**
   - Define a mock input to simulate real-world data.  

2. **Deploy Changes:**
   - Save and deploy the function to apply updates.  

3. **Test Your Function:**
   - Run the function with the test event to ensure it works as expected.

### **Advantages of AWS Lambda ✅**
- **Serverless Architecture 🖥️:** No need to provision or manage servers.  
- **Cost-Effective 💰:** Pay only for requests and compute time—idle time is free!  
- **Automatic Scaling 📈:** Adjusts automatically based on request volume.  
- **Ease of Use 🎯:** Focus on coding; AWS handles infrastructure.


### **Use Cases 🌐**
- **Dynamic Link Management:**
  - Automatically redirect users to updated invite links for communities like DataTalks.Club. Avoid expired links with a Lambda function reading from a config file.  

- **Image Processing 🖼️:**
  - Use Lambda to process uploaded images (e.g., resizing or converting formats) in real time. For example, automatically resizing user-uploaded profile pictures for a social media app.

### **Free Tier Benefits 🎁**
- **1 Million Requests/Month:** Free usage within this limit.  
- **400,000 GB-seconds:** Monthly compute time included for free.  

AWS Lambda is an excellent solution for real-time tasks, lightweight applications, and scalable solutions, enabling you to innovate faster without infrastructure concerns. 🚀✨

---

## 9.3 TensorFlow Lite

TensorFlow is a relatively large framework, with an unpacked size of approximately 1.7 GB. The size of such frameworks is an important consideration for several reasons:  

- **Historical Constraints:** Previously, AWS Lambda imposed a limit of `50 MB` for package sizes. While Docker has since increased these limits to 10 GB, the size of the framework still plays a crucial role in certain scenarios.  
- **Performance Issues with Large Images:** Large frameworks like TensorFlow result in increased storage costs, longer initialization times (e.g., for invoking a Lambda function), slower loading times, and a significantly larger RAM footprint.  

### Optimizing with TensorFlow Lite  
To address these challenges, TensorFlow Lite (TF-Lite) provides a lightweight alternative designed specifically for inference tasks (i.e., making predictions with `model.predict(X)`) and excludes training functionality. Using TF-Lite can significantly reduce model size and improve performance.  

### Model Conversion to TensorFlow Lite  
To use TensorFlow Lite, the original TensorFlow model needs to be converted into the TF-Lite format. Below, we demonstrate this process using a pre-trained model. First, download and save the model as `clothing-model.h5`:  

```bash
wget https://github.com/DataTalksClub/machine-learning-zoomcamp/releases/download/chapter7-model/xception_v4_large_08_0.894.h5 -O clothing-model.h5
```

This model can be used to make predictions, such as classifying an image of pants. We will convert the model to the TF-Lite format to optimize it for inference tasks.  

---

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
