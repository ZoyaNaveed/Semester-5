# Diabetes-Predictor
Diabetes Predictor
Project Overview:
Introduction:
In this project, our objective is to predict whether the patient has diabetes or not based on various features like Glucose level, Insulin, Age, and BMI. We will perform all the steps from Data gathering to Model deployment. During Model evaluation, we compare various machine learning algorithms on the basis of accuracy_score metric and find the best one. Then we create a web app using Flask which is a python micro framework.
Algorithm used:
•	Logistic Regression Algorithm
•	Random Forest Algorithm
•	K nearest neighbors Algorithm
•	Support Vector Classifier Algorithm
•	Naïve Bayes Algorithm
•	Decision Tree Algorithm
Data Set Used:
Pima Indians Diabetes Database
https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database
Observations:	
1.	There are a total of 768 records and 9 features in the dataset.
2.	Each feature can be either of integer or float data type.
3.	 Some features like Glucose, Blood pressure, Insulin, BMI have zero values which represent missing data.
4.	There are zero NaN values in the dataset.
5.	In the outcome column, 1 represents diabetes positive and 0 represents diabetes negative
Contribution we did to the project:
1.	Used a new Dataset
2.	Used a different FrontEnd
3.	Additional comparison with other algorithms
Accuracy Analysis:
1.	Logistic Regression: 71.42857142857143
2.	K Nearest neighbors: 78.57142857142857
3.	Support Vector Classifier: 73.37662337662337
4.	Naive Bayes: 71.42857142857143
5.	Decision tree: 68.18181818181817
6.	Random Forest: 75.97402597402598

Installation:
•	Go to flask directory
•	Begin a new virtual environment with Python 3
•	Install the required packages using pip install -r requirements.txt
•	Execute the command: python app.py

Execution:
Step 0: Data gathering and importing libraries
All the standard libraries like numpy, pandas, matplotlib and seaborn are imported in this step. We use numpy for linear algebra operations, pandas for using data frames, matplotlib and seaborn for plotting graphs. The dataset is imported using the pandas command read_csv().
Step 1: Descriptive Analysis
1.	There are a total of 768 records and 9 features in the dataset.
2.	Each feature can be either of integer or float data type.
3.	 Some features like Glucose, Blood pressure, Insulin, BMI have zero values which represent missing data.
4.	There are zero NaN values in the dataset.
5.	In the outcome column, 1 represents diabetes positive and 0 represents diabetes negative
Step 2: Data visualizations
 
Observations:
1. The countplot tells us that the dataset is imbalanced, as the number of patients who don’t have diabetes is more than those who do.
2. From the correlation heatmap, we can see that there is a high correlation between Outcome and [Glucose, BMI, Age, Insulin]. We can select these features to accept input from the user and predict the outcome.

Step 3: Data Preprocessing	
In this dataset, the missing values are represented by zero values that need to be replaced. The zero values are replaced by NaN so that missing values can easily be imputed using the fillna() command.
We perform Feature scaling on the dataset using Minmaxscaler() so that it scales the entire dataset such that it lies between 0 and 1. It is an important preprocessing step for many algorithms
Step 4: Data Modelling	
Use of SVC and comparison of other algorithms.
Step 5: Model Evaluation
We have chosen three metrics accuracy_score, confusion matrix and classification report for evaluating our model.
Step 6: Model Deployment	
In this step, we will use Flask micro-framework to create a web application of our model. All the required files can be found in my GitHub repository here.
