![ML Zoomcamp Illustration](https://github.com/maxim-eyengue/Python-Codes/blob/main/ML_Zoomcamp_2024/zoomcamp.jpg)
---

## 📚 Session 5 Summary - Machine Learning Zoomcamp

### 1. 🗺️ **Project Overview: Deploying a Churn Prediction Model** 

The goal of this session is to learn how to **deploy machine learning (ML) models**,
specifically a **churn prediction model**.

The project includes the following steps:
* Training a churn prediction model.
* Saving the model to a file.
* Loading this file from a separate web service (churn service).

Two services are involved: a **churn service**, which hosts the churn prediction model, 
and a **marketing service**, which contains user information and needs to query the churn service. 
The marketing service sends requests to the churn service to predict whether a user will churn, 
and uses this information to decide whether to send a promotional offer.

This session focuses on:
* Training the model.
* Saving the model.
* Loading the model using a web service.
* Interacting with this service.

### 2. 💻 **Saving and Loading the Model**

After training, the ML model resides in the Jupyter notebook. To use the model in a web service,
it needs to be saved to a file. This can be done using the **`pickle`** library in Python. 

The process involves:
* Creating a file and specifying that it will store bytes.
* Saving the model and the one-hot encoder to the file.
* Closing the file. 

To verify that the file has been saved, the kernel can be restarted, the file opened,
the model loaded, and predictions can be made.

To create a script that trains a model instead of running individual Python cells in a Jupyter notebook,
you can download the notebook as a Python file (an executable script).
It is recommended to place parameters at the top of the file for easy modification.
These parameters can also be configured via the command line interface.
An additional Python script can be created for generating predictions.

To view the content of a text file:
* Use the Linux command: `less file_name.ext`.
* Use the Windows command: `type file_name.ext | more`.

To run the training script, use the command `python train.py`. To confirm that the model was saved in the
current directory, use the command `ls` which list files. JupyterLab is well-suited for carrying out these
tasks.

### 3. 🌐 **Web Services Introduction**

**Flask** is a Python framework for building web services. 

The project aims to integrate the churn prediction model into a **churn service** that interacts with
a **marketing service**. Communication between these services involves sending requests and receiving
responses.

A web service is a service accessed over a network using protocols like TCP/IP. Flask can be used to
implement a web service. It handles internal complexities, simplifying communication with the web service. 

To use Python code directly in the terminal, use **`ipython`**. Install the Flask framework using
**`pip install flask`**.

A decorator adds functionality to a function, for instance, turning it into a web service. 
Here is an example of a decorator in Flask:

```python
@app.route("/ping", methods = ["GET"])
```

* **`route`**: Specifies the address where the function will reside (e.g., "/ping").
* **`methods`**: Defines how to access the address.
* **`GET`**: Requests data from a source.
* **`POST`**: Sends data to a server to create or update a resource.

To run the application in debug mode on the localhost:

```python
app.run(debug = True, host = '0.0.0.0', port = 9696)
```

The application should be run within the **`__main__`** method, which represents the top-level script
environment. To run the Python script that launches the app, use the command **`python ping.py`**. 

To send a request after opening a new terminal:

* Type the following address in a web browser: `http://localhost:9696/ping`.
* Use **`curl`** in a new terminal: `curl http://localhost:9696/ping` or `curl http://127.0.0.1:9696/ping`.

Attempts to access the app are tracked in the server terminal.

### 4. 📊 **Serving the Churn Model with Flask**

The goal is to convert the prediction script into a churn service. The marketing service should be able
to send customer information to the churn service and receive the churn probability as a response.
This is achieved by creating a **`predict`** method at the address **/predict**.

Information is exchanged in JSON format. Flask requires using the **`request`** utility to format
the input and **`jsonify`** to format the output. **`request.get_json()`** converts the request body
into a Python dictionary.

Sending requests directly from the browser, as done with `ping`, is not permitted for the `predict` method.
Instead, requests are sent using Python and the **`requests`** library.

The development server is not suitable for production deployments. A production WSGI server should be used
instead.

Instead of using Flask directly, **WSGI** (Web Server Gateway Interface) should be employed for production. 

Examples of production WSGI servers:
* **`gunicorn`** (for macOS and Linux): Installed using `pip install gunicorn`.
* **`waitress`** (for Windows): Installed using `pip install waitress`.

To use **`gunicorn`**:

```bash
gunicorn --bind 0.0.0.0:9696 predict:app
```

* **`predict`**: Refers to the Python file `predict.py`.
* **`app`**: The variable used to define the Flask app.

To use **`waitress`**:

```bash
waitress-serve --listen=127.0.0.1:9696 predict:app 
```

You can then write a script to retrieve the churn probability as a response and run it with:
`python predict_test.py`.

### 5. 📦 **Dependencies and Environment**

**Virtual environments** are essential for managing dependencies in Python projects.

To install scikit-learn using pip:
```bash
pip install scikit-learn
``` 

On Anaconda, this uses the `pip` from the `$PATH`, which typically points to `~/anaconda3/bin/pip`.
This `pip` interacts with **`pypi.org`** (the Python Package Index), retrieves scikit-learn
(the latest version if no specific version is specified), and installs it using a package format
like `.wheel`. 

To install a particular version, add `== version` to the `pip` command.

If two services require different versions of the same package, you need to ensure compatibility and that
both services can run without issues. To prevent conflicts, place these services in separate,
isolated environments. This practice, known as **virtual environments**, allows each service to manage
its dependencies independently, avoiding conflicts.

Common tools for managing virtual environments:
* **virtualenv**: `/venv`
* **conda**
* **pipenv**: Officially recommended by the Python community.
* **poetry**

To install libraries using **`pipenv`**:
```bash
pipenv install numpy scikit-learn==1.4.2 flask
```

This command creates two files: `Pipfile` and `Pipfile.lock`.

The **`Pipfile`** contains:
* **source**:  The package source, typically PyPI.
* **packages**:  The required packages and their versions (if specified).
* **dev-packages**: Packages needed for development.
* **requires**: The Python version.

You also need to install **`gunicorn`** if using it as the WSGI server.

Anyone can clone the project folder from a GitHub repository and use **`pipenv install`** to set up
the correct environment.

The **`Pipfile.lock`** is a comprehensive JSON file containing the precise versions of all installed
dependencies along with their checksums. This ensures that the exact same versions are used on other
machines, guaranteeing reproducibility. This is particularly critical because libraries are frequently
updated.

To activate the environment and ensure that the specified dependencies are used, run **`pipenv shell`**.
This command also displays the path to the environment.

In this environment, you can execute commands like **`gunicorn --bind 0.0.0.0:9696 predict:app`**.

Instead of typing **`pipenv shell`** followed by the desired command, you can use **`pipenv run`**
directly:

```bash
pipenv run gunicorn --bind 0.0.0.0:9696 predict:app
```

For services requiring specific versions of system dependencies outside of Python,
such as `apt-get install libgomp`, virtual environments are insufficient.
Docker offers an additional level of isolation.

### 6. 🐳 **Environment Management: Docker**

Docker provides isolation for the entire application from the host machine's resources.

Consider a laptop running Ubuntu with two virtual environments: a churn service and a lead scoring service.
Each environment has specific dependencies that might conflict. Instead of using virtual environments,
you can place each service within a **container**. This ensures complete isolation.

With Docker, the churn service can run on Ubuntu 18.04, the lead scoring service on Ubuntu 20.04,
and another service (e.g., email) on Perl and Amazon Linux. Each container can have different Python
versions and libraries. All of this resides on a host machine (e.g., Ubuntu or macOS).
The host can accommodate numerous containers with varying operating systems and dependencies.

A key benefit of Docker is portability. You can take the churn service container and deploy it to the cloud.

The following command runs a specific Python version in a Docker container:

```bash
docker run -it --rm python:3.8.12-slim
```

* **`-it`**: Provides access to the container's terminal.
* **`--rm`**: Removes the image after the session ends. 

Use **CTRL+D** to exit the Docker image.

To access a Docker image's terminal and make changes, you can overwrite the **entrypoint** (the default
command executed with **`docker run`**).

