import java.util.HashMap; 
import java.util.Map; 
import java.util.Arrays; 
import java.util.ArrayList; 


class movies{

    public static void findMovies(int flightTime, int[] Netflix){
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < Netflix.length; i++){
            map.put(Netflix[i], i);
        }

        int targetTime = flightTime - 30;
        int[] res= new int[2];

        Arrays.sort(Netflix);

        for(int i = Netflix.length-1; i >= 0; i--){
            if(map.containsKey(targetTime-Netflix[i])){
                res[0] = map.get(targetTime-Netflix[i]);
                res[1] = map.get(Netflix[i]);
            }else{
                map.put(Netflix[i], i);
            }
        }
        
        System.out.print(res[0]);
        System.out.print(", ");
        System.out.println(res[1]);
    }

    public static void main(String args[]){
        
        int F1 = 110;
        int[] N1 = {20, 70, 90, 30, 60, 100};
        findMovies(F1, N1);

        int F2 = 250;
        int[] N2 = {100, 180, 40, 120, 10};
        findMovies(F2, N2);
    }
}