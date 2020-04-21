import java.util.*;

class test{
    public static void main(String[] args){

        char[] freq = new char[26];
        String str = "abcdef";
        // for(int i = 0; i < str.length(); i++){
        //     freq[str.charAt(i)-'a']++;
        // }

        char[] test = {'a', 'b'};
        String s = new String(test);
        System.out.println(s);
        System.out.println(Arrays.toString(freq));
    }
}