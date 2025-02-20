import pygame
import random

# 初始化 Pygame
pygame.init()

# 定义常量
WIDTH = 300
HEIGHT = 600
BLOCK_SIZE = 30
COLUMNS = WIDTH // BLOCK_SIZE
ROWS = HEIGHT // BLOCK_SIZE

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

# 定义形状
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]]
]

COLORS = [CYAN, YELLOW, MAGENTA, GREEN, RED, BLUE, ORANGE]

# 创建游戏窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("俄罗斯方块")

# 时钟对象，用于控制帧率
clock = pygame.time.Clock()

# 初始化游戏板
board = [[0] * COLUMNS for _ in range(ROWS)]

# 定义方块类
class Block:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = random.choice(COLORS)

    def move_down(self):
        self.y += 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def rotate(self):
        self.shape = list(map(list, zip(*self.shape[::-1])))

    def draw(self):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[0])):
                if self.shape[i][j] == 1:
                    pygame.draw.rect(screen, self.color, (
                        (self.x + j) * BLOCK_SIZE, (self.y + i) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

# 创建新方块
def new_block():
    shape = random.choice(SHAPES)
    return Block(COLUMNS // 2 - len(shape[0]) // 2, 0, shape)

# 检查碰撞
def check_collision(block, board):
    for i in range(len(block.shape)):
        for j in range(len(block.shape[0])):
            if block.shape[i][j] == 1:
                if block.y + i >= ROWS or block.x + j < 0 or block.x + j >= COLUMNS or board[block.y + i][block.x + j] == 1:
                    return True
    return False

# 合并方块到游戏板
def merge_block(block, board):
    for i in range(len(block.shape)):
        for j in range(len(block.shape[0])):
            if block.shape[i][j] == 1:
                board[block.y + i][block.x + j] = 1

# 检查并清除满行
def check_lines(board):
    full_lines = []
    for i in range(ROWS):
        if all(board[i]):
            full_lines.append(i)
    for line in full_lines:
        del board[line]
        board = [[0] * COLUMNS] + board
    return board

# 主游戏循环
current_block = new_block()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                new_block = Block(current_block.x - 1, current_block.y, current_block.shape)
                if not check_collision(new_block, board):
                    current_block.move_left()
            elif event.key == pygame.K_RIGHT:
                new_block = Block(current_block.x + 1, current_block.y, current_block.shape)
                if not check_collision(new_block, board):
                    current_block.move_right()
            elif event.key == pygame.K_DOWN:
                new_block = Block(current_block.x, current_block.y + 1, current_block.shape)
                if not check_collision(new_block, board):
                    current_block.move_down()
            elif event.key == pygame.K_UP:
                new_shape = list(map(list, zip(*current_block.shape[::-1])))
                new_block = Block(current_block.x, current_block.y, new_shape)
                if not check_collision(new_block, board):
                    current_block.rotate()

    # 自动下落
    new_block = Block(current_block.x, current_block.y + 1, current_block.shape)
    if not check_collision(new_block, board):
        current_block.move_down()
    else:
        merge_block(current_block, board)
        board = check_lines(board)
        current_block = new_block()
        if check_collision(current_block, board):
            running = False

    # 绘制背景
    screen.fill(BLACK)

    # 绘制游戏板
    for i in range(ROWS):
        for j in range(COLUMNS):
            if board[i][j] == 1:
                pygame.draw.rect(screen, WHITE, (j * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    # 绘制当前方块
    current_block.draw()

    # 更新显示
    pygame.display.flip()
pip
    # 控制帧率
    clock.tick(3)

# 退出 Pygame
pygame.quit()
