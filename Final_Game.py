#!python3
# coding=utf-8

import random
import os
from time import sleep

N = int(input())
spawn_prob = random.randrange(1, 10)/10
A = N*N
a = str(A)
sp = str(spawn_prob)
est = A*spawn_prob
estimate = str(est)
print("You will play with a board of " + a + " squares. The probability of a rabbit starting in each square is " + sp + ". On average you will begin the game with " + estimate + " rabbits. Let's see how it goes.")
sleep(5)
def should_be_alive(live_neighbors, i_am_alive):
        if i_am_alive:
                if live_neighbors < 2:
                        return False
                if live_neighbors > 3:
                        return False
                else:
                        return True

        else:
                if live_neighbors == 3:
                        return True
                else:
                        return False

def iterate(array):
        result = [x[:] for x in [[None]*N]*N]

        for i in range(len(array)):
                for j in range(len(array[i])):
                        live_neighbors = 0

                        for x in [-1, 0, 1]:
                                for y in [-1, 0, 1]:
                                        if x != 0 or y != 0:
                                                comparison_x = (i+x) % N
                                                comparison_y = (j+y) % N
                                                if array[comparison_x][comparison_y]:
                                                        live_neighbors = live_neighbors + 1
                        result[i][j] = should_be_alive(live_neighbors, array[i][j])
        return result

def draw(array):

        for row in array:
                for point in row:
                        if point:
                                print('🐇', end = '')
                        else:
                                print('🌱', end = '')
                print()

current = []
for i in range(N):
        current.append([])
        for j in range(N):
                if random.random() < spawn_prob:
                        current[i].append(False)
                else:
                        current[i].append(True)

while True:
        os.system('clear')
        draw(current)
        current = iterate(current)
        sleep(0.1)
