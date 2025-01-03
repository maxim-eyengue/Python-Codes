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
   ```bash
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

## 10.3 🚀 Creating a Pre-processing Service  
We'll convert the Jupyter [notebook](code/zoomcamp/tf_serving.ipynb) into a Flask application using the command:  
```bash
jupyter nbconvert --to script
```  
Next, we'll rename the generated script as [gateway.py](code/zoomcamp/gateway.py). 🛠️ Afterward, we'll clean up the script and transform it into a Flask application.  

✨ To manage dependencies, we can use `pipenv` to set up an isolated environment with the necessary libraries.  

⚡ To avoid including the full TensorFlow package, there's a lighter-weight alternative called `tensorflow-cpu`, which can handle the transformation of our data into protobuf format. However, this version is still quite large (~443 MB).  

💡 A more lightweight option is `tensorflow-protobuf`, a specialized version that includes only the required protobuf files (compiled), allowing us to convert NumPy arrays to protobuf format.  

📦 To install it, use the following command:  
```bash
pipenv install tensorflow-protobuf==2.7.0
```  

---

## 10.4 Running Everything Locally with Docker-Compose 🚀

We will use Docker Compose to run the gateway service and the TensorFlow Serving model together, locally. 

### 🛠️ Preparing Docker Images
First, we need to prepare and build the Docker images for both the gateway and the TensorFlow Serving model. 

For the model, we will build the Docker image with the following command:
```bash
 docker build -t zoomcamp-10-model:xception-v4-001 -f image-model.dockerfile .
```
To run the model Docker image, execute:
```bash
 docker run -it --rm \
    -p 8500:8500 \ 
    zoomcamp-10-model:xception-v4-001 
```
To quickly test the model Docker image, we can modify the [gateway script](code/zoomcamp/gateway.py) and run it with:
```bash
pipenv run python gateway.py
```

Next, we create a Docker image for the gateway using the corresponding [Dockerfile](code/zoomcamp/image-gateway.dockerfile):
```bash
 docker build -t zoomcamp-10-gateway:001 -f image-gateway.dockerfile .
```
Run the gateway image with:
```bash
 docker run -it --rm \
    -p 9696:9696 \ 
    zoomcamp-10-gateway:001
```

### 🔗 Linking Containers with Docker-Compose
When both services are running, we can test them using the [test script](code/zoomcamp/test.py). However, an error will occur because the gateway cannot reach the TensorFlow Serving model. This happens because the two Docker containers run separately on different ports, and the test script attempts to send requests to the TensorFlow model via the gateway without them being linked.

To resolve this, we need to link the two services by placing them in the same network. This allows them to communicate with each other. A convenient way to achieve this is by using Docker Compose, which runs multiple Docker containers and links them within a single network.

### 📥 Installing Docker Compose
If you are using Docker Desktop, Docker Compose is already installed. Otherwise, follow the installation guide [here](https://docs.docker.com/compose/install/). To ensure the `docker-compose` command is available in your terminal, add it to your PATH by editing the `.bashrc` file:
```bash
nano ~/.bashrc
```
Add the following line at the end of the file (adjust `/bin` to the folder where Docker Compose is installed):
```bash
export PATH="$(HOME)/bin:${PATH}"
```
Save and exit.

### 📝 Creating the Docker-Compose File
We need to create a [docker-compose.yaml file](code/zoomcamp/docker-compose.yaml) to describe the containers we want to run.

The Flask app in our gateway component is configured to access the model at localhost `8500`. This results in the app trying to find the model within the gateway container, rather than the TensorFlow Serving container. To fix this, we will make the host configurable by importing `os` in the gateway script to access environment variables and set the model host using:
```python
os.getenv('TF_SERVING_HOST', 'localhost:8500')
```

Rebuild the gateway Docker image and run it with:
```bash
 docker run -it --rm \
    -p 9696:9696 \ 
    zoomcamp-10-gateway:002
