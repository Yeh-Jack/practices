# Use build-in datasets by load_***()
from matplotlib import pyplot as plt
from pandas import DataFrame as df
from sklearn import datasets as ds
from sklearn.linear_model import LinearRegression

SKIP_ONE_LINE = "\n\n"


def plotScatter(x, y, labelX="X-Axis", lableY="Y-Axis", title="Title"):
    plt.scatter(x, y)
    plt.xlabel(labelX)
    plt.ylabel(lableY)
    plt.title(title)
    plt.show()


# Load dataset
diabetes = ds.load_diabetes()

# Train model by linear regression.
X = df(diabetes.data, columns=diabetes.feature_names)
y = df(diabetes.target, columns=["Predicted Quantitative Measure"])
model = LinearRegression()
model.fit(X, y)

# Predict and draw scatter chart for the dataset.
predict = model.predict(X)
plotScatter(
    y,
    predict,
    "Quantitative Measure",
    "Predicted Quantitative Measure",
    "Quantitative Measure vs. Predicted Quantitative Measure",
)
print("Full diabete scatter chart is shown.", end=SKIP_ONE_LINE)

# Extract some factors only for prediction.
print(diabetes.feature_names, end=SKIP_ONE_LINE)
chosen_factors = X.iloc[:, :4]  # first 4 columns: 'age', 'sex', 'bmi', 'bp'

model = LinearRegression()
model.fit(chosen_factors, y)

# Predict and draw scatter chart for the dataset.
predict = model.predict(chosen_factors)
plotScatter(
    y,
    predict,
    "Quantitative Measure",
    "Predicted Quantitative Measure",
    "Quantitative Measure of Age, Sex, BMI and BP",
)
print("Some diabete factors scatter chart is shown.", end=SKIP_ONE_LINE)
