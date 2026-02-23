import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# 加载数据
data = pd.read_csv(r"C:\Users\hujia\Downloads\housing.csv")
X = data[['RM']]
y = data['MEDV']

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建和训练模型
model = LinearRegression()
model.fit(X_train, y_train)

# 预测和评估
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print('均方误差:', mse)
print('R²:', r2)

# 可视化结果
plt.figure(figsize=(8,6))
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted')
plt.xlabel('Number of rooms')
plt.ylabel('Median house price')
plt.title('Linear Regression Predicting House Prices')
plt.legend()

# 保存图像到本地
plt.savefig(r"C:\Users\hujia\Downloads\linear_regression_result.png", dpi=300, bbox_inches='tight')

# 显示图像
plt.show()
