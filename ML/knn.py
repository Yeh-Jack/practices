# Use build-in datasets by load_***()
import numpy as np
import pandas as pd
from sklearn import neighbors

SKIP_ONE_LINE = "\n\n"

X = pd.DataFrame({
    "durability": [7, 7, 3, 1],
    "strength": [7, 4, 4, 4]
})
y = np.array([0, 0, 1, 1])  # 0 = bad, 1 = good.
k = 3

# Generate testing dataset and train the model.
model = neighbors.KNeighborsClassifier(n_neighbors=k)
model.fit(X, y)

# Predict
# new_product = np.array([[3, 7]])
new_product = pd.DataFrame([[3, 7]], columns=["durability", "strength"])
predict = model.predict(new_product)
print(predict, end=SKIP_ONE_LINE)  # [1] -> predict it's good.
