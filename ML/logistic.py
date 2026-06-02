import math
import os
import numpy as np
import pandas as pd
from sklearn import preprocessing as pp
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot as plt


SKIP_ONE_LINE = "\n\n"
cwd = os.getcwd() + "/.."
csvPath = cwd + "/data/csv/"
csvPath = "./"


def plotScatter(x, y, labelX="X-Axis", lableY="Y-Axis", title="Title"):
    plt.scatter(x, y)
    plt.xlabel(labelX)
    plt.ylabel(lableY)
    plt.title(title)
    plt.show()


# Data cleaning : fill median value to Age column if it's null.
titanic = pd.read_csv(csvPath+"titanic.csv")
age_median = np.nanmedian(titanic['Age'])
new_age = np.where(titanic['Age'].isnull(), age_median, titanic['Age'])
titanic['Age'] = new_age

# Convert column value to numeric.
label_encoder = pp.LabelEncoder()
encoded_class = label_encoder.fit_transform(titanic['PClass'])
X = pd.DataFrame([encoded_class, titanic['SexCode'], titanic['Age']]).T
y = titanic['Survived']

# Train the model.
model = LogisticRegression()
model.fit(X, y)
# The coefficient shows that the 3rd column 'Age' is less efficient, hence could be ignored.
print(f"Coefficient = {model.coef_}")
print(f"Intercept = {model.intercept_}")

# Predict and print it's confusion matrix.
predict = model.predict(X)
print(f'''
Confusion matrix:
{pd.crosstab(titanic['Survived'], predict)}

Accuracy: {model.score(X, y)}
''', end=SKIP_ONE_LINE)
