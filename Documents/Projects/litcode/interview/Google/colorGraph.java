import java.util.*;

class colorGraph{

    public static int DFS(Boolean[][] memo, int x_start, int y_start, String[][] graph, int max_color_nums){
        // down, up, left, right
        int dx[] = {0,0,-1,1};
        int dy[] = {1,-1,0,0};
        String color = graph[x_start][y_start];
        
        // System.out.println(x_start+" "+y_start);

        for(int m = 0; m < 4; m++){
            int x_move = dx[m];
            int y_move = dy[m];

            // if same color, count
            try{
                if(graph[x_start+x_move][y_start+y_move] == color){
                    if(memo[x_start+x_move][y_start+y_move] == null){
                        max_color_nums++;
                        memo[x_start+x_move][y_start+y_move] = true;
                        max_color_nums = DFS(memo, x_start+x_move, y_start+y_move, graph, max_color_nums);
                    }
                }
            }catch(Exception e){
                // System.out.println("out of bounds, but it's ok!");
            }finally{
                continue;
            }
        }

        return max_color_nums;
    }

    public static void main(String[] args){

        String graph[][] = {
            {"B", "B", "W", "R"},
            {"B", "W", "R", "W"},
            {"W", "W", "W", "W"},
            {"W", "R", "R", "R"},
            {"W", "W", "W", "W"},
        };
        // String graph[][] = {
        //     {"B", "B", "W"}, 
        //     {"B", "W", "R"},
        //     {"B", "W", "B"}
        // };
        int r = 5;
        int col = 4;

        // up, down, left, right
        int dx[] = {0,0,-1,1};
        int dy[] = {1,-1,0,0};

        int max_color_nums = 0;
        String max_color = "";
        int temp;

        Boolean memo[][] = new Boolean[r][col];
        for(int i = 0; i < r; i++){

            for(int j = 0; j < col; j++){
                
                if(memo[i][j] == null){
                    memo[i][j] = true;
                    temp = DFS(memo, i, j, graph, 1);
                    System.out.println(temp);
                    if(temp > max_color_nums){
                        System.out.println(temp+" ??? "+max_color_nums);
                        max_color = graph[i][j];
                        max_color_nums = temp;
                    }
                }

            }
        }

        System.out.println(max_color);
    }
}