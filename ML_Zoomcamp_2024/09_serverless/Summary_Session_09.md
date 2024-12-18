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
- **Cost-Effective 💰:** Pay only for requests and compute time: idle (waiting) time is free!  
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

## 9.3 TensorFlow Lite 🧩

TensorFlow is a relatively large framework, with an unpacked size of approximately 1.7 GB. The size of such frameworks is an important consideration for several reasons:  

- **📜 Historical Constraints:** Previously, AWS Lambda imposed a limit of `50 MB` for package sizes. While Docker has since increased these limits to 10 GB, the size of the framework still plays a crucial role in certain scenarios.  
- **⚡ Performance Issues with Large Images:** Large frameworks like TensorFlow result in increased storage costs, longer initialization times (e.g., for invoking a Lambda function), slower loading times, and a significantly larger RAM footprint.  

### Optimizing with TensorFlow Lite 🚀
To address these challenges, TensorFlow Lite (TF-Lite) provides a lightweight alternative designed specifically for inference tasks (i.e., making predictions with `model.predict(X)`) and excludes training functionality. Using TF-Lite can significantly reduce model size and improve performance.  

### Model Conversion to TensorFlow Lite 🔄
To use TensorFlow Lite, the original TensorFlow model needs to be converted into the TF-Lite format. Below, we demonstrate this process using a pre-trained model.  

📥 **Step 1: Download and Save the Model**  
First, download and save the model as `clothing-model.h5`:  

```bash
wget https://github.com/DataTalksClub/machine-learning-zoomcamp/releases/download/chapter7-model/xception_v4_large_08_0.894.h5 -O clothing-model.h5
```  

This model can be used to make predictions, such as classifying an image of pants.  

📤 **Step 2: Convert the Model to TF-Lite**  
We will convert the model to the TF-Lite format to optimize it for inference tasks. [see [notebook](code/zoomcamp/tensorflow_model.ipynb)] 

---

## 9.4 Preparing the Lambda Code

To prepare the Lambda code, we will start by converting the inference logic written in our [notebook](code/zoomcamp/tensorflow_model.ipynb) into a Python script. This can be achieved using the following command:  

```bash
jupyter nbconvert --to script tensorflow_model.ipynb
```

After conversion, we will clean up the generated script and define a `predict()` function to handle inference. Once finalized, the script will be saved as `lambda_function.py`. The `predict()` function can then be tested in the terminal with the following code:

```python
# Import the module
import lambda_function

# Make a prediction
lambda_function.predict('http://bit.ly/mlbookcamp-pants')
```

Next, we will extend the script by adding a handler function for Lambda. This function will serve as the entry point for processing events. The updated script can then be tested using the terminal with an example event:

```python
# Import the module
import lambda_function

# Define a sample event
event = {'url': 'http://bit.ly/mlbookcamp-pants'}

# Invoke the Lambda handler
lambda_function.lambda_handler(event)
```

This step ensures that the script is ready for deployment as an AWS Lambda function.

---

## 🚢 9.5 Preparing a Docker Image  

To deploy our model to **`AWS Lambda`**, we need to create a [Dockerfile](code/zoomcamp/Dockerfile) 📝. This Dockerfile will:  
✅ Specify the base image (an AWS-provided image)  
✅ Include the necessary libraries  
✅ Package the model file and Python script  
✅ Configure the Lambda function entry point  

### 🛠️ Here's the final Dockerfile with explanatory comments:  
```docker  
# 📦 Use AWS Lambda's Python 3.10 runtime as the base image  
FROM public.ecr.aws/lambda/python:3.10  

# 🧰 Install required libraries  
RUN pip install numpy==1.23.1  
RUN pip install --no-deps https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl  

# 🗂️ Copy the model and Lambda function script to the image  
COPY clothing-model.tflite .  
COPY lambda_function.py .  

# 🚀 Specify the Lambda function entry point  
CMD [ "lambda_function.lambda_handler" ]  
```  

### 🏗️ Building and Running the Docker Image  

1. **🔨 Build the Docker image**:  
   ```bash  
   docker build -t clothing-model .  
   ```  

