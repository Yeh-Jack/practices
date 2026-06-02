# Use build-in datasets by load_***()
import pandas as pd
from sklearn import datasets as ds
from sklearn.model_selection import train_test_split as tts
from sklearn import neighbors
from matplotlib import pyplot as plt

SKIP_ONE_LINE = "\n\n"


def plotScatter(x, y, labelX="X-Axis", lableY="Y-Axis", title="Title"):
    plt.scatter(x, y)
    plt.xlabel(labelX)
    plt.ylabel(lableY)
    plt.title(title)
    plt.show()


# iris is used for classification.
"""
Keys:
  data: 自變數資料
  target: 因變數資料
  ***_names: ***變數名稱
    feature_names: 自變數名稱
    target_names: 因變數名稱
"""
iris = ds.load_iris()
print(iris.keys(), end=SKIP_ONE_LINE)
print(iris.feature_names)
print(iris.DESCR, end=SKIP_ONE_LINE)

X = pd.DataFrame(iris.data, columns=iris.feature_names)
target = pd.DataFrame(iris.target, columns=["target"])
y = target["target"]
k = 3

# Generate testing dataset and train the model.
XTrain, XTest, yTrain, yTest = tts(X, y, test_size=0.25, random_state=2432)
model = neighbors.KNeighborsClassifier(n_neighbors=k)
model.fit(XTrain, yTrain)

predict = model.predict(XTest)
print(f"Accuracy: {model.score(XTest, yTest):.2f}", end=SKIP_ONE_LINE)
print(predict)
print(yTest.values, end=SKIP_ONE_LINE)  # [1] -> predict it's good.
