![ML Zoomcamp Illustration](../files/zoomcamp.jpg)
---

## 📚 ML Zoomcamp Capstone 01 Project Reviews

During the program, we completed capstone projects that were peer-reviewed, providing valuable insights into our work. This document summarizes comprehensive feedback on three midterm projects from the DataTalksClub ML Zoomcamp. Each review highlights the projects' strengths and areas for improvement, and lessons learned. These insights aim to guide future machine learning projects and foster continuous improvement.

---

### [Project 01 Feedback](https://github.com/AudryBarimbane/ML_zoomcamp_2024/tree/main/Capstone1_ML_Zoomcamp_2024)

#### Summary:
This project folder contains only an empty test script, which highlights the importance of proper submission practices.

#### Key Takeaway:
 Always ensure your work is progressively pushed to the repository, and double-check the version submitted before the deadline.

---


### [Project 02 Feedback: Website phishing and scam prediction](https://github.com/aashalabi/ml-zoomcamp-project/tree/main) 

#### Observations and Suggestions:

1. **💡 Feature Details in the ReadMe**:  
   The ReadMe doesn't explain the features used to detect phishing websites. There is no feature description. Add a section in the ReadMe that clearly explains the features (e.g., URL info, domain registration length) and their role in solving the problem. This will make the goal clearer!  

2. **📝 Text Formatting**:  
   Code blocks for plain text make things hard to read. Stick to Markdown for better readability and presentation.  

3. **✏️ Typos and Unnecessary Info**:  
   There are some typos and extra info like "midterm_project" that don't belong. Proofread carefully and remove irrelevant details to keep the document neat.  

4. **📊 Treat Features Correctly**:  
   Categorical variables (-1, 0, 1) were treated as numbers, and histograms were used for them (which isn't right). Encode categorical features properly, and use appropriate visualizations (e.g., bar charts for categories).  

5. **🎯 Target Variable Analysis**:  
   The target variable wasn't explained or analyzed well. Spend more time analyzing the target variable since it's the core of the problem.  

6. **📈 Model Metrics**:  
   Models were compared using different metrics, which isn't fair. Use the same metric for all models to make the comparisons consistent.  

7. **📦 Irrelevant Libraries**:  
   The training script had imports for libraries that weren't even used. Keep the code clean by including only the libraries you actually use.  

8. **☁️ Deployment**:  
   Cloud deployment wasn't properly done, or at least, not as expected. Only the interface was provided. Provide full deployment scripts along with the interface to meet expectations.  

9. **📋 Following Instructions**:  
   The project didn't fully follow the instructions. Take the time to read and follow all the project requirements carefully before starting.  

---


### [Project 03 Feedback: Airbnb-Price-Prediction](https://github.com/sindhu28ss/airbnb-price-prediction-service)

🚀 **First Impressions:**  
I love how you've organized your README file: it's so clean and well-structured! 👏 Including all the detailed steps in one place was a fantastic idea: it makes it super convenient for others to follow along without needing to dig through multiple files. Also, adding illustrations from your notebook was a smart touch! 🖼️ A small suggestion: consider adding an eye-catching image at the top to represent Airbnb: it would really elevate the visual appeal.  

#### **Observations and Suggestions:**  
1. **Dataset Link:**  
   The Kaggle dataset link in your README isn't pointing to the main dataset card but to the code section. 🔗 Try updating it to make it easier for others to access. Also, including the dataset directly in your repository could make the workflow smoother.  

2. **Repository Structure:**  
   While the files are presented in a logical order, adding a dedicated section to describe the repository structure would make it even more beginner-friendly. 🗂️  

3. **Missing Values Check:**  
   For checking missing values, you used a method that creates a new dataframe, but a simpler approach would be:  
   ```python  
   df.isna().sum()  
   ```  
   This keeps it cleaner and more concise. ✨  

4. **Outliers & Visualization:**  
   I'm curious about the bounds you used to remove outliers: they seem unique. 🤔 I'm familiar with the common 0.1 and 0.9 quantiles, but your method caught my attention! After removing outliers, it's helpful to re-plot the data as you did earlier to easily visualize the changes. 📊  

5. **Model Fine-Tuning:**  
   You trained two models but didn't fine-tune their parameters. Hyperparameter tuning could have improved your performance metrics significantly. 🔧✨  

6. **Training Script:**  
   The training script contains quite a bit of irrelevant information. Streamlining it to focus only on data cleaning and training the optimal model would make it much cleaner and easier to read. 🛠️  

#### **Technical Concerns:**  
1. **Python & Scikit-learn Versions:**  
   The project uses Python 3.12, which isn't aligned with the Zoomcamp's recommended version (3.11). ⚠️ Clarify this in your README so others are aware of potential setup issues. Additionally, the `scikit-learn` version isn't specified in the Pipfile, which might cause dependency errors when running the code.  

2. **Multicollinearity Issue:**  
   The moderate positive correlation between `number_of_reviews_ltm` and `number_of_reviews` suggests multicollinearity. It would be better to keep just one of these features since they provide overlapping information. This step could improve your model's performance. 📉  

3. **Model Selection:**  
   The goal is to *reduce* RMSE, not increase it. Is the chosen model actually better? 🤷‍♂️ It might be worth revisiting this decision to ensure the best performance.  

#### **Overall:**  
Great effort on this project! 🌟 With a few tweaks: like refining your README, adding fine-tuning, and addressing the multicollinearity: you could take this project to the next level. Keep up the amazing work! 💪  

----
For more fun: [click here to review my capstone project.](https://github.com/maxim-eyengue/Depression-Mood-Tracker)