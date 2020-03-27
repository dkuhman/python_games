import pygame
import random
import math

pygame.init()  # Initialize game
game_screen = pygame.display.set_mode((700, 475))  # create the game screen
screen_height = 475
screen_width = 700
pygame.display.set_caption('TANKS!')
pygame.display.set_icon(pygame.image.load('tanks_logo.png'))  # Replace later - this looks bad

# Fonts for screen display
font = pygame.font.SysFont(None, 25)
large_font = pygame.font.SysFont(None, 80)

def text_objects(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def button(text, x, y, width, height, color, hover_color, action = None):
    global game_running
    pygame.draw.rect(game_screen, color, (x, y, width, height))  # Play button
    mouse_pos = pygame.mouse.get_pos()  # Gets the position of the mouse
    mouse_click = pygame.mouse.get_pressed()
    # Give hover effects to buttons
    if x + width > mouse_pos[0] > x and y + height > mouse_pos[1] > y:
        pygame.draw.rect(game_screen, hover_color, (x, y, width, height))
        if mouse_click[0] == 1 and action != None:
            if action == 'play':
                main_game_loop()
            elif action == 'home':
                intro_game()
            elif action == 'quit':
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(game_screen, color, (x, y, width, height))
    text_surf, text_rect = text_objects(text, font, (255, 255, 255))
    text_rect.center = ((x + (width / 2)), (y + (height / 2)))
    game_screen.blit(text_surf, text_rect)


def intro_game():
    while True:
        game_screen.blit(pygame.image.load('intro_screen.png'), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #Add buttons
        button('Play', 275, 200, 100, 50, (0,175,0), (0,255,0), 'play')
        button('Quit', 275, 300, 100, 50, (175,0,0), (255,0,0), 'quit')
        pygame.display.update()


def main_game_loop():
    game_clock = pygame.time.Clock()  # Creates a clock to control frame rate - will be important for velocity
    backgrounds = pygame.image.load('background_1.png')  # TODO: Add more later for new levels
    # DEFINE GAME OBJECTS AND ENVIRONMENT CONDITIONS
    # Player tank
    player_tank = pygame.transform.scale2x(pygame.image.load('tank.png'))  # Loads and resizes image to double initial size
    player_x = 100  # Initial player x position
    player_y = 390  # Initial player y position
    change_x = 0  # number of pixels moved per press
    # Coin
    coin_img = pygame.image.load('test coin.png')
    coin_x = random.randint(150, 600)
    coin_y = random.randint(100, 350)
    # Missile
    missile = pygame.image.load('missile.png')
    explosion = pygame.image.load('explosion.png')
    missile_x = 100
    missile_y = 390
    missile_vel_r = 2.5  # Defines the missile's resultant velocity
    launch_angle = 0  # Launch angle
    launch_angle_change = 0  # Change in launch angle based on up/down key press
    time_in_air = 0
    missile_state = 'ready'  # Ready state - missile cannot be seen
    explosion_state = 'off'  # Explosion cannot be seen
    explosion_time = 0  # We want the explosion to stay on the screen for 1-second
    # Environment conditions
    gravity = 0.981
    wind_resist = 0
    wind_assist = 0
    # User Score & ammo status
    user_score = 0
    user_ammo = 3

    # Define in-game functions
    def player(x, y):
        game_screen.blit(player_tank, (x, y))


    def coin_front(x, y):
        game_screen.blit(coin_img, (x, y))


    # TODO: Test the physics on this! I already changed the frame rate to 100 fps, so we have a time constant now
    def missile_fire(x, y):
        global missile_state
        missile_state = 'fire'
        game_screen.blit(missile, (x, y))
        return missile_state


    def collision(x1, y1, x2, y2):
        distance = math.sqrt((math.pow(x2 - x1, 2)) + (math.pow(y2 - y1, 2)))
        if distance < 27:
            return True
        else:
            return False


    # TODO: figure out how to keep explosive on the screen after the missile disappears
    def missile_explosion(x, y, show_time):
        global explosion_state
        explosion_state = 'on'
        if show_time > 0:
            game_screen.blit(explosion, (x, y))
            show_time -= 1


    def score_msg(msg, color):
        global font
        display_text = font.render(msg, True, color)
        game_screen.blit(display_text, (25, 25))


    # TODO: Add a message for ammo based on how many shots are left. Will need to add pictures
    def ammo_msg(msg, color):
        global font
        display_text = font.render(msg, True, color)
        game_screen.blit(display_text, (25, 50))


    def launch_angle_msg(msg, color):
        global font
        display_text = font.render(msg, True, color)
        game_screen.blit(display_text, (25, 75))


    #Game Loop
    while True:
        game_screen.fill((0, 0, 0))
        game_screen.blit(pygame.transform.scale(backgrounds, (700, 475)), (0, 0))  # Adds background image to screen and scales to fit
        game_clock.tick(100)  # Set frame rate to 100 fps

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_x = -0.35
                elif event.key == pygame.K_RIGHT:
                    change_x = 0.35
                elif event.key == pygame.K_UP:
                    launch_angle_change = 0.1
                elif event.key == pygame.K_DOWN:
                    launch_angle_change = -0.1
                elif event.key == pygame.K_SPACE:
                    if missile_state is 'ready':
                        missile_x = player_x  # This is to make sure the missile stays straight horizontal
                        missile_state = missile_fire(missile_x, missile_y)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    change_x = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    launch_angle_change = 0

        # Player Mechanics
        player_x = player_x + change_x
        if player_x < 0:  # Set left boundary
            player_x = 0
        if player_x > 637:  # Set right boundary
            player_x = 637

        # Missile Mechanics
        launch_angle = launch_angle + launch_angle_change
        if launch_angle < 0:  # Constrain launch angle to 0-90
            launch_angle = 0
        elif launch_angle > 90:
            launch_angle = 90

        if missile_state is 'fire':  # If a missile is fired
            time_in_air = time_in_air + 0.01
            launch_angle_rads = math.radians(launch_angle)
            missile_x += (math.cos(launch_angle_rads) * missile_vel_r) * time_in_air
            missile_y += (gravity * time_in_air + (math.sin(-launch_angle_rads) * missile_vel_r)) * time_in_air
            missile_state = missile_fire(missile_x, missile_y)
            # Collision detection
            collision_status = collision(coin_x, coin_y, missile_x, missile_y)
            if collision_status is True:
                # Update score
                user_score += 1
                # Update missile data
                missile_y = 390
                missile_x = 100
                time_in_air = 0
                missile_state = 'ready'
                # Add a new coin
                coin_x = random.randint(150, 630)
                coin_y = random.randint(100, 350)

            # End of current missile
            if missile_y < 0 or missile_y > player_y + 20 or missile_x > screen_width:
                # Show explosion
                if explosion_time == 0:
                    explosion_time = 100
                explosion_x = missile_x
                explosion_y = missile_y
                missile_explosion(explosion_x, explosion_y, explosion_time)
                # Reset parameters
                missile_state = 'ready'
                explosion_state = 'off'
                missile_y = 390
                missile_x = 100
                time_in_air = 0
                # Adjust Ammo
                user_ammo -= 1

        launch_angle_msg('Launch Angle: ' + str(round(launch_angle)), (255, 255, 255))
        score_msg('User score: ' + str(user_score), (255, 255, 255))
        ammo_msg('Ammo: ' + str(user_ammo), (255, 255, 255))
        player(player_x, player_y)  # Draws the player
        coin_front(coin_x, coin_y)  # Draws a coin

        if user_ammo == 0:
            # TODO: provide play again or quit buttons - make them hoverable
            end_game_loop()

        pygame.display.update()


def end_game_loop():
    while True:
        game_screen.blit(pygame.image.load('end_screen.png'), (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # Add buttons
        button('Play Again', 275, 200, 150, 50, (0, 175, 0), (0, 255, 0), 'play')
        button('Home Screen', 275, 275, 150, 50, (0, 0, 175), (0, 0, 255), 'home')
        button('Quit', 275, 350, 150, 50, (175, 0, 0), (255, 0, 0), 'quit')
        pygame.display.update()

#LAUNCH THE GAME!
intro_game()

