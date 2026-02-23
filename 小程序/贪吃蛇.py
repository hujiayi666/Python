import pygame
import time
import random

pygame.init()

# 设置屏幕尺寸和颜色
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 设置蛇和食物的大小
BLOCK_SIZE = 20

# 设置蛇的速度
SNAKE_SPEED = 15

# 初始化屏幕
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("贪吃蛇游戏")

# 初始化蛇的位置和初始长度
snake = [(WIDTH / 2, HEIGHT / 2)]
snake_length = 1

# 初始化蛇的移动方向
snake_direction = "RIGHT"

# 初始化食物的位置
food = (random.randrange(1, (WIDTH//BLOCK_SIZE)) * BLOCK_SIZE,
        random.randrange(1, (HEIGHT//BLOCK_SIZE)) * BLOCK_SIZE)

# 设置字体和字号
font = pygame.font.SysFont(None, 55)

# 定义绘制蛇的函数
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, WHITE, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

# 定义绘制食物的函数
def draw_food(food):
    pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))

# 主游戏循环
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 处理按键事件，改变蛇的方向
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"

    # 更新蛇的位置
    x, y = snake[0]
    if snake_direction == "UP":
        y -= BLOCK_SIZE
    elif snake_direction == "DOWN":
        y += BLOCK_SIZE
    elif snake_direction == "LEFT":
        x -= BLOCK_SIZE
    elif snake_direction == "RIGHT":
        x += BLOCK_SIZE

    # 检查是否吃到食物
    if x == food[0] and y == food[1]:
        food = (random.randrange(1, (WIDTH//BLOCK_SIZE)) * BLOCK_SIZE,
                random.randrange(1, (HEIGHT//BLOCK_SIZE)) * BLOCK_SIZE)
        snake_length += 1

    # 更新蛇的长度
    snake = [(x, y)] + snake[:snake_length-1]

    # 检查是否撞到墙或自己
    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or (x, y) in snake[1:]:
        running = False

    # 清空屏幕
    screen.fill(BLACK)

    # 绘制蛇和食物
    draw_snake(snake)
    draw_food(food)

    # 更新显示
    pygame.display.flip()

    # 控制游戏速度
    clock.tick(SNAKE_SPEED)

# 游戏结束时显示分数
score_text = font.render(f"Game Over! Your Score: {snake_length}", True, WHITE)
screen.blit(score_text, (WIDTH/2 - score_text.get_width()/2, HEIGHT/2 - score_text.get_height()/2))
pygame.display.flip()

# 等待几秒后退出游戏
time.sleep(3)

pygame.quit()