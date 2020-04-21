/*
Design a Phone System API 

-store phone numbers
-requests a specific number  


getRandomNumber()
    -give a new number(randomly) 

showAllUsedNumbers()

showAllUnusedNumbers()

*/
import java.util.HashMap;
import java.util.Random;
import java.util.ArrayList;
import java.util.List;

class telephone{

    public static void print_used_numbers(HashMap<String, Boolean> Phone_System){
        for(String number: Phone_System.keySet()){
            if(Phone_System.get(number)){
                String key = number.toString();
                Boolean value = Phone_System.get(number);
                System.out.println(key + ": " + value);
            }
        }
    }

    public static void print_unused_numbers(HashMap<String, Boolean> Phone_System){
        for(String number: Phone_System.keySet()){
            if(!Phone_System.get(number)){
                String key = number.toString();
                Boolean value = Phone_System.get(number);
                System.out.println(key + ": " + value);
            }
        }
    }

    public static void print_random_number(HashMap<String, Boolean> Phone_System){
        List<String> keysAsArray = new ArrayList<String>(Phone_System.keySet());
        Random r = new Random();
        prints(keysAsArray.get(r.nextInt(keysAsArray.size())));
    }

    public static void prints(String s){
        System.out.println(s);
    }

    // phone system put
    public static void add_entry(HashMap<String, Boolean> Phone_System, String number, Boolean status){
        Phone_System.put(number, status);
    }

    // phone system get
    public static Boolean get_entry(HashMap<String, Boolean> Phone_System, String number){
        return Phone_System.get(number);
    }

    // phone system delete
    public static void delete_entry(HashMap<String, Boolean> Phone_System, String number){
        Phone_System.remove(number);
    }

    // use a number in phone system
    public static void use(HashMap<String, Boolean> Phone_System, String number){
        Phone_System.put(number, true);
    }

    public static void main(String[] args){
        // phone system hashmap
        HashMap<String, Boolean> Phone_System= new HashMap<>();

        add_entry(Phone_System, "415-000-0001", false);
        add_entry(Phone_System, "415-000-0002", false);
        add_entry(Phone_System, "415-000-0003", false);
        add_entry(Phone_System, "415-000-0004", false);
        add_entry(Phone_System, "415-000-0005", false);
        add_entry(Phone_System, "415-000-0006", false);
        add_entry(Phone_System, "415-000-0007", false);
        add_entry(Phone_System, "415-000-0008", false);
        add_entry(Phone_System, "415-000-0009", false);
        add_entry(Phone_System, "415-000-0010", false);

        use(Phone_System, "415-000-0001");
        use(Phone_System, "415-000-0002");

        prints("=====used numbers=====");
        print_used_numbers(Phone_System);
        prints("=====unused numbers=====");
        print_unused_numbers(Phone_System);

        prints("=====random number=====");
        print_random_number(Phone_System);
    }
}

