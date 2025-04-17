import turtle
import random

# Настройка экрана
screen = turtle.Screen()
screen.bgcolor("black")  # Черный фон для красоты
screen.title("С Днем Святого Валентина!")  # Заголовок окна

# Настройка черепашки
heart_turtle = turtle.Turtle()
heart_turtle.shape("turtle")
heart_turtle.speed(0)  # Максимальная скорость
heart_turtle.hideturtle()  # Скрываем черепашку

# Цвета для сердечек
colors = ["red", "pink", "magenta", "purple", "orange", "yellow"]

# Функция для рисования одного сердечка
def draw_heart(x, y, size, color):
    heart_turtle.penup()
    heart_turtle.goto(x, y)
    heart_turtle.pendown()
    heart_turtle.color(color)
    heart_turtle.begin_fill()
    heart_turtle.left(50)
    heart_turtle.forward(size)
    heart_turtle.circle(size / 2, 200)
    heart_turtle.right(140)
    heart_turtle.circle(size / 2, 200)
    heart_turtle.forward(size)
    heart_turtle.end_fill()
    heart_turtle.setheading(0)  # Возвращаем черепашку в исходное положение

# Функция для написания поздравления
def write_congratulations():
    heart_turtle.penup()
    heart_turtle.goto(0, -200)  # Перемещаем черепашку вниз
    heart_turtle.color("white")
    heart_turtle.write("С Днем Святого Валентина!", align="center", font=("Arial", 30, "bold"))

# Рисуем много сердечек
for _ in range(50):  # Количество сердечек
    x = random.randint(-300, 300)  # Случайная координата X
    y = random.randint(-200, 200)  # Случайная координата Y
    size = random.randint(20, 50)  # Случайный размер сердечка
    color = random.choice(colors)  # Случайный цвет
    draw_heart(x, y, size, color)

# Пишем поздравление
write_congratulations()

# Завершение
turtle.done()