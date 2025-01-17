# -*- coding: utf-8 -*-
"""Stroke Prediction System.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19elA0mVYqkdlGDT73qU43fkAYmqeg8OS

# Brain Stroke Detection

Done by:
 - 21BCE011
 - 21BCE012
 - 21BCE020
---
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
import xgboost as xgb
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import ParameterGrid
from sklearn.metrics import silhouette_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report,accuracy_score,confusion_matrix
from sklearn.metrics import auc,roc_auc_score,roc_curve,precision_score,recall_score,f1_score

df = pd.DataFrame(pd.read_csv("/content/drive/MyDrive/SEM_VI/DE/DM/Innovative/healthcare-dataset-stroke-data.csv"))
df.info()

df.head()

"""Stroke = 1 indicates stroke risk being detected.

Stroke = 0 indicates no stroke risk detected.

---

## Data Preprocessing

 - Check for missing values and fill accordingly
 - Smooth the outliers if necessary
 - Reduction and Transformation are not needed due to small size of dataset
"""

# Remove irrelevant columns for further processing
df = df.drop(columns=['id'])

# Check missing values
print(df.isna().any())

# Check outliers
q1 = df['bmi'].quantile(0.25)
q3 = df['bmi'].quantile(0.75)
iqr = q3 - q1
outliers = (df['bmi'] < (q1 - 1.5 * iqr)) | (df['bmi'] > (q3 + 1.5 * iqr))
outliers.value_counts()

# Fill missing values with mean
df['bmi'] = df['bmi'].fillna(df['bmi'].mean())

# Label Encoding - Convert categorical values to integers for computation
categorical_cols = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
label_encoder = LabelEncoder()
for col in categorical_cols:
    df[col] = label_encoder.fit_transform(df[col])

# Check whether dataset is balanced or not
print("Number of cases with no stroke detected: ", sum(df['stroke'] == 0))
print("Number of cases with stroke detected: ", sum(df['stroke'] == 1))

"""---

## Imbalanced Dataset
The dataset being used in imbalanced due to uneven distribution of the class label 'stroke'.
"""

# Split dataset
X = df.drop(['stroke'], axis=1)
y = df['stroke']
X_train, X_test , y_train , y_test = train_test_split(X, y, test_size = 0.2)

# Balance dataset using SMOTE (Synthetic Minority Oversampling Technique) approach
print("Before (label '1'): {}".format(sum(y_train == 1)))
print("Before (label '0'): {} \n".format(sum(y_train == 0)))
smo = SMOTE()
X_res, y_res = smo.fit_resample(X_train, y_train.ravel())
print("After (label '1'):", sum(y_res == 1))
print("After (label '0'):", sum(y_res == 0))

# Split the data based on balanced dataset
X_train_new, X_test_new, y_train_new, y_test_new = train_test_split(X_res, y_res, random_state = 42)

"""---

## Data Normalization
"""

# Data Normalization

# Z-Score Normalization
scaler1 = StandardScaler()
X_train_scaled_1 = scaler1.fit_transform(X_train_new)
X_test_scaled_1 = scaler1.transform(X_test_new)

"""---

## Data Mining

  - Bagging and Boosting Classifiers
"""

# Random Forest
RF = RandomForestClassifier()
RF.fit(X_train_scaled_1, y_train_new)
y_pred_RF = RF.predict(X_test_scaled_1)

# BaggingClassifier
BC = BaggingClassifier()
BC.fit(X_train_scaled_1, y_train_new)
y_pred_BC = BC.predict(X_test_scaled_1)

# Adaboost
ADA = AdaBoostClassifier()
ADA.fit(X_train_scaled_1, y_train_new)
y_pred_ADA = ADA.predict(X_test_scaled_1)

# XGBoost
XGB = xgb.XGBClassifier()
XGB.fit(X_train, y_train)
y_pred_XGB = XGB.predict(X_test_scaled_1)

# K-Nearest Neighbours
KNN = KNeighborsClassifier()
KNN.fit(X_train_scaled_1, y_train_new)
y_pred_KNN = KNN.predict(X_test_scaled_1)

"""---

