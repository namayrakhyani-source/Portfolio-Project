import pygame

pygame.init()

WIDTH = 1200
HEIGHT = 766

screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption('ball game')

bg_image = pygame.image.load('assets/bg.jpg')


divider = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

player_speed = 5
ball_speed = 5

score_font = pygame.font.SysFont('consolas, couriernew, monospace', 30)

fps = 60
clock = pygame.time.Clock()



'''
player Class()
'''
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, controls, side):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (100,150))
        self.rect = self.image.get_rect(topleft = (x,y))
        self.controls = controls
        self.side = side
        self.score = 0





    def movement(self, keys):
        if keys[self.controls['left']]:
            self.rect.x = self.rect.x - player_speed
        if keys[self.controls['right']]:
             self.rect.x = self.rect.x + player_speed
        if keys[self.controls['up']]:
             self.rect.y = self.rect.y - player_speed
        if keys[self.controls['down']]:
             self.rect.y = self.rect.y + player_speed


        self.rect.top = max(0, self.rect.top)
        self.rect.bottom = min(HEIGHT, self.rect.bottom)
        if self.side == 'left':
            self.rect.left = max(0, self.rect.left)
            self.rect.right = min(divider.left, self.rect.right)
        else:
            self.rect.left = max(divider.right, self.rect.left)
            self.rect.right = min(WIDTH, self.rect.right)

player_1 = Player(100, 200, 'assets/character_1.png', 
                  {'left': pygame.K_a, 'right': pygame.K_d, 'up': pygame.K_w, 'down': pygame.K_s}, "left")

player_2 = Player(1100, 200, 'assets/charecter_2.png',
                  {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'up': pygame.K_UP, 'down': pygame.K_DOWN}, "right" )

players = pygame.sprite.Group()
players.add(player_1, player_2)




def display():
    screen.fill('blue')
    screen.blit(bg_image, (0,0))

   
    player_1_text = score_font.render(f'Player 1: {player_1.score}', True, 'green')
    
    screen.blit(player_1_text, (30,30))

    player_2_text = score_font.render(f'Player 2: {player_2.score}', True, 'green')
    screen.blit(player_2_text, (950, 30))

    players.draw(screen)
    
    pygame.draw.rect(screen, 'white', divider)
    
    pygame.display.update()

def main():
    is_running = True
    while is_running:
        clock.tick(fps)
        display()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
                is_running = False

        keys = pygame.key.get_pressed()

        player_1.movement(keys)
        player_2.movement(keys)
    

    pygame.quit()

main()