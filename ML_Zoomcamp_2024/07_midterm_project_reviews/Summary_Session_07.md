![ML Zoomcamp Illustration](https://github.com/maxim-eyengue/Python-Codes/blob/main/ML_Zoomcamp_2024/zoomcamp.jpg)
---
## 📚 Session 7 Summary -  ML Zoomcamp Midterm Project Reviews

During three weeks, we completed midterm projects for the program, and they were evaluated by our peers. This file summarizes comprehensive reviews of three midterm projects from the DataTalksClub ML Zoomcamp. The objective is to provide a detailed analysis of each project, highlighting its strengths, weaknesses, and the valuable lessons learned from the review process. For each project, the review covers various aspects, including typos and file organization, exploratory data analysis (EDA), feature importance analysis, model fine-tuning, notebook readability, dependency management, documentation, and Docker deployment. The insights gained from these reviews aim to guide future machine learning projects and foster continuous improvement.

### 1. Diabetes Prediction Project

*   **Project Link:** [https://lnkd.in/eZxa3EfN](https://lnkd.in/eZxa3EfN)

*   **Project Topic:** This project aims to build a machine learning model that predicts whether a patient has diabetes based on specific medical attributes. Early diagnosis of diabetes is crucial for effective management and treatment.

*   **Detailed Review:**

    *   **Typos and File Organization:** The README file contains typos that need correction. Additionally, the repository structure can be simplified by removing the raw `.ipynb` file, leaving only `train.py` for clarity and conciseness.
    *   **Exploratory Data Analysis (EDA):** The EDA provided in the project lacks depth and does not adequately address the nuances of the dataset. Given that the data deals with real-world patient health information, a robust data cleaning process is essential. The presence of unrealistic `0` values for critical medical features like glucose, insulin, blood pressure, skin thickness, and BMI raises concerns about data quality. Imputation techniques or other methods to handle missing or incorrect data should have been employed to enhance the reliability of the analysis.
    *   **Feature Importance Analysis:** The method used for feature importance analysis is unconventional and unreliable.  Instead, consider using more reliable techniques like Pearson correlation for numerical variables, mutual information for categorical variables, or risk ratio analysis. These techniques offer more meaningful insights into feature relevance.
    *   **Model Fine-Tuning:** Fine-tuning the random forest classifier solely based on the number of trees is insufficient. Adjusting other parameters like tree depth and the minimum number of samples per leaf is crucial to optimize the model's performance.
    *   **Notebook Readability:** The notebook lacks structure and clarity, making it difficult to follow. Future projects should prioritize improving the structure and readability of notebooks. Clear explanations, well-organized sections, and consistent formatting enhance the understanding of the workflow for others.
    *   **Dependency Management:** The project includes unnecessary libraries, like `xgboost`, which are not used in the project. Removing such libraries will reduce resource usage and optimize the environment.
    *   **Documentation:** The README file lacks essential information, including instructions for installing dependencies and activating the environment. This information is crucial for enabling others to reproduce the work. A section on environment setup and dependency installation is recommended to improve the usability of the project.
    *   **Docker Deployment and Postman:** The project uses Postman for testing the Docker deployment, but the process lacks explanation. Including details or a brief tutorial on using Postman for testing would make the project more informative and complete.

*   **Lessons Learned:**
    *   Real-world scenarios, particularly those involving healthcare data, demand a robust and thorough data cleaning process. Handling unrealistic values, such as `0` for medical attributes, is critical for accurate analysis and reliable model performance.
    *   Feature importance analysis should be conducted using reliable and standard techniques like Pearson correlation for numerical variables and mutual information for categorical variables. This ensures that the most relevant features are identified for building the model.
    *   Fine-tuning a random forest model should extend beyond adjusting the number of trees. Parameters like tree depth and the minimum number of samples per leaf significantly impact model performance and should be optimized.
    *   Maintaining a clean and well-organized repository is essential for reproducibility. This includes a clear README file with instructions for setting up the environment, installing dependencies, and running the code. The repository should also be free of unnecessary files and libraries.
    *   The use of tools like Docker and Postman for deployment and testing should be well-documented. Providing clear instructions and explanations makes the project more accessible and reproducible for others.

### 2.  RestAI: Sleep Quality Prediction

*   **Project Link:** [https://lnkd.in/eHF-tMHv](https://lnkd.in/eHF-tMHv)

*   **Project Topic:** This project introduces RestAI, a tool that predicts sleep quality based on daily habits. Users input information about their day, such as caffeine intake, screen time, and physical activity, to receive feedback on their potential sleep quality.

*   **Detailed Review:**

    *   **Positive Aspects:** 
        *   The project effectively communicates the importance of sleep quality and the potential benefits of RestAI. 
        *   Combining various datasets and strategically subsetting the data to focus on user-controllable features demonstrates an insightful and practical approach to the problem.
        *   Performing EDA on each dataset independently before analyzing the combined data showcases a structured and thoughtful approach to understanding the data.
        *   Defining functions to streamline the process highlights the developer's attention to detail and efficiency.
    *   **Suggestions for Improvement:** 
        *   **Real-World Datasets:** Utilizing real-world datasets would significantly enhance the credibility and reliability of the project's results.
        *   **Feature Importance Techniques:** Employing more robust feature importance techniques, such as mutual information for categorical variables and Pearson's correlation coefficient for numerical variables, would provide more insightful results.
        *   **Dataset Selection and Combination:** The process of selecting and combining datasets requires further clarification. Providing a more detailed explanation of the rationale and methodology behind these choices would enhance the project's transparency and reproducibility.
        *   **Specify Software Versions:**  Specifying the appropriate version of scikit-learn in the environment setup is crucial to ensure the project's reproducibility and avoid potential errors.
        *   **Correct Typos:**  Proofreading the project documentation for typos is essential to maintain a professional and polished presentation.

*   **Lessons Learned:** 
    *   The `skew()` function is a useful tool for evaluating the skewness of data features, which is important for understanding the data distribution.
    *   Scaling data is a crucial step in many machine learning workflows, as it can improve the performance of certain algorithms.
    *   `KNNImputer()` provides an effective method for imputing missing data, enhancing the dataset's completeness and potentially improving model performance.
    *   Histograms offer a visual representation of data distribution, aiding in understanding the characteristics of numerical features.
    *   Box plots help visualize the distribution of data, including the median, quartiles, and potential outliers, providing a concise summary of the data's spread and central tendency.

### 3. Cirrhosis Diagnosis

*   **Project Link:** [https://lnkd.in/eA6jQ5ae](https://lnkd.in/eA6jQ5ae)

*   **Project Topic:** This project leverages machine learning models (Gradient Boosting, SVM, Random Forest) to predict liver disease, particularly cirrhosis, using a dataset from UCI. The goal is to explore the potential of ML as an alternative to traditional diagnostic methods like biopsies.

*   **Detailed Review:**
    *   **Correct Minor Typos:**  The documentation requires proofreading to correct minor typos, improving readability and professionalism.
    *   **Detail the Target Variable:** The README should provide a more detailed explanation of the target variable, specifically the stages of the disease represented by 1, 2, 3, and 4. Clear definitions of these stages are crucial for understanding the project's objective.
    *   **Handling Missing Values:** Before filling missing values, it's essential to calculate the percentage of missing data for each variable.  If variables like `Triglycerides` and `Cholesterol` have a high percentage of missing values, filling them in might introduce bias.  Consider removing observations with excessive missing values or dropping variables with significant missingness.
    *   **Pearson Correlation:** Utilizing Pearson correlation for numerical features can effectively assess their relationships and help in identifying potential multicollinearity issues.
    *   **Explain EDA Plots:** EDA plots should be accompanied by interpretations or explanations of their purpose. This clarifies the analysis and helps others understand the insights derived from the visualizations.
    *   **Model Fine-Tuning:**  Fine-tuning should be applied to all models before selecting the optimal one. This ensures a fair comparison and helps in identifying the best-performing model for the given task.
    *   **Set random\_state for Reproducibility:** Setting the `random_state` for all models is crucial for reproducibility. It ensures that the results can be consistently replicated, enhancing the project's reliability.
    *   **Clean Your Notebook:** The notebook should be well-organized and free of unnecessary code or output to improve its readability and professionalism. 
    *   **Clarify File Structure:** The README should provide a clear explanation of the file structure, outlining the purpose and location of each file and folder. This makes it easier for others to navigate the project and understand its organization.
    *   **Environment and Dependencies Management:** While an environment was set up, errors occurred due to an incompatible version of scikit-learn. Ensuring that the correct version of scikit-learn (`1.5.1`) is installed is vital. Additionally, a deeper understanding of environment and dependency management is crucial for avoiding compatibility issues.

*   **Lessons Learned:** 
    *   Traditional methods for diagnosing cirrhosis, like biopsies and imaging, can potentially be complemented or replaced by machine learning models using features like Ascites, Hepatomegaly, Spiders, Bilirubin, and SGOT.
    *   Addressing class imbalance is crucial for improving the performance of machine learning models, particularly in healthcare applications where the prevalence of certain conditions might be low. Techniques like the hybrid `SMOTETomek()`, which combines oversampling (SMOTE) and undersampling (Tomek links), can effectively handle imbalanced datasets.
    *   Model explainability is paramount in healthcare, where understanding the rationale behind a model's prediction is essential for building trust and ensuring responsible use. Tools like SHAP (SHapley Additive exPlanations) can provide insights into the model's decision-making process, bridging the gap between AI and human understanding.

---
For more fun: [Click here to review my midterm project](https://github.com/maxim-eyengue/Heart-Disease-App)
