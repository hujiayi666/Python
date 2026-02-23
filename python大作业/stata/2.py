import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm
import matplotlib.pyplot as plt

# ===============================
# 1️⃣ 读取数据
# ===============================
data = pd.read_csv(r"C:\Users\hujia\Downloads\housing.csv")
X = data[['RM']]
y = data['MEDV']

# ===============================
# 2️⃣ 拆分训练集与测试集
# ===============================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ===============================
# 3️⃣ sklearn 线性回归模型
# ===============================
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("====== sklearn 模型结果 ======")
print(f"均方误差 (MSE): {mse:.4f}")
print(f"决定系数 (R²): {r2:.4f}")
print(f"回归系数 (斜率): {model.coef_[0]:.4f}")
print(f"截距: {model.intercept_:.4f}")

# ===============================
# 4️⃣ statsmodels 回归（含 p 值）
# ===============================
X_train_sm = sm.add_constant(X_train)
ols_model = sm.OLS(y_train, X_train_sm).fit()

print("\n====== statsmodels 统计结果（含 p 值） ======")
print(ols_model.summary())

# ===============================
# 5️⃣ 可视化结果
# ===============================
plt.figure(figsize=(8,6))
plt.scatter(X_test, y_test, color='blue', label='实际值')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='预测值')
plt.xlabel('房间数（RM）')
plt.ylabel('房价中位数（MEDV）')
plt.title('线性回归预测房价')
plt.legend()

# 保存图像到本地
plt.savefig(r"C:\Users\hujia\Downloads\linear_regression_result1.png", dpi=300, bbox_inches='tight')

plt.show()
