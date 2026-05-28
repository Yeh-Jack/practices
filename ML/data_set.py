# Use build-in datasets by load_***()
from sklearn import datasets as ds

SKIP_ONE_LINE = "\n\n"


def plotScatter(x, y, labelX="X-Axis", lableY="Y-Axis", title="Title"):
    plt.scatter(x, y)
    plt.xlabel(labelX)
    plt.ylabel(lableY)
    plt.title(title)
    plt.show()


# breast_cancer and diabetes are used for regression.
breast_cancer = ds.load_breast_cancer()
diabetes = ds.load_diabetes()

# digits and iris are used for classification.
digits = ds.load_digits()
iris = ds.load_iris()

"""
Keys:
  data: 自變數資料
  target: 因變數資料
  ***_names: ***變數名稱
    feature_names: 自變數名稱
    target_names: 因變數名稱
"""

print(breast_cancer.keys())
print(diabetes.keys())
print(digits.keys())
print(iris.keys(), end=SKIP_ONE_LINE)

# # Testing connection to scikit.learn.fetch site.
# import requests

# url = "https://www.openml.org"
# r = requests.get(url, timeout=20)
# # If 403, the issue is outside sklearn.
# print(f"{r.status_code} from https://www.openml.org")
# url = "https://ndownloader.figshare.com"
# r = requests.get(url, timeout=20)
# # If 403, the issue is in sklearn download site.
# print(f"{r.status_code} from https://ndownloader.figshare.com")


# # Use remote datasets by fetch_***()
# import sklearn

# print(f"sklearn version = {sklearn.__version__}", end=SKIP_ONE_LINE)

# from sklearn.datasets import fetch_california_housing

# housing = fetch_california_housing()
# print(housing.data.shape, housing.target.shape)
# # print(housing.feature_names[0:6])

# from sklearn.datasets import fetch_openml

# mnist = fetch_openml("mnist_784", version=1, as_frame=False, parser="auto")
# print(mnist.keys, end=SKIP_ONE_LINE)

import math
import numpy as np
import pandas as pd
from sklearn import datasets as ds
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae
from matplotlib import pyplot as plt

# dataset = ds.fetch_openml(name="diabetes", version=1)
# dataset = ds.fetch_california_housing()
dataset = ds.load_diabetes()
X = pd.DataFrame(dataset.data, columns=dataset.feature_names)
y = pd.DataFrame(diabetes.target, columns=["Predicted Quantitative Measure"])
# target = pd.DataFrame(dataset.target, columns=["class"])
# y = target["class"]

# Generate testing dataset and train the model.
XTrain, XTest, yTrain, yTest = tts(X, y, test_size=0.25, random_state=2432)
model = LinearRegression()
model.fit(XTrain, yTrain)

# Predict
predict = model.predict(XTest)
plotScatter(yTest, predict, "labelX", "lableY", "title")
print("Done.", end=SKIP_ONE_LINE)

# Calculate correctness of the model.
maeTest = mae(yTest, predict)
mseTest = mse(yTest, predict)
rmseTest = mse(yTest, predict) ** 0.5
rmseTest = math.sqrt(mse(yTest, predict))
print(f"R-squared = {model.score(XTest, yTest)}")