## Evaluation Metrics
"""

def sen_spe(y_true,y_pred):
    CM = confusion_matrix(y_true,y_pred)
    TP = CM[1][1]
    TN = CM[0][0]
    FP = CM[0][1]
    FN = CM[1][0]
    sensitivity = TP / (TP + FN)
    specificity = TN / (TN + FP)
    return sensitivity,specificity

def evaluate_model(model, X_test, y_test):
  y_pred = model.predict(X_test)
  y_prob = model.predict_proba(X_test)
  print("Classification Report:\n{}".format(classification_report(y_test, y_pred)))
  accuracy = accuracy_score(y_test, y_pred)
  print("Accuracy Score: {:.2f}".format(accuracy))
  precision = precision_score(y_test, y_pred)
  recall = recall_score(y_test, y_pred)
  f1 = f1_score(y_test, y_pred)
  sensitivity, specificity = sen_spe(y_test, y_pred)
  auc = roc_auc_score(y_test, y_prob[:,1])
  fpr, tpr, _ = roc_curve(y_test,  y_prob[:,1])
  print("Precision Score: {:.2f}".format(precision))
  print("Recall Score: {:.2f}".format(recall))
  print("F1 Score: {:.2f}".format(f1))
  print("Sensitivity: {:.2f}".format(sensitivity))
  print("Specificity: {:.2f}".format(specificity))
  print("AUC score: {:.2f}".format(auc))
  fig, ax = plt.subplots()
  ax.plot(fpr, tpr, color='purple', label='ROC curve (area = %0.2f)' % auc)
  ax.plot([0, 2], [0, 2], color='orange', linestyle='--')
  ax.set_xlim([-0.1, 1.0])
  ax.set_ylim([0.0, 1.1])
  ax.set_xlabel('False Positive Rate')
  ax.set_ylabel('True Positive Rate')
  ax.set_title('Receiver Operating Characteristic')
  ax.legend(loc = "lower right")
  plt.show()
  # return accuracy, precision, recall, f1

"""---

## Parameter Grid Searching

 Find the best hyperparameters for each respective model
"""

def perform_grid_search(model, param_grid, X_train, y_train, X_test, y_test):
  GS = GridSearchCV(estimator=model, param_grid=param_grid, cv=3, scoring='accuracy', verbose=2, n_jobs=-1)
  GS.fit(X_train, y_train)
  print("Best Parameters:", GS.best_params_)
  best_model = GS.best_estimator_
  evaluate_model(best_model, X_test, y_test)

rf_param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['auto', 'sqrt']
}

bagging_param_grid = {
    'base_estimator': [DecisionTreeClassifier(max_depth=1), DecisionTreeClassifier(max_depth=2)],
    'n_estimators': [50, 100, 200],
    'max_samples': [0.5, 0.8, 1.0],
    'max_features': [0.5, 0.8, 1.0],
    'bootstrap': [True, False],
    'bootstrap_features': [True, False]
}

ada_param_grid = {
    'base_estimator': [DecisionTreeClassifier(max_depth=1), DecisionTreeClassifier(max_depth=2)],
    'n_estimators': [50, 100, 200],
    'learning_rate': [0.1, 0.5, 1.0]
}

xgb_param_grid = {
    'learning_rate': [0.01, 0.1, 0.2],
    'max_depth': [3, 4, 5],
    'n_estimators': [100, 200, 300]
}

knn_param_grid = {
    'n_neighbors': [3, 5, 10],
    'weights': ['uniform', 'distance'],
    'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute']
}

perform_grid_search(RF, rf_param_grid, X_train_scaled_1, y_train_new, X_test_scaled_1, y_test_new)

perform_grid_search(BC, bagging_param_grid, X_train_scaled_1, y_train_new, X_test_scaled_1, y_test_new)

perform_grid_search(ADA, ada_param_grid, X_train_scaled_1, y_train_new, X_test_scaled_1, y_test_new)

perform_grid_search(XGB, xgb_param_grid, X_train_scaled_1, y_train_new, X_test_scaled_1, y_test_new)

perform_grid_search(KNN, knn_param_grid, X_train_scaled_1, y_train_new, X_test_scaled_1, y_test_new)

"""---

## Feature Selection
"""

# Correlation Based Feature Selection
corr = df.corr()
corr.head()

sns.heatmap(corr)

col = np.full((corr.shape[0],), True, dtype=bool)
for i in range(corr.shape[0]):
    for j in range(i+1, corr.shape[0]):
        if corr.iloc[i,j] >= 0.5:
            if col[j]:
                col[j] = False
relevant_col = df.columns[col]
# df.shape
relevant_col.shape
relevant_col

df1 = df.copy()
df1 = df[relevant_col]
df1

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='stroke', y='bmi', palette='viridis', s=60, alpha=0.5)
plt.title('Clusters based on stroke and bmi')
plt.legend(title='Cluster')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()