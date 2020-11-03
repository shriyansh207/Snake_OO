# importing the necessary libraries to run the game
import pygame
from pygame import mixer
import sys
import random
import time

# Two variables are globalised so they can be used throughout the game
global game_lost
global future


# A class is created for the object snake. This class holds all the methods and attributes of this object.
class Snake(object):

    # When initialising the snake, the snakes length is set to 1 grid square
    # The snakes position is set to the centre of the screen and it will start moving in a random direction
    # The snakes colour is set to purple, previous score is set to 0, and (current) score is set to 0.
    def __init__(self):
        self.length = 1
        self.position = [((window_width / 2), (window_height / 2))]
        self.direction = random.choice([up, down, left, right])
        self.colour = (128, 0, 128)
        self.prev_score = 0
        self.score = 0

    # This function will return the position of the snakes head from the list.
    def get_head_position(self):
        return self.position[0]

    # This function allows the snake to move in all 4 directions if the length is only 1 block.
    # But, if the length is greater than 1 then the snake is only able to move in 3 direction. It cant move back.
    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    # In this function we first get the current head position of the snake and the current direction it is travelling
    # by accessing the turn functions properties. Next, using the grid size and the screen height and width, we
    # calculate the new head position of the snake
    def move(self):
        current_pos = self.get_head_position()
        x, y = self.direction
        new_pos = (((current_pos[0] + (x*grid_size)) % window_width), (current_pos[1] + (y*grid_size)) % window_height)

        # if the length of the snake is greater than 2 and the snakes head intercepts any other part of the snake, the
        # game is ended.The snake is reset by calling the reset function. The global functions are called and game lost
        # is set to true. The future variable then holds the current time plus 6 seconds.
        # In the else statement, the new position of the snake is added to the beginning of the position list and the
        # last element is popped.
        if len(self.position) > 2 and new_pos in self.position[2:]:
            self.reset()
            global game_lost, future
            game_lost = True
            now = time.time()
            future = now + 6

        else:
            self.position.insert(0, new_pos)
            if len(self.position) > self.length:
                self.position.pop()

    # This function is used to reset the snake when the snake dies. A sound effect is called and played in this function
    # The previous score variable will now hold the score from the last game.The snakes length is also set back to 1.
    # The snake is put back in the centre of the screen and will stay in place, until arrow keys are pressed to move it
    # again. The snakes direction is put on hold. The current score 'self.score' is also reset to 0. Time.sleep
    # is called to freeze the game for 2 seconds.
    def reset(self):
        game_over_sound = mixer.Sound("Game_reset.wav")
        game_over_sound.play()
        self.prev_score = self.score
        self.length = 1
        self.position = [((window_width / 2), (window_height / 2))]
        self.direction = hold
        self.score = 0
        time.sleep(2)

    # This function draws the snake onto the screen surface. A block is drawn for each xy position of the snake using
    # the draw attribute from the pygame module.
    def display(self, surface):
        for p in self.position:
            r = pygame.Rect((p[0], p[1]), (grid_size, grid_size))
            pygame.draw.rect(surface, self.colour, r)
            pygame.draw.rect(surface, (93, 216, 228), r, 1)

    # This function checks for user interaction. If the user presses exit to quit the game. The pygame is exited and
    # the running program too with help from exit attribute from the sys module.
    def key_pressed(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # The game checks to see if the game_lost variable is false. If it is then game checks if the user has pressed
        # any of the arrow keys, if they have then the snake will move in that direction.
            elif not game_lost:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.turn(up)
                    elif event.key == pygame.K_DOWN:
                        self.turn(down)
                    elif event.key == pygame.K_LEFT:
                        self.turn(left)
                    elif event.key == pygame.K_RIGHT:
                        self.turn(right)

    
# A class is created for the object apple. This class holds all the methods and attributes of this object.
class Apples(object):

    # The apple(food) for the snake will have an x, y position and it will have a dark red colour.
    def __init__(self):
        self.position = (0, 0)
        self.colour = (220, 20, 60)
        self.random_position()

    # With the help of the random function, the apple is spawned into the game window at a random position.
    def random_position(self):
        self.position = (random.randint(1, int(grid_width - 2)) * grid_size, (random.randint(1, int(grid_height - 2))
                         * grid_size))

    # This function displays the apples onto the screen, using the draw attribute from the pygame library, the xy of the
    # apple is drawn onto the screen.
    def display(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (grid_size, grid_size))
        pygame.draw.rect(surface, self.colour, r)
        pygame.draw.rect(surface, (139, 0, 0), r, 1)


# This class is very similar to the apples class. This is the (poison/ bad apple) for the snake.
class GreenApple(object):

    # The green apple(poison) for the snake will have an x, y position and it will have a dark green colour.
    def __init__(self):
        self.position = (0, 0)
        self.colour = (0, 102, 0)
        self.random_position()

    # With the help of the random function, the apple is spawned into the game window at a random position.
    def random_position(self):
        self.position = (random.randint(1, int(grid_width - 2)) * grid_size, random.randint(1, int(grid_height - 2))
                         * grid_size)
        
    # This function displays the green apples onto the screen, using the draw attribute from the pygame library,
    # the xy of the green apple is drawn onto the screen.
    def display(self, surface):
        g = pygame.Rect((self.position[0], self.position[1]), (grid_size, grid_size))
        pygame.draw.rect(surface, self.colour, g)
        pygame.draw.rect(surface, (0, 102, 0), g, 1)
    

# A class is created for the object rocks. This class holds all the methods and attributes of this object.
class Rocks(object):

    # The base colour and position of the rocks is set in the initialise function
    def __init__(self):
        self.pos_list = []
        self.colour = (245, 245, 220)
        self.position()
        
    # This function finds the positions of rocks on the game screen. The position is found by finding the border of the
    # screen when a co-ordinate is found of the rock, it is added to a list of co-ordinates.
    def position(self):
        
        for x in range(0, int(grid_width)):
            if x == 0 or x == (grid_width-1): 
                for y in range(0, int(grid_height)):
                    co_ords = tuple([x * grid_size, y * grid_size])
                    self.pos_list.append(co_ords)

        for y in range(0, int(grid_height)):
            if y == 0 or y == (grid_height-1):
                for x in range(0, int(grid_width)):
                    co_ords = tuple([x * grid_size, y * grid_size])
                    self.pos_list.append(co_ords)

    # This draws the rocks onto the game screen. It takes all the coordinates from the coordinates list and draws it
    # onto the screen
    def draw(self, surface):
        for x, y in self.pos_list:
            w = pygame.Rect((x, y), (grid_size, grid_size))
            pygame.draw.rect(surface, (245, 245, 220), w)
     

# This function is responsible for drawing the background of the game. It takes the parameter surface.
# Multiple for loops are used to go through each grid square and alternate the colours between consecutive grid squares.
# These alternate coloured squares are then drawn onto the screen to form the background
def draw_background(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if(x + y) % 2 == 0:
                r = pygame.Rect((x*grid_size, y*grid_size), (grid_size, grid_size))
                pygame.draw.rect(surface, (135, 206, 250), r)
            else:
                r2 = pygame.Rect((x*grid_size, y*grid_size), (grid_size, grid_size))
                pygame.draw.rect(surface, (32, 178, 170), r2)


# The window width and height are set to 800 x 800 pixels.
window_height = 600
window_width = 600


# each grid is 20 x 20 pixels
# The window width and height are set to how many squares it holds on the row and column.
grid_size = 20
grid_width = window_width/grid_size
grid_height = window_height/grid_size

# The brackets represent the x and y. When moving horizontally, the x co-ordinates are affected
# When moving vertically, the y co=ordinates are affected. When on hold, the snake isn't moving.
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)
hold = (0, 0)


# This is the most crucial function. This function is what runs the whole code until the game is exited.
# The pygame window is initialised.
def main():
    pygame.init()

    # The game clock is initialised using the attribute in the pygame library called time.
    # The game screen is also initialised with set height and width. The game name is captioned as Snake
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Snake")

    # Surface contains the value of the screen size by using the Surface attribute from the pygame lib.
    # The surface is then converted and passed as a parameter when calling the draw background function.
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_background(surface)

    # The snake, apple rock and green apple classes are put into their respective variable names
    snake = Snake()
    apple = Apples()
    rocks = Rocks()
    green_apple = GreenApple()

    # Multiple fonts and sizes are set in variables.
    font = pygame.font.SysFont("comicsansms", 16)
    font_loser = pygame.font.SysFont("dejavuserif", 80)
    font_respawn = pygame.font.SysFont("comicsansms", 24)
    
    # The background music for the game is loaded and played. The music is set in loop so it will keep playing at all
    # times.
    mixer.music.load("background_music.mp3")
    mixer.music.play(-1)

    # Two sound effects are loaded and put into variables using the mixer library.
    points_sound = mixer.Sound("Score.wav")
    ouch_sound = mixer.Sound("ouch.wav")

    # Game_lost and future variables are globalised so they can be used outside the function.
    global game_lost
    global future

    # The game_lost variable is set as false and the now variable contains current time and the future variable contains
    # the current time + 6 seconds. The green_apple_spawn variable contains the current time plus 20 seconds.
    # These variables are needed in the main game loop below.
    game_lost = False
    now = time.time() 
    future = now + 6
    green_apple_spawn = now + 20

    # A while loop, that never ends is run, this is the main loop to run the game.
    while True:

        # If statement is used to check if the game is lost, if it is lost then the game displays the game over screen.
        # The game screen fills up the screen with the colour red, and displays information such as score on the screen.
        if game_lost:
            if time.time() < future:
                screen.fill((255, 51, 51))
                text_loser = font_loser.render("GAME OVER!", 1, (255, 255, 255))
                text_loser_message = font_respawn.render("Your snake will respawn in a couple seconds", 1, (0, 102, 0))
                text_loser_message1 = font_respawn.render("You can then play again", 1, (0, 102, 0))
                text_score = font.render("Last game you scored {0}".format(snake.prev_score), 1, (0, 0, 0))
                screen.blit(text_loser, (100, 240))
                screen.blit(text_loser_message, (80, 300))
                screen.blit(text_loser_message1, (80, 320))
                screen.blit(text_score, (80, 360))
                pygame.display.update()
                
        # This selection statement checks if current time is greater than the time inside the future variable, if it is
        # then the game_lost variable is set to false.
        if time.time() > future and game_lost:
            game_lost = False

        # This selection statement displays the green apple in a random location every 20 seconds and resets the clock
        # every time the apple is displayed in a new position.
        if time.time() > green_apple_spawn:
            green_apple.random_position()
            now = time.time()
            green_apple_spawn = now + 20

        # The game clock is set to 10ms, the key pressed function in the snake class is also called. Next the background
        # and rocks are drawn onto the screen. The move function in the snake class is then called.
        clock.tick(10)
        snake.key_pressed()
        draw_background(surface)
        rocks.draw(surface)
        snake.move()

        # A for loop is run that checks the rocks position list. if the snakes head and any one of the rocks overlap,
        # then the snake is reset by calling the reset function in the snake class. The now variable then holds the  
        # current time and the future variable holds the current time plus 5 seconds. Game_lost is also set to true.
        for i in rocks.pos_list:
            if i == snake.get_head_position():
                snake.reset()
                now = time.time()
                future = now + 5
                game_lost = True

        # An if statement checks the position of the snakes head and the apple displayed on the screen. If they overlap:
        # a sound effect is played, the length of the snake is increased by 1, the snake score is incremented by 10 and
        # another apple is displayed on the screen.
        if snake.get_head_position() == apple.position:
            points_sound.play()
            snake.length += 1
            snake.score += 10
            apple.random_position()

        # This selection statement checks if the snakes head position and the green apples position overlaps. Another if
        # statement checks the length of the snake. If the length of the snake is greater than 6, a sound effect is
        # played, the apple is spawned in a new location and the snakes length and score is decrement by 6 and 60
        # respectively. However if the snakes length is less than 6 when it eats the green apple, the snake is reset.
        # The now and future timers are also reset and the game_lost variable is set to true. The game is over.
        if snake.get_head_position() == green_apple.position:
            if snake.length > 6:
                ouch_sound.play()
                green_apple.random_position()
                snake.position = snake.position[:len(snake.position)-6]
                snake.length -= 6
                snake.score -= 60
                
            else:
                snake.reset()
                now = time.time()
                future = now + 5
                game_lost = True
                
        # The snake and apples are drawn onto the screen.
        snake.display(surface)
        apple.display(surface)
        green_apple.display(surface)

        # The following blocks of code prints different things onto the game screen. Text variables contain texts,
        # formatting and colour of the text. These texts are then displayed on the screen using screen.blit.
        screen.blit(surface, (0, 0))
        text = font.render("Current Score {0}".format(snake.score), 1, (0, 0, 0))
        text2 = font.render("Do not eat the Green apples!!!", 1, (255, 51, 51))
        text_prev_score = font.render("Last game you scored {0}".format(snake.prev_score), 1, (0, 0, 0))
        screen.blit(text, (5, 0))
        screen.blit(text2, (195, 0))
        screen.blit(text_prev_score, (5, 15))
        pygame.display.update()


# This calls the main function which then starts the whole game.
main()
