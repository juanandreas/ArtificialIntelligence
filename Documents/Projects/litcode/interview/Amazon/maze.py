def printMat(Maze):
    for r in Maze:
        print(r)
    print("================")

def isPath(Maze, row, col):
    # set arr[0][0] = 1 
    arr[0][0] = 1
  
    # Mark reachable (from top left)  
    # nodes in first row and first column.  
    for i in range(1, row): 
        if (arr[0][i] != -1): 
            arr[0][i] = arr[0][i - 1]
    printMat(Maze)
  
    for j in range(1, col): 
        if (arr[j][0] != -1): 
            arr[j][0] = arr[j - 1][0]
    printMat(Maze)
              
    # Mark reachable nodes in  
    # remaining matrix.  
    for i in range(1, row): 
        for j in range(1, col): 
            if (arr[i][j] != -1): 
                arr[i][j] = max(arr[i][j - 1],  
                                arr[i - 1][j]) 
    printMat(Maze)
                                  
    # return yes if right  
    # bottom index is 1 
    return (arr[row - 1][col - 1] == 1) 


if __name__ == '__main__':
    # Given array  
    arr =  [[ 0, 0, -1, -1, 0 ],  
            [-1, -1, 0, -1, -1],  
            [ 0, 0, 0, -1, 0 ],  
            [-1, 0, -1, 0, -1],  
            [ 0, 0, -1, 0, 0 ]]  
    row = 5
    col = 5
  
    # path from arr[0][0] to arr[row][col]  
    if (isPath(arr, row, col)): 
        print("Yes")  
    else: 
        print("No") 