```bash
docker run -it --rm --entrypoint=bash python:3.8.12-slim
```

This command opens a Linux terminal. To update the packages in the container, use **`apt-get update`**. 
You can then install additional tools like **`wget`** using **`apt-get install wget`**.

Changes made within the container, such as creating directories, are isolated and do not affect the host.

To define how to build a Docker image, you create a **Dockerfile**. Here's an example 
(note that comments should be removed):

```dockerfile
FROM python:3.11.10-slim # Base image
RUN pip install pipenv # Install pipenv
WORKDIR /app # Set working directory
COPY ["Pipfile", "Pipfile.lock", "./"] # Copy dependency files
RUN pipenv install --system --deploy # Install dependencies
COPY ["predict.py", "./"] # Copy the prediction script
COPY ["model.pkl", "./"] # Copy the model file
EXPOSE 9696 # Expose the port
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"] # Start gunicorn
```

To build the Docker image:
```bash
docker build -t zoomcamp-test . 
```

* **`-t`**: Specifies the image name (`zoomcamp-test` in this case).
* **`.`**: Indicates that the Dockerfile in the current directory should be used.

Run the Docker image using:

```bash
docker run -it --rm zoomcamp-test 
```

In Docker, you generally install libraries directly into the container's environment rather than creating
a separate virtual environment. The `--system` and `--deploy` flags in the `pipenv install` command in the
Dockerfile are used to install dependencies system-wide (skipping environment creation).

