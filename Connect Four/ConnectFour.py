#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 08:34:03 2020

Connect Four

Tutorial from Keith Galli

"""
import numpy as np
import pygame
import sys
import math

# Constant colors
PINK = (255, 102, 178)
BLACK = (0, 0, 0)
GREEN = (0, 255, 128)
YELLOW = (255, 255, 102)

# Game board's constants
ROWS = 6
COLUMNS = 7

def createBoard():
    board = np.zeros((ROWS, COLUMNS))
    return board

def dropPiece(board, row, column, piece):
    board[row][column] = piece
    
def isValidLocation(board, column):
    return board[ROWS - 1][column] == 0

def getNextOpenRow(board, column):
    for row in range(ROWS):
        if board[row][column] == 0:
            return row

def printBoard(board):
    print(np.flip(board, 0))
    
def winningMove(board, piece):
    # Check all horizontal locations
    for column in range(COLUMNS - 3):
        for row in range(ROWS):
            if board[row][column] == piece and board[row][column + 1] == piece and board[row][column + 2] == piece and board[row][column + 3] == piece:
                return True
    
    # Check all vertical locations
    for column in range(COLUMNS):
        for row in range(ROWS - 3):
            if board[row][column] == piece and board[row + 1][column] == piece and board[row + 2][column] == piece and board[row + 3][column] == piece:
                return True
    
    # Check for positively sloped diaganols
    for column in range(COLUMNS - 3):
        for row in range(ROWS - 3):
            if board[row][column] == piece and board[row + 1][column + 1] == piece and board[row + 2][column + 2] == piece and board[row + 3][column + 3] == piece:
                return True
   
    # Check for positively sloped diaganols
    for column in range(COLUMNS - 3):
        for row in range(3, ROWS):
            if board[row][column] == piece and board[row - 1][column + 1] == piece and board[row - 2][column + 2] == piece and board[row - 3][column + 3] == piece:
                return True

# This is different from printBoard because it draw the board with the pygame graphics
def drawBoard(board):
    for column in range(COLUMNS):
        for row in range(ROWS):
            pygame.draw.rect(screen, PINK, (column * SQUARESIZE, row * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(column * SQUARESIZE + SQUARESIZE / 2), int(row * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), radius)
                
    for column in range(COLUMNS):
        for row in range(ROWS):
            if board[row][column] == 1:
                pygame.draw.circle(screen, GREEN, (int(column * SQUARESIZE + SQUARESIZE / 2), height - int(row * SQUARESIZE + SQUARESIZE / 2)), radius)
            elif board[row][column] == 2:
                pygame.draw.circle(screen, YELLOW, (int(column * SQUARESIZE + SQUARESIZE / 2), height - int(row * SQUARESIZE + SQUARESIZE / 2)), radius)
                
    pygame.display.update()        

# Main Game loop    
board = createBoard()
printBoard(board)
gameOver = False
turn = 0

pygame.init() # We need to do this in any pygame project

SQUARESIZE = 100

width = COLUMNS * SQUARESIZE
height = (ROWS + 1) * SQUARESIZE

size = (width, height)

radius = int(SQUARESIZE / 2 - 5)

screen = pygame.display.set_mode(size)
drawBoard(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            posX = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, GREEN, (posX, int(SQUARESIZE / 2)), radius)
            else:
                pygame.draw.circle(screen, YELLOW, (posX, int(SQUARESIZE / 2)), radius)
        
        pygame.display.update()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            
            # Player 1
            if turn == 0:
                posX = event.pos[0]
                column = int(math.floor(posX / SQUARESIZE))
                
                if isValidLocation(board, column):
                    row = getNextOpenRow(board, column)
                    dropPiece(board, row, column, 1)
                    
                    if winningMove(board, 1):
                        label = myfont.render("Player 1 Wins!!", 1, GREEN)
                        screen.blit(label, (40, 10))
                        gameOver = True
                        
            # Player 2            
            else:
                posX = event.pos[0]
                column = int(math.floor(posX / SQUARESIZE))
                
                if isValidLocation(board, column):
                    row = getNextOpenRow(board, column)
                    dropPiece(board, row, column, 2)
                    
                    if winningMove(board, 2):
                        label = myfont.render("Player 2 Wins!!", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        gameOver = True
            
            printBoard(board)
            drawBoard(board)
        
            turn += 1 # Update the turn
            turn %= 2
            
            if gameOver:
                pygame.time.wait(3000) # Right after the game is over, the game screen will wait for 3000ms before it automatically disappears