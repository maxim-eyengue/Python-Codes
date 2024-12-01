![ML Zoomcamp Illustration](https://github.com/maxim-eyengue/Python-Codes/blob/main/ML_Zoomcamp_2024/zoomcamp.jpg)
---


## 📚 Session 8 Summary - Machine Learning Zoomcamp

### Fashion Classification

In the previous session, we discussed tabular data and explored models such as linear and logistic regression, along with tree-based models. In this session, we'll shift our focus to image data for a multi-class classification project, leveraging neural networks. Specifically, we will build a fashion classification service that allows users to upload an image and receive its category in return (e.g., T-shirts). The dataset we'll use is a subset of the clothing dataset, featuring its 10 most popular classes. The training dataset is organized into 10 folders, each named after a category and containing the corresponding images. Since the dataset has already been split, no need to perform train-test-validation splits.

This lesson is focused on practical implementation. For a deeper understanding of how neural networks function, refer to this [tutorial](https://cs231n.github.io/).

We will be using `TensorFlow` and `Keras` for training the models. `TensorFlow` is a popular deep learning framework that facilitates the development of neural network models. In this session, we will cover using pre-trained models, an overview of neural network theory, and introduce key concepts like transfer learning (where we fine-tune pre-trained models to solve specific problems), parameters, generalization, and data augmentation.

#### Setting up the Environment on Saturn Cloud

1. Log in to Saturn Cloud and create a secret key to push notebooks to GitHub using SSH. If you haven't already, generate an SSH key on your laptop associated with your GitHub account. Follow this [tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).
2. After creating a resource, add your public SSH key when prompted, following the steps outlined [here](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/08-deep-learning/01b-saturn-cloud.md).
3. Once the environment is set up, ensure that `TensorFlow` is installed by importing it and checking its version.

---

### TensorFlow and Keras Overview

**TensorFlow** is a powerful library primarily designed for deep learning and machine learning tasks. It provides the foundation for building and training complex neural networks. On top of this, **Keras** acts as a high-level API that simplifies the process of creating, training, and deploying neural networks, making TensorFlow more accessible.

##### Installation
To install TensorFlow, you can use either of the following commands, depending on your package manager:
- Using Anaconda:  
  ```bash
  !conda install tensorflow -y
  ```
- Using pip:  
  ```bash
  !pip install tensorflow
  ```

**Note:**  
If you have a GPU and wish to utilize it for accelerated training, additional setup is required to install the appropriate CUDA and cuDNN libraries to integrate TensorFlow with your GPU.

##### Keras in TensorFlow
Previously, Keras was an independent library. Since TensorFlow 2.0, Keras has been integrated into TensorFlow as its default high-level API, allowing seamless usage.


#### Working with Images in TensorFlow

##### Loading and Preprocessing Images
To load an image, the `load_img` function from `tensorflow.keras.preprocessing.image` or `tensorflow.keras.utils` can be used. Images must often be resized to specific dimensions required by neural networks, such as \( 299 \times 299 \), \( 224 \times 224 \), or \( 150 \times 150 \). Resizing ensures the input matches the network's expected format.

After loading an image, you can convert it into a NumPy array using `np.array()`.

##### Understanding Image Representation
Images are typically represented as a 3D array with the following dimensions:
- **Height** (number of pixels vertically)
- **Width** (number of pixels horizontally)
- **Color Channels** (Red, Green, Blue or RGB)

Example:
- An image with a size of \( 150 \times 150 \) would have an array representation with a shape of `(150, 150, 3)`.

For each pixel, the RGB values are stored in the range of `0` to `255`, where:
- **R** (Red) = Intensity of the red channel
- **G** (Green) = Intensity of the green channel
- **B** (Blue) = Intensity of the blue channel

##### Example
A single pixel with the RGB values `[179, 171, 99]` would mean:
- \( R = 179 \)  
- \( G = 171 \)  
- \( B = 99 \)  

##### Data Type
The pixel values are stored in a `numpy.array` of type `uint8` (unsigned 8-bit integer). This data type is ideal for pixel representation since:
- Each pixel value ranges from `0` to `255` (1 byte or 8 bits per color channel).
- Unsigned integers are used because negative pixel values are not meaningful.

In summary, a typical color image has three channels (RGB), each with an 8-bit representation. Combined, this structure ensures precise color representation for every pixel. This standardized format simplifies how neural networks process and analyze image data.

---

### Pre-Trained Convolutional Neural Networks

#### **Pre-trained Models**
Pre-trained models are neural networks that have been trained on large datasets to recognize and classify images. They serve as a robust foundation for various computer vision tasks by providing a general understanding of visual features.

#### **ImageNet Dataset**
- **Source**: [ImageNet Dataset](https://www.image-net.org/)
- **Overview**:  
  - **Training Set**: 1,281,167 images  
  - **Validation Set**: 50,000 images  
  - **Test Set**: 100,000 images  
- **Purpose**: General-purpose image classification.

#### **Models Trained on ImageNet**
- Pre-trained models available via [Keras Applications](https://keras.io/api/applications/) are trained on the ImageNet dataset.
- We focus on the **Xception** model due to its balance of:
  - Size: 88 MB.
  - Parameters: 22,910,480.
  - Performance: High accuracy.
  - Speed: Efficient computation, ideal for setups with limited resources.

#### **Accelerating Training and Inference**
- **GPU Usage**:
  - **Advantages**: 
    - Parallel processing capabilities.
    - Superior performance in matrix operations crucial for neural networks.
  - **Tools**:
    - **SageMaker** or **Saturn Cloud** for cloud-based GPU access.
    - Use kernel `tensorflow2_p36` when leveraging SageMaker.

- **CPU vs. GPU**:
  - GPUs can be up to 8x faster than CPUs for training and inference tasks.

#### **Functions Specific to Xception**
- **`preprocess_input`**: Prepares batches of images for Xception by normalizing and scaling input.
- **`decode_predictions`**: Translates model outputs into human-readable class names with associated probabilities.

#### **Customizing Pre-Trained Models**
- While ImageNet-trained models are excellent for general image classification, they may lack specificity for certain domains, such as clothing, where classes like *t-shirt* may not exist.
- **Solution**:
  - Build on top of pre-trained models by fine-tuning or transferring learning to adapt to specific datasets, enabling better performance for specialized tasks like clothing classification.

---

### CNNs



### Transfer Learning


### Adjusting the learning rate
    

### Checkpointing


### Adding more Layers


### Regularization and Dropout


### Data Augmentation


### Training a Larger Model


### Using the Model



## **💡 Key Takeaways**
