#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 01:16:01 2020

Easy level Sudoku solver

Algorithm: Backtracking

Procedure:
    1. Pick an empty square
    2. Try all number from 1 to 9 inclusively
    3. Find 1 that works
    4. Repeat the process
    5. Backtrack

Base on: TechWithTim's tutorial
"""
# Print out the full sudoku board
def print_board(brd):
    for i in range(len(brd)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")
            
        for j in range(len(brd[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")
                
            if j == 8:
                print(brd[i][j])
            else:
                print(str(brd[i][j]) + " ", end = "")
                

# Pick an empty square
def find_emp(brd):
    for i in range(len(brd)):
        for j in range(len(brd[0])):
            if brd[i][j] == 0:
                return (i, j)
            
    return None
         
# Find valid number
def isValid(brd, num, pos):
    # Check row
    for i in range(len(brd[0])):
        if brd[pos[0]][i] == num and pos[1] != i:
            return False
            
    # Check column
    for i in range(len(brd)):
        if brd[i][pos[1]] == num and pos[0] != i:
            return False
        
    # Check box
    boxX = pos[1] // 3
    boxY = pos[0] // 3
    
    for i in range(boxY * 3, boxY * 3 + 3):
        for j in range(boxX * 3, boxX * 3 + 3):
            if brd[i][j] == num and (i, j) != pos:
                return False
            
    return True

# Backtrack
def solved(brd):
    find = find_emp(brd)
    
    if not find:
        return True           
    else:
        row, col = find
        
    for i in range(1, 10):
        if isValid(brd, i, (row, col)):
            brd[row][col] = i
            
            if solved(brd):
                return True
            
            brd[row][col] = 0
            
    return False

# Test the program
if __name__ == '__main__':
    '''
    # Board found in page 13
    board = [
                [7, 8, 0, 2, 0, 4, 0, 6, 0],
                [0, 2, 0, 5, 8, 0, 0, 0, 0],
                [0, 0, 0, 3, 7, 0, 1, 0, 0],
                [0, 1, 2, 0, 6, 0, 0, 4, 8],
                [0, 9, 5, 8, 0, 3, 6, 1, 0],
                [8, 7, 0, 0, 4, 0, 2, 9, 0],
                [0, 0, 1, 0, 5, 2, 0, 0, 0],
                [0, 0, 0, 0, 9, 8, 0, 5, 0],
                [0, 5, 0, 7, 0, 1, 0, 2, 9]
            ]
    
    '''
    
    # Board found in page 35
    board = [
                [0, 0, 6, 0, 7, 0, 0, 3, 8],
                [0, 0, 2, 4, 0, 0, 9, 0, 1],
                [0, 0, 0, 1, 6, 3, 7, 2, 4],
                [8, 0, 0, 3, 0, 0, 2, 5, 0],
                [1, 0, 3, 0, 2, 0, 4, 0, 7],
                [0, 2, 7, 0, 0, 4, 0, 0, 3],
                [2, 6, 5, 7, 3, 1, 0, 0, 0],
                [7, 0, 8, 0, 0, 2, 6, 0, 0],
                [9, 4, 0, 0, 8, 0, 3, 0, 0]
            ]
    
    print("Puzzle:")
    print_board(board)
    solved(board)
    print("_________________________________")
    print("Solution:")
    print_board(board)          