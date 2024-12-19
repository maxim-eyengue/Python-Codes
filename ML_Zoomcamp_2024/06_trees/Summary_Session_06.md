![ML Zoomcamp Illustration](https://github.com/maxim-eyengue/Python-Codes/blob/main/ML_Zoomcamp_2024/zoomcamp.jpg)
---


## 📚 Session 6 Summary - Machine Learning Zoomcamp
### 1.  **🗺️ Project Overview: Credit Risk Scoring** 
This week's project focuses on building a model to predict the risk of a customer defaulting on a loan.
The model will use information about the client, such as salary, income, and debt, to determine the
probability of default. This is a binary classification problem, with the target variable y being
either `0` (ok) or `1` (default).

| Variable   | Description                      |
|------------|----------------------------------|
| Status     | Credit status                    |
| Seniority  | Job seniority (years)            |
| Home       | Type of home ownership           |
| Time       | Time of requested loan           |
| Age        | Client's age                     |
| Marital    | Marital status                   |
| Records    | Existence of records             |
| Job        | Type of job                      |
| Expenses   | Amount of expenses               |
| Income     | Amount of income                 |
| Assets     | Amount of assets                 |
| Debt       | Amount of debt                   |

**Table: Credit Risk Scoring Dataset Description.**


### 2.  **🗃️ Data Cleaning and Preparation** 
- The dataset was downloaded and the column names were normalized.
- Categorical values were decoded to their original string values.
- Outliers were identified and replaced with missing values.
- Observations with unknown target values (`unk`) were dropped.
- A train-test-validation split was performed.

### 3.  **🌳 Decision Trees** 
- A decision tree is a data structure that uses nodes (conditions) and branches (boolean values for the node condition leading to another nodes) to make predictions. When it has only one condition node, it is called a **decision stump**. The tree starts with a root node and terminates with leaves modes.
- A decision tree classifier was implemented manually to understand its workings, and then a decision
tree classifier from `scikit-learn` was used. Note that there are also decision tree regressors for regression problems.
- **Overfitting:** The difference in scores between the validation and training sets indicated
overfitting (situation occuring when a model learns too much from the training data, so it cannot generalize well on new useen data). Reducing the depth of the tree or setting a maximum number of leaves can help with overfitting. The depth of a tree is the number of leavels it has or the longest pat from the root node to a leaf node.

### 4.  **⚙️ Decision Tree Learning Algorithm** 
**The goal of the learning algorithm is to build the best classifier possible by:**
*   Determining the best conditions to split the data at each node. 
*   Dividing the data into purer sets with lower misclassification rates (weighted average of the rates of errors obtained after splitting data into two sets knowing that for each set, the predicted class will be the majority one), or impurity after each split.
*   Considering each feature with its optimized threshold to determine the best feature for splitting at a particular node.
*   Recursively applying the process at each child node until a stopping criterion is met.

**Stopping criteria are used to prevent overfitting. These include:**

*   The group is already pure.
*   The maximum depth has been reached.
*   The group is smaller than the minimum size set for groups.
*   The maximum number of leaves/terminal nodes has been reached.

**Common misclassification rates include GINI Impurity and Entropy**.

### 5.  **🔧 Decision Trees Parameter Tuning** 
- The `max-depth` (maximum depth of a tree) and `min_samples_leaf` (minimum samples required to be at a leaf node) parameters were fine-tuned.
- Tuning was done in two stages:
    - First, the model was fine-tuned using possible depths to identify a subset of optimal depths.
    - Second, the model was fine-tuned again using the subset of optimal depths and possible values for minimum samples per leaf.
- Scores were visualized using a heatmap to easily identify lower and higher values.
Note that this fine-tuning method is suboptimal particularly for small datasets, but very
useful with large ones, as less computationally expensive. Also, when choosing parameter values, it is
important to avoid `NaN` values, even if they seem to lead to better accuracy, for they do not allow to control the size of the tree.

### 6.  **🌲 Ensemble Learning & Random Forest** 
- **Ensemble Learning:** This approach uses multiple models (weak learners) to make predictions. The final prediction is based on the aggregation of individual model predictions.
- **Random Forest:** A type of ensemble learning that uses multiple decision trees. Each tree is trained on a different random subset of features, preventing all trees from being identical.
- **Key parameters for Random Forest:**
    - `n_estimators`: number of trees in the forest.
    - `max_depth`: maximum depth of a tree.
    - `max_features`: number of features to consider when looking for the best split.
    - `bootstrap`: whether bootstrap samples are used when building trees.
    - `n_jobs`: number of jobs to run in parallel. Setting `n_jobs` to -1 instructs the model to utilize all available processor cores for parallel training, potentially speeding up the process.

**Note:** Trees in random forests are trained independently. That is why they can be trained in parallel.

### 7.  **📈 Gradient Boosting and XGBoost**
- **Boosting:** Models are trained sequentially, with each model correcting the errors of the previous model.
- **XGBoost:** A library that implements gradient boosting trees. 
- **Benefits of XGBoost:**
    - Faster training when using the `xgb.DMatrix()` data structure.
    - Ability to evaluate the model after each tree is trained using a watchlist.
- **Key parameters for XGBoost:**
    - `eta`: learning rate.
    - `max_depth`: maximum depth of a tree.
    - `min_child_weight`: minimum sample size of a child node.
    - `objective`: the problem being solved (regression or classification).
    - `nthread`: number of threads for parallel training.
    - `seed`: random seed for reproducibility.
    - `verbosity`: level of detail in output.
    - `num_boost_round`: how many trees to grow.
    
### 8.  **🔧 XGBoost Parameter Tuning** 
- The following parameters were tuned in order:
    - `eta`.
    - `max_depth`.
    - `min_child_weight`.
- **Other useful parameters:**
    - `subsample` and `colsample_bytree` for subsampling rows and features before model training.
    - `lambda` and `alpha` for L2 and L1 weights regularizations.

### 9.  **🏆 Selecting the Best Model** 
- The XGBoost model had the best performance compared to the decision tree and random forest models.
- The XGBoost model was trained on the full training dataset and tested. It generalized well.
- **Note:** XGBoost tends to perform better for tabular data but can be more complex to fine-tune.

### 10.  **💡 Key Takeaways**
- Decision trees can easily overfit.
- Random forests combine multiple decision trees for better performance.
- Boosting trains trees sequentially to correct previous errors.
