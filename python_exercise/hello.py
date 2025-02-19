import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("飞机")

# Colors
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

def draw_airplane(surface, x, y):
    # 机身
    pygame.draw.ellipse(surface, GRAY, (x, y, 120, 40))
    
    # 机头
    pygame.draw.polygon(surface, GRAY, [
        (x + 120, y + 20),  # 机头尖端
        (x + 100, y + 5),   # 上部
        (x + 100, y + 35)   # 下部
    ])
    
    # 机翼
    pygame.draw.polygon(surface, BLUE, [
        (x + 40, y + 20),   # 中心点
        (x + 70, y - 30),   # 左上
        (x + 90, y + 20),   # 右
        (x + 70, y + 70)    # 左下
    ])
    
    # 尾翼
    pygame.draw.polygon(surface, RED, [
        (x, y + 20),        # 中心点
        (x + 20, y - 10),   # 上
        (x + 30, y + 20),   # 右
        (x + 20, y + 50)    # 下
    ])

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 清空屏幕
    screen.fill(WHITE)
    
    # 在屏幕中央绘制飞机
    draw_airplane(screen, screen_width//2 - 60, screen_height//2 - 20)
    
    # 更新显示
    pygame.display.flip()

pygame.quit()