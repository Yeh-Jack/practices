# Use build-in datasets by load_***()
from matplotlib import pyplot as plt
from pandas import DataFrame as df
from sklearn import datasets as ds
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae

SKIP_ONE_LINE = "\n\n"


def plotScatter(x, y, labelX="X-Axis", lableY="Y-Axis", title="Title"):
    plt.scatter(x, y)
    plt.xlabel(labelX)
    plt.ylabel(lableY)
    plt.title(title)
    plt.show()


# Calculate performance of the model.
def showPredict(model, data, target, dataScope):
    predict = model.predict(data)
    maeTest = mae(target, predict)
    mseTest = mse(target, predict)
    rmseTest = mse(target, predict) ** 0.5
    print(
        f"""{dataScope}：
        MSE = {mseTest:.2f}, R-squared = {model.score(data, target):.4f}""",
        end=SKIP_ONE_LINE,
    )


# Load dataset
diabetes = ds.load_diabetes()

# Train model by linear regression.
X = df(diabetes.data, columns=diabetes.feature_names)
y = df(diabetes.target, columns=["Predicted Quantitative Measure"])

# Predict and draw scatter chart for the dataset.
# predict = model.predict(X)
# plotScatter(
#     y,
#     predict,
#     "Quantitative Measure",
#     "Predicted Quantitative Measure",
#     "Quantitative Measure vs. Predicted Quantitative Measure",
# )
# print("Full diabete scatter chart is shown.", end=SKIP_ONE_LINE)

# Full dataset.
model = LinearRegression()
model.fit(X, y)
showPredict(model, X, y, "全部資料")

# 33% testing dataset.
XTrain, XTest, yTrain, yTest = tts(X, y, test_size=0.25, random_state=100)
model = LinearRegression()
model.fit(XTrain, yTrain)
showPredict(model, XTest, yTest, "3:1資料")

# 25% testing dataset.
XTrain, XTest, yTrain, yTest = tts(X, y, test_size=0.20, random_state=100)
model.fit(XTrain, yTrain)
showPredict(model, XTest, yTest, "4:1資料")

# Conclusion.
print("""
=================================================================
MSE：越小越好
R-squared：越大越好（0 ~ 1）

MSE：4:1資料 < 3:1資料 < 全部資料
R-squared：3:1資料 > 全部資料 > 4:1資料

選用 [3:1資料]，因為 R-squared 的表現最優秀，而 MSE 僅略遜於 [4:1資料]。
""")
