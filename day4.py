import os
import copy

def score(board):
    sum = 0
    for row in board:
        for item in row:
            if item != 'x':
                sum += item
    return sum

def bingo(board):
    win = False
    sum = 0
    board_length = len(board[0])
    for row in board:
        for item in row:
            if item != 'x':
                sum = 0
                break
            sum += 1
            if sum == board_length:
                return True, score(board)
    sum = 0
    for i in range(len(board)):
        if board[i][i] != 'x':
            sum = 0
            break
        sum += 1
        if sum == board_length:
            return True, score(board)
    sum = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[j][i] != 'x':
                sum = 0
                break
            sum += 1
            if sum == board_length:
                return True, score(board)
    return False, 0
    
def update_boards(boards, num):
    indexes = []
    won = False
    high_score = 0
    for i in range(len(boards)):
        for j in range(len(boards[0])):
            for k in range(len(boards[0][0])):
                if boards[i][j][k] == num:
                    boards[i][j][k] = 'x'
        win, score = bingo(boards[i])
        if win: 
            indexes.append(i)
            won = True
            if score > high_score: high_score = score
    return won, high_score, indexes


with open(os.path.join('inputs','day4.txt')) as file:
    numbers = [int(item) for item in file.readline().strip().split(',')]
    empty = file.readline()
    bingo_boards = []
    board = []
    for line in file:
        if line.strip() == '':
            bingo_boards.append(board)
            board = []
        else:
            board.append([int(item) for item in line.split()])
    #print(type(numbers))
    times_ran = 0
    for num in numbers:
        times_ran += 1
        win, final_score, indexes = update_boards(bingo_boards, num)
        if win:
            if len(bingo_boards) == 1:
                print('Final_score: ', final_score*num)
                exit()
            new_boards = copy.deepcopy(bingo_boards)
            [new_boards.remove(bingo_boards[idx]) for idx in indexes]
            bingo_boards = new_boards

    #print(bingo_boards)
    print(times_ran, len(numbers))