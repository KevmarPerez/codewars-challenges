board = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]

def check_dup(ls):
    return sorted(ls) == list(range(1,10))

def done_or_not(board):
    # print("checking the row")
    rows = True
    columns = True
    new_board = [list(col) for col in list(zip(*board))]
    for row in board:
        if  not check_dup(row):
            rows = False
            break
        
    
    # print("checking the columns")
    for col in new_board:
        if  not check_dup(col):
            columns = False
            break
    
    return"Finished!" if rows and columns else 'Try again!'

print(done_or_not(board))