#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


# Load and preprocess the data
df = pd.read_csv("/Users/sabai/Desktop/data/static/df1-2019.csv")


# In[3]:


# 1. Correlation Analysis

# 'aadb' is 'target'
correlation_matrix = df.corr()

# Plotting the correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.show()

# Selecting features with high correlation to the target variable
correlation_threshold = 0.2
selected_features_corr = correlation_matrix[abs(correlation_matrix['aadb']) > correlation_threshold].index.tolist()
selected_features_corr.remove('aadb')
print("Selected features based on correlation analysis:", selected_features_corr)


# In[12]:


# 2. Feature Importance from Tree-Based Models

import pandas as pd
from sklearn.impute import SimpleImputer

# Separate features and target variable
X = df.drop(columns=['aadb'])
y = df['aadb']

# Impute missing values with mean
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)

# Convert back to DataFrame
X_imputed_df = pd.DataFrame(X_imputed, columns=X.columns)


# In[13]:


from sklearn.ensemble import RandomForestRegressor
import numpy as np

# Train a Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_imputed_df, y)

# Get feature importances
importances = model.feature_importances_
indices = np.argsort(importances)[::-1]

# Print the feature ranking
print("Feature ranking:")
for f in range(X_imputed_df.shape[1]):
    print(f"{f + 1}. feature {X_imputed_df.columns[indices[f]]} ({importances[indices[f]]})")

# Selecting top features
num_features = 10
selected_features_rf = [X_imputed_df.columns[indices[f]] for f in range(num_features)]
print("Selected features based on Random Forest importance:", selected_features_rf)


# In[ ]:





# In[23]:


# 3. Recursive Feature Elimination (RFE)

import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
import numpy as np

# Assuming target variable is 'aadb'
target_variable = 'aadb'

# Separate features and target variable
X = df.drop(columns=[target_variable])
y = df[target_variable]

# Impute missing values with mean
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)

# Convert back to DataFrame
X_imputed_df = pd.DataFrame(X_imputed, columns=X.columns)

# Step 1: Correlation Analysis with the target variable
correlations = X_imputed_df.corrwith(y)
correlation_threshold = 0.1
selected_features_corr = correlations[abs(correlations) > correlation_threshold].index.tolist()
print("Selected features based on correlation analysis:", selected_features_corr)

# Step 2: Feature Importance from RandomForest
model_rf = RandomForestRegressor(n_estimators=100, random_state=42)
model_rf.fit(X_imputed_df, y)

importances = model_rf.feature_importances_
indices = np.argsort(importances)[::-1]

# Selecting top features based on importance
num_features_rf = 10
selected_features_rf = [X_imputed_df.columns[indices[f]] for f in range(num_features_rf)]
print("Selected features based on Random Forest importance:", selected_features_rf)

# Step 3: Recursive Feature Elimination (RFE)
model_lr = LinearRegression()
rfe = RFE(model_lr, n_features_to_select=10)
rfe.fit(X_imputed_df, y)

selected_features_rfe = X_imputed_df.columns[rfe.support_]
print("Selected features based on RFE:", selected_features_rfe.tolist())

# Combining the Results
selected_features_combined = set(selected_features_corr).union(set(selected_features_rf)).union(set(selected_features_rfe))
print("Combined selected features:", selected_features_combined)


# In[24]:


# Combining the Results

selected_features = set(selected_features_corr).union(set(selected_features_rf)).union(set(selected_features_rfe))
print("Combined selected features:", selected_features)


# In[25]:


# Print the number of features (excluding the target variable)
num_features = df.shape[1] - 1  # Subtract 1 for the target variable
print(f"The dataset has {num_features} features.")

