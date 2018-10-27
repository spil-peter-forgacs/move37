import pygame
from pygame.locals import *
import sys
import random

class FlappyBird:
    def __init__(self):
        self.bird = pygame.Rect(65, 50, 50, 50)
        self.distance = 0
        self.gap = 145
        self.wallx = 400
        self.birdY = 350
        self.jump = 0
        self.jumpSpeed = 15
        self.gravity = 10
        self.dead = False
        self.counter = 0
        self.offset = random.randint(-200, 200)

    def calculateInput(self):
        dist_X_to_The_Wall = self.wallx+80
        dist_Y_to_The_Wall_UP = self.birdY-(0 - self.gap - self.offset+500)
        dist_Y_to_The_Wall_DOWN = self.birdY-(360 + self.gap - self.offset)
        dist_Y_TOP = self.birdY
        dist_Y_BOTTOM = 720-self.birdY
        res = [dist_X_to_The_Wall,dist_Y_to_The_Wall_UP,dist_Y_to_The_Wall_DOWN,dist_Y_TOP,dist_Y_BOTTOM]
        return res

    def centerWalls(self):
        return 0 - self.gap - self.offset+572.5

    def downWall(self):
        return 360 + self.gap - self.offset

    def posBird(self):
        return self.birdY

    def isDead(self):
        return self.dead

    def TotalDistance(self):
        return self.distance


    def updateWalls(self):
        self.wallx -= 4
        if self.wallx < -80:
            self.wallx = 400
            self.counter += 1
            self.offset = random.randint(-200, 200)

    def birdUpdate(self):
        self.distance =  self.distance + 1 
        if self.jump:
            self.jumpSpeed -= 1
            self.birdY -= self.jumpSpeed
            self.jump -= 1
        else:
            self.birdY += self.gravity
            self.gravity += 0.2
        self.bird[1] = self.birdY
        upRect = pygame.Rect(self.wallx,
                             360 + self.gap - self.offset + 10,
                             88,
                             500)
        downRect = pygame.Rect(self.wallx,
                               0 - self.gap - self.offset - 10,
                               88,
                               500)
        if upRect.colliderect(self.bird):
            self.dead = True
        if downRect.colliderect(self.bird):
            self.dead = True
        if not 0 < self.bird[1] < 720:
            self.dead=True


    def tick(self,jump):
        if (jump==True) and not self.dead:
            self.jump = 17
            self.gravity = 10
            self.jumpSpeed = 15

        self.updateWalls()
        self.birdUpdate()


import neat

number_generations = 1000
def eval_genomes(genomes,config):
    for genome_id, genome in genomes:
        genome.fitness = 99999
        net = neat.nn.FeedForwardNetwork.create(genome,config)
        bird = FlappyBird()
        while (not bird.isDead() and not bird.TotalDistance()>110000):
            nnInput = bird.calculateInput()
            #print(nnInput)
            #print(bird.fitness())
            output = net.activate(nnInput)
            if output[0] > output[1]:
                bird.tick(True)
            else:
                bird.tick(False)

        genome.fitness = bird.TotalDistance()

config = neat.Config(neat.DefaultGenome,neat.DefaultReproduction,neat.DefaultSpeciesSet,neat.DefaultStagnation,'FlapyBirdNEAT')
p = neat.Population(config)
p.add_reporter(neat.StdOutReporter(False))
winner = p.run(eval_genomes,number_generations)
