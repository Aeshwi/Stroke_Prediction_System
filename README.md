# Stroke_Prediction_System
A stroke, also known as brain attack, is a medical emergency where blood supply to a part of the brain is blocked or
or when a blood vessel in the brain bursts which can lead to brain death. Timely diagnosis of brain strokes are
crucial for effective treatment.
# Overview
This project aims to predict stroke events using a healthcare dataset. The dataset contains various health-related attributes which are analyzed, preprocessed, and used to build multiple classification models to predict stroke occurrences. The project includes steps for handling missing values, encoding categorical variables, balancing the dataset, scaling features, and optimizing model parameters using Grid Search.

# Dataset Information
The dataset used in this project is healthcare-dataset-stroke-data.csv. The dataset consists of 12 columns and a total of 5110 entries. The aim of using this dataset is to predict whether a
patient will experience stroke or not. It includes the following columns:

id: Unique identifier for each patient.
gender: Gender of the patient.
age: Age of the patient.
hypertension: Whether the patient has hypertension.
heart_disease: Whether the patient has heart disease.
ever_married: Marital status of the patient.
work_type: Type of work the patient does.
Residence_type: Type of residence the patient lives in.
avg_glucose_level: Average glucose level in the blood.
bmi: Body Mass Index.
smoking_status: Smoking status of the patient.
stroke: Whether the patient had a stroke.
# 1. Data Loading and Preprocessing
Load the Data: Load the dataset and inspect its structure and contents.

Drop Unnecessary Columns: Remove the id column as it does not contribute to the prediction.

Handle Missing Values: Check for missing values in the dataset and fill the missing bmi values with the mean of the column.

Outlier Detection and Handling: Calculate the interquartile range (IQR) for the bmi column and identify outliers based on the IQR. Handle these outliers appropriately.

Encode Categorical Variables: Convert categorical variables such as gender, ever_married, work_type, Residence_type, and smoking_status into numerical format using label encoding.
# Data Balancing and Splitting
Balance the Dataset using SMOTE: Since the dataset is imbalanced (more instances of no stroke than stroke), use Synthetic Minority Over-sampling Technique (SMOTE) to balance the dataset.

Further Split the Data: Split the balanced dataset into training and testing sets to evaluate model performance.

Feature Scaling: Scale the features to ensure that all variables contribute equally to the model training.
