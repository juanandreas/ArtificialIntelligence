class drone{

    public static void printdp(int columnCount, int rowCount, int[][] dp){
        for(int i=0; i<rowCount; i++){
            System.out.print("[");
            for(int j=0; j<columnCount; j++){
                System.out.print(dp[i][j]);
                if(j < columnCount-1){
                    System.out.print(", ");
                }
            }
            System.out.println("]");
        }
        System.out.println(" ");
    }

    public static void maxOfMinAltitudes(int columnCount, int rowCount, int[][] mat){
        int[][] dp = new int[rowCount+1][columnCount+1];
        dp[0][0] = mat[0][0];

        for(int i=0; i<rowCount; i++){
            for(int j=0; j<columnCount; j++){
                if(i==0 && j==0){
                    dp[i][j] = mat[i][j];
                }
                else if(i==0){
                    dp[i][j] = Math.min(dp[i][j-1], mat[i][j]);
                }
                else if(j==0){
                    dp[i][j] = Math.min(dp[i-1][j], mat[i][j]);
                }
                else{
                    dp[i][j] = Math.min( Math.max(dp[i-1][j], dp[i][j-1]), mat[i][j]);
                }
            }
            printdp(rowCount, columnCount, dp);
        }

        System.out.println(dp[rowCount-1][columnCount-1]);
    }
    
    public static void findMaxAltitude(int rows, int cols, int[][] mat){



        System.out.println(0);
    }

    public static void main(String args[]){
        int rows1 = 2;
        int cols1 = 2;

        int[][] mat1 = {
            {1,1},
            {1,100}
        };

        // findMaxAltitude(rows1, cols1, mat1);

        maxOfMinAltitudes(rows1, cols1, mat1);

        int rows2 = 3;
        int cols2 = 3;

        int[][] mat2 = {
            {5,1,6},
            {5,4,8},
            {2,3,9}
        };

        // findMaxAltitude(rows2, cols2, mat2);

        maxOfMinAltitudes(rows2, cols2, mat2);
    }
}