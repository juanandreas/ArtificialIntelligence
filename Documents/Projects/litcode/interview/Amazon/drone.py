def altitude(cols, rows, M):

    dp = [[0 for i in range(cols)] for j in range(rows)]
    print(dp)

    for i in range(cols):
        for j in range(rows):
            if i==0 and j==0:
                dp[i][j] = 0
            
            else:
                dp[i][j] = min



    return 0

if __name__ == '__main__':

    mat1 = [
        [5,1],
        [4,5]
    ]
    rows1 = 2
    cols1 = 2

    print(altitude(rows1, cols1, mat1))

    mat2 = [
        [5,1,6],
        [4,5,8],
        [2,3,9]
    ]
    rows2 = 3
    cols2 = 3

    # print(altitude(rows2, cols2, mat2))