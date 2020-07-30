# https://ko.wikipedia.org/wiki/%ED%83%84%EC%84%B1_%EC%B6%A9%EB%8F%8C
import pygame
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 750, 450
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("elastic collision")

clock = pygame.time.Clock()

#### class def ####
class Box:
    def __init__(self, img, velocity, mass):
        self.img = img
        self.v = velocity
        self.m = mass
        self.x, self.y = 0, 0
        self.width = self.height = img.get_rect().size[0]

    def get_pos(self):
        return round(self.x), round(self.y)

#### load image ####
box1_load = pygame.image.load("D:/sunrin/Python/elastic collision count/box1.png")
box2_load = pygame.image.load("D:/sunrin/Python/elastic collision count/box2.png")
box1_load = pygame.transform.scale(box1_load, (50, 50))
box2_load = pygame.transform.scale(box2_load, (170, 170))

#### global variable ####
digits = 2
timeSteps = 1
collision_count = 0
isRunning = True

#### font #### 
font_ = pygame.font.Font("D:/sunrin/Python/elastic collision count/NanumMyeongjo-Regular.ttf", 32) # (font-name, font-size)

#### create box ####
box1 = Box(box1_load, 0, 1)
box2 = Box(box2_load, -3 / timeSteps, 100**(digits - 1))

#### set start pos ####
box1.x, box1.y = 150, SCREEN_HEIGHT - box1.height
box2.x, box2.y = 350, SCREEN_HEIGHT - box2.height

start = False

while isRunning:

    deltaTime = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start = True

    if not start: continue

    for _ in range(timeSteps):
        # 벽과 충돌
        if box1.x <= 0:
            box1.v *= -1
            collision_count += 1
        # 박스끼리 충돌
        if box1.x + box1.width > box2.x:
            m1, m2 = box1.m, box2.m
            v1, v2 = box1.v, box2.v
            total_v1 = (v1 * (m1 - m2) + 2 * m2 * v2) / (m1 + m2)
            total_v2 = (v2 * (m2 - m1) + 2 * m1 * v1) / (m1 + m2)
            box1.v, box2.v = total_v1, total_v2
            collision_count += 1

        box1.x += box1.v
        box2.x += box2.v


    screen.fill((0, 0, 0))
    screen.blit(box1.img, box1.get_pos())
    screen.blit(box2.img, box2.get_pos())

    count_txt = font_.render('# ' + str(collision_count), True, (217, 220, 236))
    screen.blit(count_txt, (SCREEN_WIDTH -  count_txt.get_width() - 30, 20))

    pygame.display.update()

# print(box1_load.get_rect().size)
print("collisions :", collision_count)
pygame.quit()