![ML Zoomcamp Illustration](https://github.com/maxim-eyengue/Python-Codes/blob/main/ML_Zoomcamp_2024/zoomcamp.jpg)
---


## 📚 Session 8 Summary - Machine Learning Zoomcamp


### Fashion Classification:

In the previous session we talked about tabular data,
and used models for this purpose: linear and logistic
regression and tree-based models. In this session
we will look at images data for a multi-class classification project. For that we will use neural networks. The idea is to build a fashion classification service where a user can post an image, so to get its category in return (e.g T-shirts). The dataset used is a subset of the clothing-dataset with its 10 most popular classes. In the train dataset, there are 10 different folders, each named by a category, and containing the corresponding images. No need to do tran-tes-validation, as the dataset has alredy been splitted.

In this lesson, we'll be more practical. Check the following link to know more about how neural networks function : https://cs231n.github.io/.

Note that we will use `tensorflow` and `keras` for training models. `tensorflow` is a framework for deep learning models.
We will learn about how to use models already trained. We will get an overview of some theory and then talk about transfer learning (getting a model previously trained, fien-tune it to solve a particular problem), parameters and generalization and data augmentation.

#### Setting up the environment on Saturn Cloud
Login on Saturn Cloud and create a secret key to push notebooks to github with ssh. For that you should already have generated an ssh key on your laptop with your GitHub account. 
Check [Tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).
And then add the public ssh key when required after [creating a resource](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/08-deep-learning/01b-saturn-cloud.md).  
You can then launch the environment and make sure tensorflow has been installed by checking its version.


### Tensorflow and Keras
`tensorflow` is a library for doing deep learning (its main focus) And
`keras` is a library providing the higher level abstaction on the top of `tensorflow` which
makes it simpler to create, train and use neural networks.
We can install it with:
`!conda install tensorflow -y` (as we are using `anaconda`)
or with the classic: `!pip install tensorflow`. 
Note that if you have a GPU, on your local computer, installing it
is a bit more complex, as it would then require additional setup to integrate `tensorflow`.
Note that `keras` used to be a separate library from `tensorflow` but was include
in more recent verions of both frameworks (from `tensorflow 2.0`).

We used the function `load_img` from `tensorflow.keras.preprocessing.image` (or from `tensorflow.keras.utils` if any errors) 
to load an image and converted it to an array with `np.array()`. Note that it is important to resize
the images when loading them because neural networks usually expect images with a certain size:
$299 * 299$ or $224 * 224$ or $150 * 150$.
Each image is represented internally as an array with three channels:
one red, one green and one blue. For each of this channel, we have an array
containing numbers (bytes) whose values are between 0 and 255. Images is made of pixels.
Each pixel on the original image is represented by a combination of the pixels at the same
position of these three channels. It has a shape of three dimension:  (height, width, color channels)
Image : (150, 150)
Array: (150, 150, 3)
When obtaining the representation of an image as a `numpy.array`:
`[179, 171,  99]` is a pixel with `RGB` values 
(`179`--> `R`, `171`--> `G`, `99`--> `B`).
The type of tis `numpy.array` is `uint8`, with `u` for `unsigned`
as pixel values go from `0` to `255`, and `int8` as it is an `integer` that
takes 8 bits or 1 byte. Simply said, A typical color image consists of three color channels: red, green and blue. 
Each color channel has 8 bits or 1 byte and can represent distinct values between 0-256 (uint8 type).


### Pre-Trained Convolutional Neural Networks
Pre-trained models have already been trained, generally on larger
datasets.

* Imagenet dataset: https://www.image-net.org/
It has $1,281,167$ training images, $50,000$ validation ones, and $100,000$ for test. It is a
dataset for general purpose image classificattion.
* Pre-trained models: https://keras.io/api/applications/
 They were trained on Imagenet to get a good general understanding of images. We will use
 `Xception` as it is quite small compared to others (`88 MB` and $22,910,480$ parameters),
 and so, quite fast with a good accuracy.
We can use `Sage Maker` or `Saturn Cloud` to get a `GPU` so to run things faster, instead of using
the `CPU` of our local computer which can be $8$ times slower. `GPU` are quite good at parralelizing things,
fast when performing matrix multiplications, that is necessary for neural networks.
We can for example use as kernel `tensorflow2_p36` when using `Sage Maker`.
Note that as we are using `Xception` we will have to use corresponding functions `preprocess_input` and `decode_predictions`
to respectively preprocess an input batch of images to the model, and get classes with corresponding probabilities for each
prediction.

Ps: ImageNet can be used for general image classification but wjhen it comes to clothes. There are classes
it doesn't have, such as *t-shirt*. That is why we can use a pre-trained model, build on top of it so it get
adapted to our particular case of clothing.

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
