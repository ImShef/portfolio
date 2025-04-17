import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
# загрузить данные
url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
data = pd.read_csv(url)
# вывести в консоль первые 5 строк таблицы с данными
print(data.head())
# разделение данных на признаки (X) и целевую переменную (y)
X = data.drop(columns = ["medv"])
y = data["medv"]
# разделение данных на две части: обучающую и тестовую
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size = 0.2, random_state = 42)
# создание модели по алгоритму линейной регрессии
model = LinearRegression()
# обучение модели на обучающей части данных
model.fit(X_train, y_train)
# использование обученной модели на тестовой части данных
y_pred = model.predict(X_test)
# оценка обученной модели
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Среднеквадратичная ошибка (MSE): {mse}")
print(f"Коэффициент детерминации (R^2): {r2}")
# визуализация результатов работы обученной модели
plt.scatter(y_test, y_pred)
plt.xlabel("Реальные значения")
plt.ylabel("Предсказанные значения")
plt.title("Реальные vs Предсказанные значения")
plt.show()