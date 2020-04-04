import pygame
import os

pygame.init()

game_screen = pygame.display.set_mode((500, 600))
game_screen_width = 500
game_screen_height = 600
pygame.display.set_caption('Motor Adapt!')
font = pygame.font.SysFont('Arial', 25)

ball = pygame.image.load('ball.png')
ball_y = 500
ball_x = 200
ball_center = ball_y + 34
change_y = 0
ball_state = 'ready'

errors = []
toss_count = 0
feedback = 'inactive'

def ball_move(x,y):
    game_screen.blit(ball, (x, y))

def screen_msg(text,color,x,y):
    global font
    display_text = font.render(text, True, color)
    game_screen.blit(display_text, (x, y))

def text_objects(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()

def button(text, x, y, width, height, color, hover_color, action = None):
    global play_game
    pygame.draw.rect(game_screen, color, (x, y, width, height))  # Play button
    mouse_pos = pygame.mouse.get_pos()  # Gets the position of the mouse
    mouse_click = pygame.mouse.get_pressed()
    # Give hover effects to buttons
    if x + width > mouse_pos[0] > x and y + height > mouse_pos[1] > y:
        pygame.draw.rect(game_screen, hover_color, (x, y, width, height))
        if mouse_click[0] == 1 and action != None:
                if action == 'download':
                    # Save errors to .csv
                    export_error_data = (str(error) for error in errors)
                    export_error_data = ','.join(export_error_data) + '\n'
                    with open("ball_toss_error_data.csv", "w") as fp:
                        fp.write(export_error_data)
    else:
        pygame.draw.rect(game_screen, color, (x, y, width, height))
    text_surf, text_rect = text_objects(text, font, (255, 255, 255))
    text_rect.center = ((x + (width / 2)), (y + (height / 2)))
    game_screen.blit(text_surf, text_rect)

def end_game():
    while True:
        game_screen.blit(pygame.image.load('end_screen.png'), (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # Add buttons
        button('Download Data', 175, 300, 150, 60, (175, 0, 0), (255, 0, 0), 'download')
        filename = 'ball_toss_error_data.csv'
        if os.path.isfile(filename):
            screen_msg('Download Successful!', (0, 255, 0), 150, 400)
        pygame.display.update()


play_game = True
while play_game:
    game_screen.fill((0, 0, 0))
    pygame.draw.line(game_screen, (0, 255, 0), (0, 150), (500, 150),3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ball_state is 'ready':
                    ball_state = 'active'
                    toss_count += 1
                    if toss_count <= 50:
                        change_y = -1
                    elif 50 < toss_count <= 150:
                        change_y = -2
            elif event.key == pygame.K_f: #Toggles feedback of toss number and error
                if feedback is 'inactive':
                    feedback = 'active'
                elif feedback is 'active':
                    feedback = 'inactive'
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                if toss_count <= 50:
                    change_y = 1
                    release_height = ball_center
                    error = 150 - release_height
                    errors.append(error)
                elif 50 < toss_count <= 150:
                    change_y = 1
                    release_height = ball_center
                    error = 150 - release_height
                    errors.append(error)

    if ball_state is 'active':
        ball_y = ball_y + change_y
        ball_center = ball_y + 34
        if ball_y < 0:
            ball_y = 0
        elif ball_y > 500:
            ball_y = 500
            ball_state = 'ready'
            pygame.time.delay(200)

    ball_move(ball_x, ball_y)

    #Feedback
    if feedback is 'active':
        screen_msg('Toss number: ' + str(toss_count), (255, 255, 255), 25, 50)
        if not errors:
            screen_msg('Error: ',(255, 255, 255), 25, 75)
        else:
            screen_msg('Error: ' + str(errors[-1]),(255, 255, 255), 25, 75)

    #End game
    if toss_count == 150 and ball_y == 500:
        pygame.time.delay(1500)
        play_game = False

    pygame.display.update()

end_game()