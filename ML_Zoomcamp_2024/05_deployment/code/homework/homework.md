## Session 05  Homework

For this homework, we will work under the ml-zoomcamp environment running with Python 3.11.10. All our work is stored in a folder named `homework`.

## Question 1

First, we can install `Pipenv` using the command `pip install pipenv`. The version of pipenv installed (`pipenv, version 2024.2.0`) is given by `pipenv --version`.


## Question 2

Using Pipenv, we install Scikit-Learn version 1.5.2 with the command: `pipenv install scikit-learn==1.5.2`. The first hash for scikit-learn that we get in Pipfile.lock is: `"sha256:03b6158efa3faaf1feea3faa884c840ebd61b6484167c711548fce208ea09445"`.


## Models

A dictionary vectorizer and a model have been prepared, and trained (roughly) using this code:

```python
features = ['job', 'duration', 'poutcome']
dicts = df[features].to_dict(orient = 'records')

dv = DictVectorizer(sparse = False)
X = dv.fit_transform(dicts)

model = LogisticRegression().fit(X, y)
```
and then saved with Pickle. We will download them:

* [DictVectorizer](https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/cohorts/2024/05-deployment/homework/dv.bin?raw=true)
* [LogisticRegression](https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/cohorts/2024/05-deployment/homework/model1.bin?raw=true)

With `wget`:

```bash
PREFIX=https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/master/cohorts/2024/05-deployment/homework
wget $PREFIX/model1.bin
wget $PREFIX/dv.bin
```


## Question 3

Let's use these models!

We will write a script for loading these models with pickle and score the following client:

```json
{"job": "management", "duration": 400, "poutcome": "success"}
```

The probability that this client will get a subscription is `0.759`.


## Question 4

Now let's serve this model as a web service. We install Flask and gunicorn using `pip install`. We then write the Flask code for serving the model and score the following client using the library `requests`:

```python
url = "http://localhost:9696/q4_predict"
client = {"job": "student", "duration": 280, "poutcome": "failure"}
requests.post(url, json = client).json()
```

The probability that this client will get a subscription is `0.335`.


## Docker

We installed [Docker](https://andrewlock.net/installing-docker-desktop-for-windows/) for the next two questions.

For these questions, a base image: `svizor/zoomcamp-model:3.11.5-slim` was prepared. We need to use it (see Question 5 for an example).

This image is based on `python:3.11.5-slim` and has a logistic regression model 
(a different one) as well as a dictionary vectorizer inside. 

This is how the Dockerfile for this image looks like:

```docker 
FROM python:3.11.5-slim
WORKDIR /app
COPY ["model2.bin", "dv.bin", "./"]
```

It has already been built and pushed to [`svizor/zoomcamp-model:3.11.5-slim`](https://hub.docker.com/r/svizor/zoomcamp-model). So, we don't need to build this docker image anymore, it's just for your reference.


## Question 5

Let's download the base image `svizor/zoomcamp-model:3.11.5-slim`. We can easily make it by using [docker pull](https://docs.docker.com/engine/reference/commandline/pull/) command: `docker pull svizor/zoomcamp-model:3.11.5-slim`.

The size of this base image is `130 MB`. We got it in the "SIZE" column by running `docker images`.


## Dockerfile

Now, we can create our own Dockerfile based on the prepared image, installing all the dependencies from the Pipenv file, copying our Flask script, and running it with gunicorn.

After adding comments to the content of this file, we obtain:

```docker
# Specify the image file used
FROM svizor/zoomcamp-model:3.11.5-slim

# Install all the dependencies from the Pipenv file
RUN pip install pipenv

# Create a directory that doesn't exist and opens it
WORKDIR /app

# Copy files, from which we want to install libraries, to the current directory
COPY ["Pipfile", "Pipfile.lock", "./"]

# Skip creating a virtual environment
RUN pipenv install --system --deploy

# Copy our Flask script
COPY ["q6_predict.py", "./"]

# Expose the port for mapping it later
EXPOSE 9696

# Run it with Gunicorn as entrypoint
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "q6_predict:app"]
```
Note that the dockerfile should not contain comments.

Let's build our docker image with: `docker build -t maxim-zoomcamp-homework .`


## Question 6

Let's run our docker container with `docker run -it --rm -p 9696:9696 maxim-zoomcamp-homework`!

After running it, we can score the following customer:

```python
url = "http://localhost:9696/q6_predict"
client = {"job": "management", "duration": 400, "poutcome": "success"}
requests.post(url, json = client).json()
```

The probability that this client will get a subscription now is `0.757`.
