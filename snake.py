import pygame
import time
import random
from pygame.locals import *
import sys
import os


class Snake(object):
    def __init__(self, snake_block, snake_speed):
        self.snake_block = snake_block
        self.snake_speed = snake_speed
        self.snake_list = []
        self.snake_Head = []

    def our_snake(self):
        for x in self.snake_list:
            pygame.draw.rect(game.dis, snakeColor.bg, [
                x[0], x[1], self.snake_block, self.snake_block])


class Game(object):

    def __init__(self, dis_width, dis_height,  font_style, score_font):
        pygame.init()
        self.dis = pygame.display.set_mode(
            (dis_width, dis_height), pygame.HWSURFACE)
        self.dis_width = dis_width
        self.dis_height = dis_height
        self.bgStart = pygame.image.load('logo_small_512.png').convert()
        self.font_style = pygame.font.SysFont(font_style, 35)
        self.score_font = pygame.font.SysFont(score_font, 35)
        self.x1_change = 0
        self.y1_change = 0
        self.button = 0
        self.msgPos = -50
        self.Length_of_snake = 1
        self.clock = pygame.time.Clock()
        self.score = 0
        self.game_menu = True
        self.game_over = True
        self.game_close = False
        self.x1 = self.dis_width / 2
        self.y1 = self.dis_height / 2
        self.foodx = round(random.randrange(
            0, self.dis_width - snake.snake_block) / snake.snake_block) * snake.snake_block
        self.foody = round(random.randrange(0, self.dis_height -
                                            snake.snake_block) / snake.snake_block) * snake.snake_block

    def gameOver(self):
        self.dis.fill((0, 0, 0))
        self.dis.blit(self.bgStart, (80, 150))
        mesg = self.font_style.render("You Lost!", True, errorColor.color)
        self.dis.blit(mesg, [100, 100])
        mesg = self.font_style.render(
            "SCORE: " + str(self.score), True,  gameTextColor.color)
        self.dis.blit(mesg, [100, 130])

        pygame.mixer.music.set_volume(0.2)
        pygame.display.update()
        time.sleep(3)
        self.resetGame()

    def resetGame(self):
        self.x1_change = 0
        self.y1_change = 0
        self.Length_of_snake = 1
        self.score = 0
        self.clock = pygame.time.Clock()
        self.x1 = self.dis_width / 2
        self.y1 = self.dis_height / 2
        snake.snake_list = []
        snake.snake_Head = []
        self.game_over = False
        self.game_menu = True
        # self.newGame()

    def credits(self):
        pygame.mixer.music.fadeout(1000)
        self.dis.fill(gameTextColor.bg)
        mesg = self.font_style.render(
            "have a nice day", True, gameTextColor.color)
        self.dis.blit(mesg, [self.dis_width / 7, self.dis_height / 3])
        mesg = self.font_style.render(
            "don´t forget to visit www.dominikhaid.de", True, gameTextColor.color)
        self.dis.blit(mesg, [self.dis_width / 7, (self.dis_height / 3)+50])
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        quit()

    def mainMenu(self):
        msg = "Welcome to SNAKE GAME"
        color = gameTextColor.color
        self.dis.fill((0, 0, 0))
        self.dis.blit(self.bgStart, (80, 150))
        headtop = 100

        while self.msgPos <= 100:
            self.dis.fill((0, 0, 0))
            self.dis.blit(self.bgStart, (80, 150))
            self.msgPos += 1
            mesg = self.font_style.render(msg, True, color)
            self.dis.blit(mesg, [self.msgPos,  headtop])
            pygame.display.update()
            time.sleep(0.003)
        else:
            mesg = self.font_style.render(msg, True, color)
            self.dis.blit(mesg, [self.msgPos,  headtop])

        if self.button == 0:
            msg = "[ START ]"
            button = self.font_style.render(msg, True, activeTextColor.color)
            self.dis.blit(
                button, [100,  headtop+30])
            msg = "QUIT"
            button = self.font_style.render(msg, True, gameTextColor.color)
            self.dis.blit(
                button, [250, headtop+30])
            pygame.display.update()
        else:
            msg = "START"
            button = self.font_style.render(msg, True, gameTextColor.color)
            self.dis.blit(
                button, [100, headtop+30])
            msg = "[ QUIT ]"
            button = self.font_style.render(msg, True, activeTextColor.color)
            self.dis.blit(
                button, [250, headtop+30])
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.button > 0:
                        self.button -= 1
                    else:
                        self.button = 0
                elif event.key == pygame.K_RIGHT:
                    if self.button < 2:
                        self.button += 1
                    else:
                        self.button = 1
                elif event.key == pygame.K_RETURN:
                    if self.button == 0:
                        self.game_over = False
                        self.game_menu = False
                    else:
                        self.game_close = True
                        self.game_menu = False

    def newGame(self):
        self.dis.fill(boardColor.color)
        pygame.mixer.music.set_volume(0.3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.x1_change = -snake.snake_block
                    self.y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    self.x1_change = snake.snake_block
                    self.y1_change = 0
                elif event.key == pygame.K_UP:
                    self.y1_change = -snake.snake_block
                    self.x1_change = 0
                elif event.key == pygame.K_DOWN:
                    self.y1_change = snake.snake_block
                    self.x1_change = 0
        if self.x1 >= self.dis_width or self.x1 < 0 or self.y1 >= self.dis_height or self.y1 < 0:
            self.game_over = True
            # self.gameOver()

        self.x1 += self.x1_change
        self.y1 += self.y1_change
        self.dis.fill(boardColor.bg)
        pygame.draw.rect(self.dis, fruitsColor.color, [
            self.foodx, self.foody, snake.snake_block, snake.snake_block])
        snake.snake_Head = []
        snake.snake_Head.append(self.x1)
        snake.snake_Head.append(self.y1)
        snake.snake_list.append(snake.snake_Head)

        if len(snake.snake_list) > self.Length_of_snake:
            del snake.snake_list[0]

        if self.Length_of_snake > 2:
            for x in snake.snake_list[:-1]:
                if x == snake.snake_Head:
                    self.game_over = True
                    # self.gameOver()

        snake.our_snake()
        self.your_score(self.score)
        pygame.display.update()

        if self.x1 == self.foodx and self.y1 == self.foody:
            self.foodx = round(random.randrange(
                0, self.dis_width - snake.snake_block) / snake.snake_block) * snake.snake_block
            self.foody = round(random.randrange(
                0, self.dis_height - snake.snake_block) / snake.snake_block) * snake.snake_block
            self.Length_of_snake += 1
            self.score += 1
        self.clock.tick(snake.snake_speed)

    def your_score(self, score):
        value = self.score_font.render(
            "SCORE: " + str(self.score), True, gameTextColor.color)
        self.dis.blit(value, [0, 0])

    def message(self, msg, color):
        mesg = self.font_style.render(msg, True, color)
        self.dis.blit(mesg, [self.dis_width / 6, self.dis_height / 3])


class Colors(object):

    def __init__(self, foreground, background):
        self.color = foreground
        self.bg = background

    def show(self):
        return self.color


# Setup Colors
boardColor = Colors((10, 10, 10), (10, 10, 10))
snakeColor = Colors((230, 230, 230,), (230, 230, 230))
errorColor = Colors((180, 0, 0), (80, 0, 0))
fruitsColor = Colors((210, 111, 28), (0, 80, 0))
gameTextColor = Colors((230, 230, 230), (10, 10, 18))
activeTextColor = Colors((210, 111, 28), (10, 10, 10))


# Setup Snakes
snake = Snake(20, 15)


# Setup Games
game = Game(640, 680, "cascadiacode", "comicsansms")

# Plays six times, not five!
pygame.mixer.music.load('Night-Life-2-short-version.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(5)


def gameState():

    while game.game_menu == True and game.game_close == False:
        game.mainMenu()

    while game.game_over == False and game.game_close == False:
        game.newGame()

    while game.game_over == True and game.game_close == False:
        game.gameOver()


while game.game_close == False:
    gameState()
else:
    game.credits()
