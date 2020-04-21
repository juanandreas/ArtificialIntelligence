/*
(Coding) Given two strings, figure out if they are anagrams 
(Kept asking for a better answer until a good linear solution was presented)
*/

import java.util.Arrays;

class anagram{
    
    public static boolean isAnagram(String s1, String s2){
        int[] freq = new int[26];

        for(int i = 0; i < s1.length(); i++){
            freq[s1.charAt(i) - 'a']++;
        }

        for(int i = 0; i < s2.length(); i++){
            freq[s2.charAt(i) - 'a']--;
            if(freq[s2.charAt(i) - 'a'] < 0){
                return false;
            }
        }

        System.out.println(Arrays.toString(freq));

        return true;

        
    }

    public static void main(String[] args){
        String s1 = "listen";
        String s2 = "silent";

        System.out.println((int)'a');

        System.out.println(isAnagram(s1, s2));
    }
}