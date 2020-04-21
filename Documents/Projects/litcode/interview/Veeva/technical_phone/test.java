import java.util.*;

class test{
    public static void testing(String t){
        System.out.println(t);
    }

    public static void main(String[] args){

        // testing("shit");

        ArrayList<String> a = new ArrayList<>();
        a.add("fuck");
        ArrayList<String> b = new ArrayList<>();
        b.add("shit");

        System.out.println(Arrays.toString(a.toArray()));
        System.out.println(Arrays.toString(b.toArray()));


    }
}