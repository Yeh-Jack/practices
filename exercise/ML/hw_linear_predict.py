import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
from sklearn.linear_model import LinearRegression

# Build sampling data.
height = np.array([147, 163, 159, 155, 163, 158, 172, 161, 153, 161])
dfHeight = pd.DataFrame(height, columns=["Height"])
weight = np.array([51, 60, 57, 53, 60, 55, 68, 59, 56, 62])
dfWeight = pd.DataFrame(weight, columns=["Weight"])

# Predict Weight from Height (Height -> Weight)
model_weight = LinearRegression()
model_weight.fit(dfHeight, dfWeight)
print(f"""
=============================================
Predict Weight from Height (Height -> Weight)
Regression result:
\tcoefficient = [{model_weight.coef_[0][0]:.1f}]
\tintercept   = [{model_weight.intercept_[0]:.1f}]
""")

h4p = np.array([155, 165, 180])  # h4p = height for predict
dfh4p = pd.DataFrame(h4p, columns=["Height"])  # dfh4p = dataFrame of height for predict
pw = model_weight.predict(dfh4p)  # pw = predicted weight
for idx, pdw in enumerate(pw):
    print(f"Predicted weight = [{pdw[0]:.1f}] for height [{h4p[idx]:.1f}].")

# Predict Height from Weight (Weight -> Height)
model_height = LinearRegression()
model_height.fit(dfWeight, dfHeight)
print(f"""
=============================================
Predict Height from Weight (Weight -> Height)
Regression result:
\tcoefficient = [{model_height.coef_[0][0]:.1f}]
\tintercept   = [{model_height.intercept_[0]:.1f}]
""")

w4p = np.array([55, 65, 70])  # w4p = weight for predict
dfw4p = pd.DataFrame(w4p, columns=["Weight"])  # dfw4p = dataFrame of weight for predict
ph = model_height.predict(dfw4p)  # ph = predicted height
for idx, pdh in enumerate(ph):
    print(f"Predicted height = [{int(pdh[0])}] for weight [{w4p[idx]:.1f}].")

# Draw a scatter chart to the prediction.
plot.scatter(dfHeight, dfWeight)
# plot.plot(dfHeight, dfWeight, color="blue")
plot.plot(ph, dfw4p, color="red", marker="o", markersize=10)
plot.show()
