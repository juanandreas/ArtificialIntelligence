import java.util.*;

class hc{

    public static void main(String[] args){
        // String[] fuckveeva = {"b", "b", "b", "a", "a", "c", "d"};
        String[] fuckveeva = {"dog", "cat", "dog", "amsterdam", "hi", "bunny"};
        HashMap<Integer, Integer> freq = new HashMap<>();
        for(String s : fuckveeva){
            System.out.println(s+" : "+s.hashCode());
        }
        System.out.println("============");
        for(String s : fuckveeva){
            if(!freq.containsKey(s.hashCode())){
                freq.put(s.hashCode(), 1);
            }else{
                int fuck = freq.get(s.hashCode());
                // System.out.println(fuck+":"+s);
                freq.put(s.hashCode(), ++fuck);
            }
        }
        
        for(int i : freq.keySet()){
            System.out.println(i+" "+freq.get(i));
        }
        // System.out.println(ass.hashCode());
        // System.out.println(shit.hashCode());
    }
}