2. **🚀 Run the Docker image locally**:  
   ```bash  
   docker run -it --rm -p 8080:8080 clothing-model:latest  
   ```  

   🎉 This will start the container and expose it on **port 8080** for testing.  

### 🧪 Testing the Lambda Function  

Create a [test script](code/zoomcamp/test.py) 🖥️ to verify that the Lambda function works as expected.  

### 🔑 Important Notes  

- 🛡️ The `tflite` library installed in the Dockerfile **must match** the environment in which it will run, specifically `Amazon Linux`. This ensures that the required `GLIBC_2.27` dependency is available.  
- 📥 To achieve this, the `tflite` library is precompiled in the target environment. By pointing to the precompiled `.whl` file during the build process, the library is installed correctly. For more details, refer to [this compilation guide](https://github.com/alexeygrigorev/tflite-aws-lambda/).  

🎯 By following these steps, you can successfully package and deploy your Lambda function using Docker.  

--- 

## 9.6 Creating the Lambda function 🚀

We’ve previously explored how to create and deploy a Lambda function `from scratch` directly on AWS. Now, let's deploy the Docker image we recently built to Lambda. Here's how to proceed step-by-step:

### **Step 1: Access Lambda and Choose the Container Image Option 🖥️**
In the **AWS Management Console**, click on `Lambda` and create a function. Choose the `Container image` option. To proceed, you'll need to publish the Docker image to **Amazon Elastic Container Registry (ECR)** to obtain the `Docker container image URL`.

### **Step 2: Publish Your Docker Image to Amazon ECR 🐳**

1. **Create a Repository**:
   - Navigate to **Amazon ECR** and create a repository to publish images.
   - Alternatively, use the AWS CLI:
     ```bash
     aws ecr create-repository --repository-name clothing-tflite-images
     ```
   - Copy the `repositoryUri` after creating the repository.

2. **Install and Configure AWS CLI**:
   - Install the AWS CLI:
     ```bash
     pip install awscli
     ```
   - If running it for the first time, configure it:
     ```bash
     aws configure
     ```
     You'll be prompted to enter:
     - Your **AWS Access Key ID**.
     - Your **AWS Secret Access Key**.
     - The **Default region name** assigned to you.
     - The **Default output format** (JSON, text, or table).

3. **Log In to Your ECR Repository 🔐**:
   - Use the command:
     ```bash
     aws ecr get-login --no-include-email | sed 's/[0-9a-zA-Z=]\{20,\}/PASSWORD/g'
     ```
     - **`--no-include-email`**: Avoids outputting the email.
     - **`sed` utility**: Replaces sensitive data (e.g., your password) with `PASSWORD` for safety. 

   - Execute the login command:
     ```bash
     $(aws ecr get-login --no-include-email)
     ```
     the `$` sign helps to execute what ever the command in brackets outputs.

4. **Tag and Push Your Docker Image**:
   - Define the remote URI, using a `TAG` for our image, and the copied `repositoryUri`, to identify account, region, registry, and registry_uri (`PREFIX`):
     ```bash
     ACCOUNT=************
     REGION=**-****-*
     REGISTRY=clothing-tflite-images
     PREFIX=${ACCOUNT}.dkr.ecr.${REGION}.amazonaws.com/${REGISTRY}
     TAG=clothing-model-xception-v4-001

     # URI for the image we will push to ECR
     REMOTE_URI=${PREFIX}:${TAG}
     ```
   - Verify the URI:
     ```bash
     echo ${REMOTE_URI}
     ```
   - Tag the Docker image:
     ```bash
     docker tag clothing-model:latest ${REMOTE_URI}
     ```
   - Push the image to ECR:
     ```bash
     docker push ${REMOTE_URI}
     ```

5. **Verify on Amazon ECR ✅**:
   - Check that the image has been successfully pushed.

### **Step 3: Create a Lambda Function Using the Container Image ⚙️**

1. **Set Up the Function**:
   - Go back to **AWS Lambda** and create a function.
   - Name it: `clothing-classification`.
   - Provide the container image URI (`REMOTE_URI`).
   - Alternatively, browse and select the image from your repository.

2. **Adjust Configuration Settings 🛠️**:
   - Increase the timeout in **General Configuration** > **Configuration Panel**:
     - Set the timeout to **30 seconds** (default is 3 seconds).
   - Increase the memory allocation to **1GB**.
   - Save your changes and wait a moment.

3. **Test Your Lambda Function 🧪**:
   - Use the image url link in your [test file](code/zoomcamp/test.py) to create a test event.
   - Note: The function will improve with repeated runs.

### **Important Notes 📌**

- **Pricing**: Check this [link](https://aws.amazon.com/lambda/pricing/) for pricing details. Specify your region and memory usage.
- **Optimization**: There’s a relationship between memory allocation and speed. Experiment to find the best configuration for your needs.

---

## 9.7 API Gateway: Exposing the Lambda Function 🚀  

We want to expose a Lambda function as a web service. To achieve this, we'll use **API Gateway**—an AWS service that allows us to expose various AWS services as web services, including AWS Lambda.  

1. **Search and Create API**  
   - On AWS, search for `API Gateway` and click on **Create API**.  
   - Select the **Build** button for **REST API** to have complete control over requests, responses, and API management capabilities.  
   - Note: This works with `Lambda`, `HTTP`, and `AWS Services`.  

2. **Set Up the API**  
   - Enter the name of your API and a description, then click **Create API** again.  
   - Under **Actions**, we need to create a **resource**.  
     - In REST APIs, resources are typically nouns (e.g., users, items).  
     - Here, we’ll name it `predict` for consistency with previous sessions.  
   - Click on **Create Resource**.  

3. **Create a Method for the Resource**  
   - Using the **Actions** button again, create a method to invoke the endpoint.  
   - Choose `POST` as the request type since we’re sending data to the service.  
   - For the **Integration type**, select `Lambda Function` and enter the name of your Lambda function (e.g., `clothing-classification`).  
   - Click **Save** and **Add Permission** to allow API Gateway to invoke the function.  

4. **Test the API**  
   - Click the **Test** link, add a sample request (e.g., `{'url': 'http://bit.ly/mlbookcamp-pants'}`), and run the test to get a response.  
   - The more you execute, the faster the response becomes. 🏃‍♂️💨  

5. **Deploy the API**  
   - Using the **Actions** button, select **Deploy API** to expose the function.  
   - Create a new deployment stage by providing a name and optional description.  
   - After deployment, you’ll get a URL that you can use to test your API.  

6. **Test with a Script**  
   - Update your [test script](code/zoomcamp/test.py) by replacing the previous local address with the new URL (e.g., `<obtained URL>/predict`).  
   - Test it in your terminal with: `python test.py`. 🧪✨  


### ⚠️ Important  
Be cautious not to expose your service to the entire world! 🔒  

---

# 🎯 **Key Takeaways**  
To create efficient, cost-effective, and scalable ML deployments! 

### 🚀 **AWS Lambda**  
- AWS Lambda enables deploying models without managing servers, allowing you to focus solely on writing the Lambda function.  
- Ideal for low-volume requests as you pay only when requests are made.  
- Use serverless solutions to improve performance and simplify infrastructure management.  
- 🔗 Expose Lambda functions via **API Gateway** for seamless integration.  

### 🧩 **TensorFlow Lite**  
- TensorFlow Lite is a lightweight alternative to TensorFlow, designed specifically for inference tasks.  
- Use it to build scalable, cost-effective, and lightweight deployment pipelines for ML models.  

### 📦 **Docker for Deployment**  
- Package your code in a Docker container, test it locally, and deploy it to Lambda for reliable performance.  
- Avoid surprises by validating your containerized application beforehand.  
- Take advantage of modern tools like **Docker**, **TensorFlow Lite**, and **AWS Lambda** to package and deploy ML models efficiently.  

### 🔍 **Additional Insights**  
- Explore similar serverless services from **Google Cloud** and **Microsoft Azure**.  
- AWS Lambda supports various ML libraries like **Scikit-Learn** and **XGBoost**, expanding its versatility.   
---
