import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */

        int rule1 = 3;
        int rule2 = 5;

        for(int i = 1; i <= 100; i++){

            String output = "";

            if(i % rule1 == 0){output += "Fizz";}
            if(i % rule2 == 0){output += "Buzz";}
            
            
            if(output == ""){
                System.out.println(i);
            }else{
                System.out.println(output);
            }
        }
    }
}