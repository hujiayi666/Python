import random
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# 模拟单个小球在高尔顿插板中的下落过程
def ball_drop(probability):
    position = 0
    for _ in range(10):  # 假设插板有10行钉子
        if random.random() < probability:
            position += 1
        else:
            position -= 1
    return position


# 模拟多个小球的下落并统计落入每个槽的小球数量
def galton_board_simulation(num_balls, probability):
    slots = [0] * 21  # 假设插板底部有21个槽，位置范围从 -10 到 10
    for _ in range(num_balls):
        final_position = ball_drop(probability)
        slot_index = final_position + 10
        slots[slot_index] += 1
    return slots


# 更新并绘制小球在各槽的分布情况
def update_and_plot():
    num_balls = int(num_balls_entry.get())
    probability = float(probability_entry.get())

    slots = galton_board_simulation(num_balls, probability)

    ax.clear()
    ax.bar(range(-10, 11), slots)
    ax.set_xlabel('Slot Position')
    ax.set_ylabel('Number of Balls')
    ax.set_title('Galton Board Simulation')

    canvas.draw()


root = tk.Tk()
root.title("Galton Board Simulator")

# 小球数量输入框及标签
num_balls_label = ttk.Label(root, text="Number of Balls:")
num_balls_label.pack()
num_balls_entry = ttk.Entry(root)
num_balls_entry.pack()

# 概率输入框及标签
probability_label = ttk.Label(root, text="Probability (left/right):")
probability_label.pack()
probability_entry = ttk.Entry(root)
probability_entry.pack()

# 模拟按钮
simulate_button = ttk.Button(root, text="Simulate", command=update_and_plot)
simulate_button.pack()

# 创建用于绘制图形的Figure和Axes
fig, ax = plt.subplots(figsize=(8, 6))

# 将Figure嵌入到Tkinter窗口中
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root.mainloop()