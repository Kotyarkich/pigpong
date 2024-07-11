import pygame 
import time
window = pygame.display.set_mode((1024, 512))
score = 0
pygame.font.init()
font = pygame.font.SysFont("Arial", 32)

fps = pygame.time.Clock()



game = True 

def renderText(text):
       return font.render(text, True, (255, 200, 100))

dontwin = renderText("Вы проиграли!")
    

class platf:
    def __init__(self, y, x, width, length) -> None:
        self.hitbox = pygame.Rect(x, y, width, length)

    def move_1p(self):
        kl = pygame.key.get_pressed()
        if kl[pygame.K_w] == True:
            self.hitbox.y -= 2
        if kl[pygame.K_s] == True:
            self.hitbox.y += 2

        if self.hitbox.y > 320:
            self.hitbox.y = 320
        if self.hitbox.y < 64:
            self.hitbox.y = 64

    def move_2p(self):
        kl = pygame.key.get_pressed()
        if kl[pygame.K_UP] == True:
            self.hitbox.y -= 2
        if kl[pygame.K_DOWN] == True:
            self.hitbox.y += 2

        if self.hitbox.y > 320:
            self.hitbox.y = 320
        if self.hitbox.y < 64:
            self.hitbox.y = 64

    def collisions(self):
        if self.hitbox.colliderect(Ball.hitbox):
            print("connect")


class ball:
    def __init__(self, y, x, width, length, speed) -> None:
        self.hitbox = pygame.Rect(x, y, width, length)
        self.speed = speed
        self.direction_y = 1
        self.direction_x = 2.5

    def move_b():
        Ball.hitbox.y += Ball.speed * Ball.direction_y
        Ball.hitbox.x += Ball.speed * Ball.direction_x

        # Check if the ball reaches the top or bottom of the window
        if Ball.hitbox.y <= 0 or Ball.hitbox.y >= 512 - Ball.hitbox.height:
            Ball.direction_y = -Ball.direction_y  # Reverse the direction

        # Check for collisions with paddles
        if Ball.hitbox.colliderect(player.hitbox) or Ball.hitbox.colliderect(sharfi.hitbox):
            Ball.direction_x = -Ball.direction_x

player = platf(128, 64, 32, 128)
sharfi = platf(128, 896, 32, 128)
Ball = ball(224, 448, 32, 32, 2)
            

def reset():
    global score, player, sharfi, Ball

    player = platf(128, 64, 32, 128)

    sharfi = platf(128, 896, 32, 128)

    Ball = ball(224, 448, 32, 32, 2)

    score = 0


while game:
    window.fill("black")


    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            game = False

    player.move_1p()
    sharfi.move_2p()
    ball.move_b()
    pygame.draw.rect(window, "blue", (player.hitbox))  
    pygame.draw.rect(window, "red", (sharfi.hitbox))  
    pygame.draw.rect(window, "white", (Ball.hitbox))  
    def pigscoredef():
        global score
        if Ball.hitbox.colliderect(player.hitbox) or Ball.hitbox.colliderect(sharfi.hitbox):
            score += 1
    def imgs():
        if Ball.hitbox.x > 1024 or Ball.hitbox.x < 0:
            window.blit(dontwin, (400, 70))
            time.sleep(0.1)
            reset()
        pigscoreimg = renderText("Score: " + str(score))
        window.blit(pigscoreimg, (400, 5))

    
    pigscoredef()
    imgs()
        
    fps.tick(128)
    # print(player.hitbox)


    pygame.display.update()