The Dockerfile also copies the `predict.py` file and the trained model (`model.pkl`) into the image. After
building the image, you run it and launch the app using **`gunicorn --bind=0.0.0.0:9696 predict:app`**.

To allow other services to access the port within the Docker container, you need to **expose** it using
**port mapping**.

The `EXPOSE 9696` instruction in the Dockerfile declares that port 9696 should be exposed.

To map the port on your machine to the port in the Docker container, requires the `-p` flag when running the
container. For example:
```bash
docker run -it --rm -p 9696:9696 zoomcamp-test
```

This maps port 9696 on the host machine to port 9696 in the container.

The Dockerfile also specifies the `gunicorn` command as the entrypoint, which means it will be executed
automatically when the container starts.

### 7. ☁️ **Deployment to the Cloud: AWS Elastic Beanstalk**

After learning how to run the service locally, the next step is to deploy it to the cloud. **AWS**
(Amazon Web Services) is a popular cloud provider, and **Elastic Beanstalk** (EB) simplifies deployment
with a few commands.

The churn service, packaged in a Docker container, can be deployed to the cloud using AWS EB. Requests
from the marketing service are routed through EB to the container, and responses are sent back through
the same path. If the churn service experiences increased traffic, EB automatically scales horizontally
(**scaling out**), adding more instances to handle the load without disruption. EB can also automatically
**scale down** to the original state when traffic decreases.

To install the **`awsebcli`** tool (AWS Elastic Beanstalk command-line interface) specifically for
the churn prediction project, use:

```bash
pipenv install awsebcli --dev
```

This command installs `awsebcli` as a development dependency, which is needed for development but not
within the container itself.

To initialize the directory with the EB client:
```bash
eb init -p docker -r eu-north-1 churn-serving
```

* **`-p docker`**: Specifies the platform as Docker.
* **`-r eu-north-1`**:  Sets the region to `eu-north-1`.
* **`churn-serving`**:  The name of the environment.

To view the configuration information in the `.elasticbeanstalk/config.yml` file,
use **`less .elasticbeanstalk/config.yml`**.

To test the application locally before deploying to the cloud:
```bash
eb local run --port 9696
```

You can then test it using the `predict.py` script in your terminal.

To deploy to the cloud:
```bash
eb create churn-serving-env
``` 

This command creates an environment. EB sets up a load balancer for scaling.

After deployment, you will receive the address where the application is accessible.
Update the local address in your `predict-test` script to the host address, omitting the port.

The deployed service is publicly accessible. In real-world scenarios, you would typically restrict
access to specific networks for security.

To terminate the service:

```bash
eb terminate churn-serving-env 
```

### 8. 🔑 **Key Takeaways**

* **Model Training and Saving:** The churn prediction model was trained and saved to a pickle file using
a Python script.
* **Flask Service:** The model was integrated into a Flask service.
* **Model Deployment:** The importance of model deployment was highlighted, as models are only useful
if other services can access them.
* **Environments and Docker:** The use of environments and Docker for isolating services and deploying
containers containing models and their environments was explained.
* **Elastic Beanstalk:** Docker containers were deployed both locally and to the cloud using
Elastic Beanstalk.
---
