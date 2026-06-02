# Use build-in datasets by load_***()
import pandas as pd
from sklearn import datasets as ds
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split as tts

SKIP_ONE_LINE = "\n\n"

"""
Keys:
  data: 自變數資料
  target: 因變數資料
  ***_names: ***變數名稱
    feature_names: 自變數名稱
    target_names: 因變數名稱
"""
breast_cancer = ds.load_breast_cancer()


# print(f"Keys:\n{breast_cancer.keys()}", end=SKIP_ONE_LINE)
# print(f"Feature names:\n{breast_cancer.feature_names}", end=SKIP_ONE_LINE)
# print(breast_cancer.DESCR)

X = pd.DataFrame(breast_cancer.data, columns=breast_cancer.feature_names)
target = pd.DataFrame(breast_cancer.target, columns=["target"])
y = target["target"]

# 1. Train the model with the full dataset.
model = LogisticRegression(max_iter=3000)
model.fit(X, y)
print(f"1. Accuracy of full dataset: {
      model.score(X, y):.2f}", end=SKIP_ONE_LINE)

# 2. Pick 5 factors for training.
selected_features = [
    'mean radius',
    'mean texture',
    'mean smoothness',
    'mean concave points',
    'mean fractal dimension'
]
_5factors = X[selected_features]

model = LogisticRegression()
model.fit(_5factors, y)
print(f"""2. 選擇最適當的五個欄位建立訓練模型：
    A. radius (mean of distances from center to points on the perimeter)
       細胞核半徑：指從細胞核中心點到其外週邊緣各點的平均距離。數值愈大通常代表細胞核愈大。
    B. texture (standard deviation of gray-scale values)
       細胞核灰階紋理：它用來衡量細胞核表面顏色的均勻度。惡性腫瘤的細胞核內部往往較為混亂、不均勻。
    C. concave points (number of concave portions of the contour)
       細胞核凹陷點數量：細胞核輪廓中向內凹陷部位的數量。
    D. smoothness (local variation in radius lengths)
       細胞核邊緣平滑度：半徑長度的局部變異性。如果邊緣起伏很大、不規則，平滑度數值就會下降。
    E. fractal dimension ("coastline approximation" - 1)
       分形維數（碎形維度）：它用來評估細胞核邊緣的複雜度與粗糙度。數值越高，代表邊緣結構越呈現複雜的自相似微小鋸齒狀。

    大小（Radius）、顏色（Texture）、平滑度（Smoothness）、凹陷數量（Concave points）、邊緣粗糙度（Fractal Dimension），五種不同維度，排除重複因子。

    Accuracy of full dataset with picked factors : {model.score(_5factors, y):.2f}
""", end=SKIP_ONE_LINE)


# 3. Split 30% data for testing.
XTrain, XTest, yTrain, yTest = tts(X, y, test_size=0.30, random_state=10)
model = LogisticRegression(max_iter=3000)
model.fit(XTrain, yTrain)
print(f"3. Accuracy of 7:3 dataset: {
      model.score(XTest, yTest):.2f}", end=SKIP_ONE_LINE)

# 4. Measure min/max accuracy of test size.
print("Finding min/max accuracy from different test size ...")
accuracy = []
for ts in range(1, 100):
    testSize = ts/100
    XTrain, XTest, yTrain, yTest = tts(
        X, y, test_size=testSize, random_state=10)
    model = LogisticRegression(max_iter=5000)
    model.fit(XTrain, yTrain)
    score = model.score(XTest, yTest)
    accuracy.append(score)
    print(f"\tAccuracy of {testSize} dataset: {score:.2f}")

aMin = min(accuracy)
iMin = accuracy.index(aMin)+1
aMax = max(accuracy)
iMax = accuracy.index(aMax)+1
print(f"3. Accuracy: min = {aMin:.2f} (testSize={
      iMin/100}), max = {aMax:.2f} (testSize={iMax/100})")
