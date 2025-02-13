![ML Zoomcamp Illustration](../files/zoomcamp.jpg)
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
export PATH="${HOME}/bin:${PATH}"
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

## 🚀 10.6 Deploying a Simple Service to Kubernetes

In this section, we will deploy a simple ping application (built with Flask) to a Kubernetes cluster. The ping application is located in the [ping folder](code/zoomcamp/ping/).

### 🛠️ Setting Up the Application
1. Install `flask` and `gunicorn` in the `ping` folder using:
   ```bash
   pipenv install flask gunicorn
   ```
2. Since there is another Pipfile in the parent directory, create a new Pipfile in the `ping` folder before installing the dependencies:
   ```bash
   touch Pipfile
   ```
3. Create a [Dockerfile](code/zoomcamp/ping/Dockerfile) for the application and build the image:
   ```bash
   docker build -t ping:v001 .
   ```
   - We specify the tag `v001` instead of the default `latest` because `kind` (a local Kubernetes cluster) requires specific tags.
4. Run the image locally:
   ```bash
   docker run -it --rm -p 9696:9696 ping:v001
   ```
5. In another terminal, test it:
   ```bash
   curl localhost:9696/ping
   ```

### ☸️ Deploying to Kubernetes

#### 📥 Installing Kubernetes Tools
- Set up a local Kubernetes cluster using `kind` and `kubectl` (the tool to interact with clusters).
- If using Docker Desktop on Windows or macOS, `kubectl` is installed automatically. On Linux, install it manually using [this guide](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/).
- Alternatively, install `kubectl` from AWS by following [this link](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html#kubectl-install-update).


#### ⚙️ Installing `kind`
>>> You can follow the [link](https://kind.sigs.k8s.io/docs/user/quick-start/) to see the instructions.
- **🪟 Windows (Docker Desktop):**
   ```bash
   curl.exe -Lo kind-windows-amd64.exe https://kind.sigs.k8s.io/dl/v0.26.0/kind-windows-amd64
   ```
   - Rename the executable to `kind.exe` and move it to a binary folder in your `PATH`.
   - Use the `set` command to check and update your `PATH` variable.
- **🐧 Linux/WSL:**
   ```bash
   mkdir -p ~/bin # create a folder named bin in the home directory
   cd ~/bin # open the bin folder
   curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.26.0/kind-linux-amd64 # install kind
   chmod +x ./kind # make kind executable
   ```
   - Add `kind` to the `PATH` by editing `.bashrc`:
     ```bash
     nano ~/.bashrc # to edit the bash script. NB: save changes with CTRL + O and Enter, and exit with Ctrl + X
     export PATH="${HOME}/bin:${PATH}" # add kind to the path
     source ~/.bashrc # execute the bash script
     ```
   - Check the path enviroment variable:
   ```bash 
   echo $PATH
   ```
   - Verify the installation:
     ```bash
     which kind
     ```

### ⚒️ Creating a Kubernetes Cluster
```bash
kind create cluster
```
- If you encounter errors with `kind create cluster` on WSL2, specify the node image:
  ```bash
  kind create cluster --image kindest/node:v1.23.0
  ```

### 🗂️ Configuring `kubectl`
We need to configure `kubectl` to access the cluster created and use it:
```bash
kubectl cluster-info --context kind-kind
```
- To debug:
  ```bash
  kubectl cluster-info dump
  ```
- List services, pods, and deployments:
  ```bash
  kubectl get service
  kubectl get pod
  kubectl get deployment
  ```
- View active Docker processes, including `kind-control-plane`:
  ```bash
  docker ps
  ```
>>> We can install an extension for kubernetes on Visual Studio Code to make our work easier, as it proposes useful templates. Just typing deployment or service in this file is enough to get a template suggestion.

### 📄 Creating the Deployment
- Create a [deployment.yaml](code/zoomcamp/ping/deployment.yaml) file to specify how the pods in our deployment will look like:

 ```yaml
      apiVersion: apps/v1
      kind: Deployment
      metadata: 
        name: ping-deployment # name of the deployment
      spec:
        replicas: 1 # number of pods to create
        selector:
          matchLabels: # all pods that have the label app named 'ping' belong to 'ping-deployment'
            app: ping
        template: # template of pods (all pods within a deployment have the same configuration)
          metadata:
            labels: # each pod / app gets the same label (i.e., ping in our case)
              app: ping
          spec:
            containers: 
            - name: ping-pod # name of the container
              image: ping:v001 # docker image with tag
              resources: # pod resources
                limits:
                  memory: "128Mi" # 128 Mbytes of RAM
                  cpu: "500m" # 0.5 CPU
              ports:
              - containerPort: 9696 # port to expose
```
>>> Tip: the command `htop` helps to visualize resources. To make sure the resources allocated do no surpass the limit of our computer, you can install it as follows: 
```bash
sudo apt install && sudo apt upgrade
sudo apt install htop
sudo snap install htop
```
- Apply the deployment:
   ```bash
   kubectl apply -f deployment.yaml
   ```
- We can now check available pods (`kubectl get pod`), and then the only one created with a detailed description using the command: `kubectl describe pod pod-name`. If the pod is pending, as expected, load the Docker image into the cluster:
   ```bash
   kind load docker-image ping:v001
   ```
This command will allow the pods to change status from `<pending>` to `<running>`.

- Forward ports to test:
   ```bash
   kubectl port-forward pod/pod-name 9696:9696 # `Port-fowarding` can be used to test the deployment before creating a service, by connecting the ping application port of our kubernetes cluster to a port on our local computer using kubectl.
   curl localhost:9696/ping # to test the deployment by returning `PONG`
   ```

### 🌐 Creating the Service
- Create a [service.yaml](code/zoomcamp/ping/service.yaml):
   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: ping # service name
   spec:
     selector:
       app: ping # to understand which pods are qualified to receive the request (those labelled with `ping`)
     ports:
     - port: 80 # port in the service where the requests will be sent before being forwarded to the adequate pod port (`80`: default http port to get requests)
       targetPort: 9696 # port on the pod / container pod
   ```
- Apply the service configuration:
   ```bash
   kubectl apply -f service.yaml
   ```
- Check the service:
   ```bash
   kubectl get service # or `kubectl get svc`
   ```
>>> Note that the ping service type is `ClusterIP` (internal service). As we are using `kind` a local kubernetes cluster, services types don't really matter but with kubernetes clusters, it does matter when something is exposed out of kubernetes cluster or not. 
- Change the service type to `LoadBalancer` for external access and reapply the configuration. You can verify updates by checking services: this time the `EXTERNAL-IP` address is `<pending>` as it still needs to be configured. Now, use port-forwarding to simulate an external connection:
   ```bash
   kubectl port-forward service/ping 8080:80 # we use the port `8080` on our local computer instead of `80` to avoid permission requiremnts (you can use `sudo` and port `80`)
   curl localhost:8080/ping # test to return `PONG`
   ```

### ⚙️ Configure External Connections with MetalLB  
Set up and use `MetalLB` as an external load balancer.  

#### 1. 🚀 Install MetalLB  
Apply the MetalLB manifest to deploy it to your cluster:  
```bash
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.13.7/config/manifests/metallb-native.yaml
```  

#### 2. ⏳ Verify MetalLB Deployment  
Wait for the MetalLB pods (controller and speakers) to be ready:  
```bash
kubectl wait --namespace metallb-system \
             --for=condition=ready pod \
             --selector=app=metallb \
             --timeout=90s
```  

#### 3. 🛠️ Configure Address Pool for Load Balancers  
1. 🔍 Retrieve the IP address range from the Docker `kind` network:  
   ```bash
   docker network inspect -f '{{.IPAM.Config}}' kind
   ```  

2. 📝 Create an IP address pool using a `metallb-config.yaml` file:  
   ```yaml
   apiVersion: metallb.io/v1beta1
   kind: IPAddressPool
   metadata:
     name: example
     namespace: metallb-system
   spec:
     addresses:
     - 172.20.255.200-172.20.255.250
   ---
   apiVersion: metallb.io/v1beta1
   kind: L2Advertisement
   metadata:
     name: example
     namespace: metallb-system
   ```  

3. 📤 Apply the MetalLB configuration:  
   ```bash
   kubectl apply -f metallb-config.yaml
   ```  

#### 4. 📦 Deploy Application and Services  
Apply the deployment and service configurations:  
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```  

#### 5. 🌐 Retrieve the External Load Balancer IP  
```bash
kubectl get service
```  

#### 6. 🧪 Test the Load Balancer  
Verify the service by sending a request to the load balancer IP:  
```bash
curl <LB_IP>:80/ping
```  

---

## 🚀 10.7 Deploying TensorFlow Models to Kubernetes

We will create a folder with configuration files for the TensorFlow (TF) Serving model and the Gateway. 🗂️

### 🛠️ Model Deployment
Create a deployment configuration file for the model:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: tf-serving-clothing-model  # Model deployment name
spec:
  selector:
    matchLabels:
      app: tf-serving-clothing-model
  template:
    metadata:
      labels:
        app: tf-serving-clothing-model
    spec:
      containers:
      - name: tf-serving-clothing-model
        image: zoomcamp-10-model:xception-v4-001  # Model image name
        resources:
          limits:
            memory: "512Mi"  # Adding more RAM may improve performance 🚀
            cpu: "0.5"  # Half CPU core ⚙️
        ports:
        - containerPort: 8500  # Port where TF-Serving listens for gRPC requests 🎯
```

Make the model image available by running:
```bash
kind load docker-image zoomcamp-10-model:xception-v4-001
```

Apply the configuration to the cluster with:
```bash
kubectl apply -f model-deployment.yaml
```

To remove a deployment, use:
```bash
kubectl delete -f model-deployment-file
```

##### 🧪 Testing the TF-Serving Model
To test the TF-Serving clothing model, port-forward the pod:
```bash
kubectl port-forward tf-serving-clothing-model-pod-name 8500:8500
```

Modify the gateway application by uncommenting the hardcoded URL and prediction logic to test the model. ⚡

### 📡 Model Service Configuration
Define a service configuration file for the model:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: tf-serving-clothing-model
spec:
  selector:
    app: tf-serving-clothing-model
  ports:
  - port: 8500
    targetPort: 8500
```

Apply the changes with:
```bash
kubectl apply -f model-service.yaml
```

Test the service by port-forwarding it:
```bash
kubectl port-forward service/tf-serving-clothing-model 8500:8500
```

Then, send requests through the gateway. 🌐

**Note:** ⚠️ Minor negligible errors may occur because gRPC is used instead of HTTP. 

### 🌐 Gateway Deployment
Create a deployment configuration file for the gateway:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: gateway
spec:
  selector:
    matchLabels:
      app: gateway
  template:
    metadata:
      labels:
        app: gateway
    spec:
      containers:
      - name: gateway
        image: zoomcamp-10-gateway:002  # Gateway image name
        resources:
          limits:
            memory: "128Mi"  # Memory limit 🧠
            cpu: "100m"  # Minimal CPU usage ⚙️
        ports:
        - containerPort: 9696  # Port for gateway requests 🎯
        env:
        - name: TF_SERVING_HOST  # Environment variable for model URL 🌍
          value: tf-serving-clothing-model.default.svc.cluster.local:8500  # Kubernetes convention for service URL
```

To verify the deployment, log into one of the pods (e.g., ping deployment pod) to send request from the ping container to itself:
```bash
kubectl exec -it ping-deployment-pod-name -- bash
```

Test the service by running:
```bash
curl localhost:9696/ping
```

If `curl` is not found, install it:
```bash
apt update && apt upgrade
apt install curl
```

Re-run the test:
```bash
curl localhost:9696/ping  # Should return 'PONG' 🏓
```

Now, send a request from the container to the service:
```bash
curl ping.default.svc.cluster.local/ping
```

To test communication with the TF-Serving model, we try:
```bash
curl tf-serving-clothing-model.default.svc.cluster.local:8500
```
As the tf-serving application doesn't want to deal with sending `http requests`, we get an error: `not allowed`. Since HTTP requests are not allowed by the TF-Serving application, use `telnet` (a very low-level library allowing to connect to any port and send something to it) to test connectivity:
```bash
apt install telnet
```

Run the command to verify that we can reach this service:
```bash
telnet tf-serving-clothing-model.default.svc.cluster.local:8500
```

Apply the gateway configuration:
```bash
kubectl apply -f gateway-deployment.yaml
```

Port-forward the gateway pod for testing:
```bash
kubectl port-forward gateway-pod-name 9696:9696
```

Run the [test script](code/zoomcamp/test.py) from another terminal to verify functionality. ✅

### 📡 Gateway Service Configuration
Define a service configuration file for the gateway:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: gateway
spec:
  selector:
    app: gateway
  ports:
  - port: 80  # Service port 🌐
    targetPort: 9696  # Target port on container 🎯
```

Apply the changes:
```bash
kubectl apply -f gateway-service.yaml
```

Check running services:
```bash
kubectl get service
```

To change the service type to `LoadBalancer`:
1. Update the configuration file.
2. Reapply the changes.

For testing, port-forward the service:
```bash
kubectl port-forward service/gateway 8080:80
```

Run the [new test script](code/zoomcamp/test_service.py) to verify the setup. 🧪

**Note:** `gRPC` is not the same as traditional `HTTP`. This distinction can lead to issues with load balancing (the process of routing requests to pods managed by a service) when deploying `gRPC` applications on Kubernetes. Specifically, when multiple pods are created, they may not receive an equal distribution of requests.

For more details on addressing load balancing challenges in production, refer to the following article: [gRPC Load Balancing on Kubernetes Without Tears](https://kubernetes.io/blog/2018/11/07/grpc-load-balancing-on-kubernetes-without-tears/).

---

## 10.8 🚀 Deploying to EKS

Deploying our application (gateway and model) locally using `kind` is great for experiments, but for cloud deployment, AWS `Elastic Kubernetes Service` (EKS) 🌐 provides a powerful solution. We'll create an EKS cluster using [`eksctl`](https://eksctl.io/installation/) ⚙️, avoiding the need for manual setup via the AWS web interface.

🔧 **Prerequisites:** Ensure that AWS CLI and Kubectl are installed by following [this guide](https://docs.aws.amazon.com/eks/latest/userguide/setting-up.html). Now let's install `eksctl`:

- 📂 Navigate to the bin directory: `cd ~/bin`
- 📥 Download and extract `eksctl`:
```bash
# for ARM systems, set ARCH to: `arm64`, `armv6` or `armv7`
ARCH=amd64 # set our architecture
PLATFORM=$(uname -s)_$ARCH # identify our system platform
curl -sLO "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_$PLATFORM.tar.gz" # download the package
tar -xzf eksctl_$PLATFORM.tar.gz && rm eksctl_$PLATFORM.tar.gz # unpack and remove the tar file
```

🔐 **IAM Access:** Ensure your IAM user has the necessary permissions for [EKS actions](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelastickubernetesservice.html) and [service manipulations](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html).

### 🚧 Creating the Cluster
Return to your working directory. Create a cluster using the command:
```bash
eksctl create cluster --name cluster-name
```
Or, define the cluster using a configuration file (eks-config.yaml):
```yaml
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: mlzoomcamp-eks
  region: us-east-1

nodeGroups: # similar to deployments
  - name: ng-m5-xlarge 
    instanceType: m5.xlarge # 4 CPUs and 16 GB of memory 🖥️
    desiredCapacity: 1 # 1 machine of this type
```
and use it to create the cluster:
```bash
# Create the cluster with a configuration file
eksctl create cluster -f eks-config.yaml
```

🗑️ To delete a cluster: `eksctl delete cluster --name cluster-name`. 

⏳ While waiting for the cluster creation, we need to publish our local images to ECR (AWS Container Registry) 📦 as they need to be available if we want to use them:
`aws ecr create-repository --repository-name mlzoomcamp-images`. We copy the repository URI furnished by this command, and then set the image addresses with the following code:

```bash
# Get the prefix address
ACCOUNT_ID=387546586013
REGION=us-east-1
REGISTRY_NAME=mlzoomcamp-images
PREFIX=${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${REGISTRY_NAME}

# Set gateway address and tag it
GATEWAY_LOCAL=zoomcamp-10-gateway:002
GATEWAY_REMOTE=${PREFIX}:zoomcamp-10-gateway-002
docker tag ${GATEWAY_LOCAL} ${GATEWAY_REMOTE}

# Set model address and tag it
MODEL_LOCAL=zoomcamp-10-model:xception-v4-001
MODEL_REMOTE=${PREFIX}:zoomcamp-10-model-xception-v4-001
docker tag ${MODEL_LOCAL} ${MODEL_REMOTE}
```

🔑 Now we can log in to ECR and push the model and the gateway:
```bash
# Login to ECR
$(aws ecr get-login --no-include-email) # there are more secure ways to login

# Push model and gateway
docker push ${MODEL_REMOTE}
docker push ${GATEWAY_REMOTE}
```

 🔄 Replace the local image names in the deployment files with thiose from ECR:
 ```bash
 # Output the new image names 
echo ${MODEL_REMOTE}  # for model-deployment
echo ${GATEWAY_REMOTE}  # for gateway-deployment
```

### 🛠️ Deploying to EKS
Once the cluster is ready, verify the nodes:
```bash
kubectl get nodes
```
⏱️ With `docker ps` we still get the ones created with `kind`.

Now let's apply the model configuration files to our cluster:
```bash
# Apply model configuration files
kubectl apply -f model-deployment.yaml # deployment
kubectl apply -f model-service.yaml # service

# Check if the service is ready
kubectl get pod # checking pods
kubectl get service # checking the service
```
We can do port-forwarding for the tf-serving service: `kubectl port-forward service/tf-serving-clothing-model 8500:8500` and test it using our gateway (note that changes should be made to this file by uncommenting and commenting some code for the gateway script to become just a test file).

Apply the gateway configuration files to our cluster:
```bash
# Apply gateway configuration files
kubectl apply -f gateway-deployment.yaml # deployment
kubectl apply -f gateway-service.yaml # service

# Check if the gateway is ready
kubectl get pod # checking pods
kubectl get service # checking the service
```

🌐 **Accessing the Gateway:**
This time we have a URL address at the External-IP information for our service. 

🔌 With port-forwarding, we can test that the service works:
```bash
# Port forwarding
kubectl port-forward service/gateway 8080:80
# Test
python test
```
To verify service status by checking the external connection we use: `telnet External-IP-address`.

🧪 **Testing:**
Once the service is up, test it with our [new script file](code/zoomcamp/test_eks.py):
```bash
python test_eks.py
```
You can monitor your cluster in the AWS console.

>>> ⚠️ **Important Note:** EKS is not part of the AWS free tier. The cluster's DNS name allows public access, so implement security measures to restrict unauthorized access.

🛑 To stop the cluster, we can delete it:
```bash
eksctl delete cluster --name mlzoomcamp-eks
```
especially as it costs money.

---

# 🎯 **Key Takeaways**  

We designed an architecture with two components:   
1. **TF-Serving Component** – Uses TensorFlow Serving to handle inference.  
2. **Gateway Component** – Acts as our serving layer, gathering user input (HTTP image links) and communicating with gRPC used by our model.  

🔹 **Why Two Components?**  
Having separate components allows for efficient resource management (CPU, GPU) and better scaling flexibility.  

💡 **Running Components Together**  
`docker-compose` was essential for running both components seamlessly.  

🚀 **Deploying Kubernetes Locally**  
`kind` is a fantastic tool for deploying Kubernetes clusters locally. Other great options include: `k3d`, `minikube`, `k3s`, `microk8s`, `EKS Anywhere`, etc. 

🌐 **Additional Tools to Explore**  
- [`Rancher Desktop`](https://rancherdesktop.io/) – Similar to Docker Desktop but integrates Kubernetes.  
- [`LENS`](https://k8slens.dev/) – A powerful IDE for managing and monitoring Kubernetes clusters.  

☁️ **Cloud Providers for Kubernetes**  
- **AWS** – `EKS cluster` allows Kubernetes deployments but isn't free.  
- **Other Providers** – GCP, Azure, and DigitalOcean offer managed Kubernetes services.  

⚙️ **Cross-Platform Configurations**  
The configuration files created are universal and can work on any Kubernetes cluster. Just update the image names as needed.  

📦 **Namespaces for Organization**  
Kubernetes namespaces are helpful for structuring your applications (the default namespace is `default`).  

### 🔑 **Quick Points**  
- **TF-Serving** – A system to deploy TensorFlow models.  
- **Pre-processing** – Required alongside TF-Serving for complete pipelines.  
- **Kubernetes** – Orchestrates and manages containers.  
- **Deployments & Services** – Essential for deploying on Kubernetes.  
- **Local Testing** – Use Docker Compose and `kind` for local development and testing.  
   
---