```

Next, update the [docker-compose.yaml file](code/zoomcamp/docker-compose.yaml) to include the new gateway image and environment variables:
```yaml
environment:
  - TF_SERVING_HOST=clothing-model:8500
```

Within Docker Compose, each container is accessible by its name (e.g., `gateway:9696` and `tf-serving:8500`). 

To run Docker Compose, use the following command, which looks for `docker-compose.yaml` in the current directory and starts the containers:
```bash
 docker-compose up
```

Now, the two services can communicate. Test the service using the test script:
```bash
python test.py
```

### 🏃 Running Docker-Compose in Detached Mode
To run Docker Compose in detached mode and return to the terminal, use:
```bash
 docker-compose up -d
```
Check running containers with:
```bash
 docker ps
```
To stop all running containers, execute:
```bash
 docker-compose down
```

---

## 🚀 10.5 Introduction to Kubernetes  
Kubernetes, also known as **K8s**, is an open-source system for automating the deployment, scaling, and management of containerized applications.  

### 🧩 Anatomy of a Kubernetes Cluster  
Imagine we have a Kubernetes cluster. Within this cluster, there are **nodes** (servers or computers running the processes). On these nodes, we find 🐳 **pods:** containers that run specific images, with allocated resources like **RAM/CPU**.  

Pods are typically grouped into **deployments** 📦. All pods in a deployment share the same Docker image and configuration. Think of a deployment as a set of identical workers, ready to process requests. For example, our **gateway service** can be structured as a deployment.  

- Larger pods require more resources 💪.  
- In addition to pods, Kubernetes uses **services** 🛎️, such as:  
  - 🌐 `gateway service`: An entry point for external requests.  
  - 🤖 `tf-model service`: Manages communication with model-serving pods.  

### 🔄 How it Works  
1. When a user uploads an image 🖼️ to the website, the request first reaches the **gateway service**.  
2. The gateway routes the request to one of the available pods, distributing traffic evenly (load balancing ⚖️).  
3. After pre-processing, the gateway deployment forwards the request to the **model service**.  
4. The model service routes the request to a pod in the `tf-serving` deployment.  
5. Predictions are made 🔮 and sent back to the user, following the same path.  

### 📍 Service Types  
Kubernetes services act as entry points to route requests to the correct pods:  
- **External Services** (`Load Balancer` 🌐): Accessible from outside the cluster. Example: `gateway service`.  
- **Internal Services** (`Cluster IP` 🔒): Accessible **only** within the cluster. Example: `model service`.  

At the front of the cluster, there’s an **entry point** called `INGRESS` 🚪. This directs user traffic to the appropriate external services.  

### ⚙️ Scaling with Kubernetes  
To handle multiple users simultaneously, Kubernetes can launch additional pods 🚀.  
- As traffic increases, Kubernetes **automatically scales** the deployment up 🆙.  
- When traffic decreases, it scales down 🛑 to save resources.  
- This dynamic scaling is managed by the **Horizontal Pod Autoscaler (HPA)** 📊.  
- If existing nodes are overwhelmed, Kubernetes can even request the creation of new nodes to handle the extra load.  

Kubernetes ensures that your application stays responsive, efficient, and ready to scale at any moment!  

---

## 10.6 Deploying a simple service to Kubernetes

* Create a simple ping application in Flask
* Installing kubectl
* Setting up a local Kubernetes cluster with Kind
* Creating a deployment
* Creating a service 

---

## 10.7 Deploying TensorFlow models to Kubernetes

* Deploying the TF-Serving model
* Deploying the Gateway
* Testing the service

---

## 10.8 Deploying to EKS

* Publishing the image to ECR with a EKS cluster on AWS

---

# 🎯 **Key Takeaways** 

* TF-Serving is a system for deploying TensorFlow models
* When using TF-Serving, we need a component for pre-processing 
* Kubernetes is a container orchestration platform
* To deploy something on Kubernetes, we need to specify a deployment and a service
* You can use Docker compose and Kind for local experiments





   
---