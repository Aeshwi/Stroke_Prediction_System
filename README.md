# Stroke_Prediction_System
A stroke, also known as brain attack, is a medical emergency where blood supply to a part of the brain is blocked or
or when a blood vessel in the brain bursts which can lead to brain death. Timely diagnosis of brain strokes are
crucial for effective treatment.
## Overview
This project aims to predict stroke events using a healthcare dataset. The dataset contains various health-related attributes which are analyzed, preprocessed, and used to build multiple classification models to predict stroke occurrences. The project includes steps for handling missing values, encoding categorical variables, balancing the dataset, scaling features, and optimizing model parameters using Grid Search.

## Dataset Information
The dataset used in this project is [Stroke Prediction Dataset]([https://pages.github.com/](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset?resource=download)). The dataset consists of 12 columns and a total of 5110 entries. The aim of using this dataset is to predict whether a
patient will experience stroke or not. It includes the following columns:

id: Unique identifier for each patient.<br />
gender: Gender of the patient.<br />
age: Age of the patient.<br />
hypertension: Whether the patient has hypertension.<br />
heart_disease: Whether the patient has heart disease.<br />
ever_married: Marital status of the patient.<br />
work_type: Type of work the patient does.<br />
Residence_type: Type of residence the patient lives in.<br />
avg_glucose_level: Average glucose level in the blood.<br />
bmi: Body Mass Index.<br />
smoking_status: Smoking status of the patient.<br />
stroke: Whether the patient had a stroke.<br />
## Data Loading and Preprocessing
Load the Data: Load the dataset and inspect its structure and contents.

Drop Unnecessary Columns: Remove the id column as it does not contribute to the prediction.

Handle Missing Values: Check for missing values in the dataset and fill the missing bmi values with the mean of the column.

Outlier Detection and Handling: Calculate the interquartile range (IQR) for the bmi column and identify outliers based on the IQR. Handle these outliers appropriately.

Encode Categorical Variables: Convert categorical variables such as gender, ever_married, work_type, Residence_type, and smoking_status into numerical format using label encoding.
## Data Balancing and Splitting
Balance the Dataset using SMOTE: Since the dataset is imbalanced (more instances of no stroke than stroke), use Synthetic Minority Over-sampling Technique (SMOTE) to balance the dataset.

Further Split the Data: Split the balanced dataset into training and testing sets to evaluate model performance.

Feature Scaling: Scale the features to ensure that all variables contribute equally to the model training.

## Model Building and Evaluation
Train and Evaluate Multiple Models: the Ensemble Learning technique of bagging and boosting classifiers to reduce the variance and bias respectively. Train various classification models such as Random Forest, Bagging Classifier, AdaBoost, XGBoost, and K-Nearest Neighbors using the training data. Evaluate these models based on their prediction performance on the test data.

Evaluation Function: Define a function to evaluate the models, which includes calculating sensitivity, specificity, accuracy, precision, recall, F1 score, and AUC score. Additionally, plot the Receiver Operating Characteristic (ROC) curve to visualize model performance.

Perform Grid Search for Hyperparameter Tuning: Optimize model parameters using Grid Search with cross-validation to find the best performing model configurations. This process involves defining parameter grids for each model and evaluating the models with different parameter combinations to select the best model.

## Results
Accuracy Score of each model: <br />
● Random Forest: 0.95 
● Bagging Classifier: 0.80<br />
● AdaBoost: 0.95<br />
● XGBoost: 0.94<br />
● KNN: 0.89<br />

## Correlation Analysis
Perform a correlation analysis to identify highly correlated features. This helps in understanding the relationships between different variables and selecting the most relevant features for the model.

## Visualization
Visualize the data and model results using various plots such as scatter plots and heatmaps to gain insights into the data distribution and model performance.

## Conclusion
The project successfully preprocesses the healthcare dataset, handles missing values, balances the dataset, scales features, and builds and evaluates multiple classification models to predict stroke occurrences. Hyperparameter tuning using Grid Search improves the model performance, and correlation analysis helps in selecting the most relevant features for the prediction task.

