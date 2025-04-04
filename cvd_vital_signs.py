# -*- coding: utf-8 -*-
"""CVD_Vital_SIgns

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PxuuQ2wka43LQ0zEsBj_-XGuJsBDLcBH

**Import Libraries**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""**ٌRead Data**"""

df=pd.read_csv('CVD_Vital_SIgns.csv')

"""**Exploratory Data Analysis (EDA)**"""

df.head()

df.info()

df.isna().sum()

df.duplicated().sum()

df.describe().round(2)

sns.boxplot(df)

df=df[(df.heart_rate<100.00) & (df.heart_rate>7.00)]
df=df[(df.oxygen_saturation<100.00) & (df.oxygen_saturation>-11.00)]
df=df[(df.respiratory_rate<100.00) & (df.respiratory_rate>2.00)]

df.describe()

"""
 **Data Cleaning**"""

df.drop(['subject_id','icustay_id'],axis=1,inplace=True)
df

df['Label'].value_counts()

"""**Visual Data Analysis**"""

sns.histplot(df, x='heart_rate', hue='Label')

sns.displot(data=df,x='blood_pressure',kde=True,hue='Label')

sns.jointplot(data=df,x='blood_pressure',y='oxygen_saturation',hue='Label')

sns.countplot(data=df,x='Label')

X=df.drop('Label',axis=1)
y=df['Label']

"""**Machine Learning Model**"""

from sklearn.model_selection import  train_test_split
x_trian,x_test,y_train,y_test=train_test_split( X, y, test_size=0.2, random_state=42)

x_trian.shape

x_test.shape

y_train.shape

y_test.shape

"""**Build a model**"""

from sklearn.linear_model import  LogisticRegression
lr=LogisticRegression()

lr.fit(x_trian, y_train)

y_pred=lr.predict(x_test)
y_pred

y_test.values

"""**Evaluate model performance**"""

from sklearn.metrics import classification_report

lr.score(x_test,y_test)

lr.coef_

lr.intercept_

report = classification_report(y_test, y_pred)
print(report)

file_path = r"C:\Users\Mass\Downloads\Data.xlsx"
df.to_excel(file_path, index=False)

print(f"File saved at: {file_path}")

# Save the DataFrame to an Excel file within the Colab environment.
df.to_excel('/content/Data.xlsx', index=False)

# Now, you can download the file using files.download.
from google.colab import files
files.download('/content/Data.xlsx')

