![ML Zoomcamp Illustration](https://github.com/maxim-eyengue/Python-Codes/blob/main/ML_Zoomcamp_2024/zoomcamp.jpg)
## 📚 Summary of First Session - Machine Learning Zoomcamp

### 1. **🚗 Introduction to Machine Learning with Cars Data**  
   We start with data about cars, including characteristics (features) and prices (target). A Machine Learning (ML) model can be used to extract patterns from known information (data) about some cars in order to predict car prices based on their characteristics.

### 2. **🧠 Rules-Based Systems vs. Machine Learning**  
   - **Rules-Based Systems:** It is necessary to manually convert rules into code using a programming language and apply them to data to product outcomes. Extracting patterns manually can become complex and challenging.  
   - **Machine Learning:** Instead of manually coding rules, ML models automatically extract patterns from data using Mathematics and Statistics.

### 3. **🔍 Supervised Machine Learning**  
   In supervised learning, models learn from labeled data (with known outcomes) to make predictions on unseen data. There are three types of supervised Machine Learning:
   - Classification: where the target is a class (spam or not spam).
   - Regression: where the target is a number (price).
   - Ranking: the output is a list of items ordered by importance of scores.

### 4. **🛠️ CRISP-DM (Cross Industry Standard Process for Data Mining)**  
   A structured methodology from 90s for organizing ML projects, consisting of the following steps:  
   - 💼 **Business Understanding** : to identify the problem to solve and how to measure the success of the project. Do we need ML ? Maybe a rule-based system is enough.
   - 🔎 **Data Understanding** : to analyze available data and how to get more data. Is the data reliable, large, good enough ? Business understanding might help.
   - 🧹 **Data Preparation** : to transform the data (clean data, build pipelines, convert to a tabular format) to make it ready for a ML algorithm.
   - 🤖 **Modeling**: which model to choose ? This step consists of choosing and training models to select the best one. Going back to add features or fix data issues might be useful.
   - 📊 **Evaluation**: is the model good enough ? Business understanding can help.
   - 🚀 **Deployment**: to roll out the product to users. This step often happens with online evaluation of live users. How well maintanable the model is, how well the service is monitored and the quality good?
   This process is iterative, allowing for continuous improvement.

### 5. **🏆 Model Selection**  
   Split data into training, validation, and test sets. Train different models, validate them, select the best performing one, and then test it on the test set to ensure generalization.
   NB: Note that it is possible to reuse the validation data. After selecting the best model, the validation and training datasets can be combined to form a single training dataset for the chosen model before testing it on the test set.

### 6. **💻 Setting Up the Environment**  
   Install necessary tools like Python, Numpy, Pandas, Matplotlib, Scikit-learn. Anaconda is the easiest option. Eventually create an AWS account for cloud resources.

### 7. **🔢 Introduction to Numpy**  
   Numpy is crucial for manipulating numerical data, providing efficient operations on arrays and matrices.

### 8. **🔗 Linear Algebra**  
   Covering all types of multiplication with vectors and matrices, including the creation of identity matrices using functions like `np.eye()`.

### 9. **📊 Introduction to Pandas**  
   Pandas is a Python library used for processing and analyzing tabular data efficiently.

---
