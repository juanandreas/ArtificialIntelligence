import java.util.*;

class groupAnagrams{

    public static List<List<String>> groupAnagrams(String[] strs) {
        
        HashMap<String, ArrayList<String>> map = new HashMap<String, ArrayList<String>>();

        for(String str : strs){
            char[] freq = new char[26];
            for(int i = 0; i < str.length(); i++){
                freq[str.charAt(i)-'a']++;
            }

            String key = new String(freq);
            if(!map.containsKey(key)){
                ArrayList<String> start = new ArrayList<>();
                start.add(str);
                map.put(key, start);
            }else{
                map.get(key).add(str);
            }
        }

        List<List<String>> result = new ArrayList<List<String>>(map.values());
        for(List<String> temp : result){
            System.out.println(Arrays.toString(temp.toArray()));
        }
        return map.values();
    }

    public static void main(String[] args){
        String[] W = {"apple", "banana", "pplea", "nanaba", "pear", "reap", "leppa", "prae", "naaban"};
        groupAnagrams(W);

    }
}