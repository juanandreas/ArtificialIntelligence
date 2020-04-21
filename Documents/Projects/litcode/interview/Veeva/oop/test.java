class test{
    public static void equalTest(String A, String B){
        /*

        1)  Main difference between .equals() method and == operator is that one is method and other is operator.
        
        2)  We can use == operators for reference comparison (address comparison) 
            and .equals() method for content comparison. 
            In simple words, == checks if both objects point to the same memory location whereas 
            .equals() evaluates to the comparison of values in the objects.
        
        3)  If a class does not override the equals method,
            then by default it uses equals(Object o) method 
            of the closest parent class that has overridden this method. 
        
        */
        if(A == B){
            System.out.println("==: True");
        }else{
            System.out.println("==: False");
        }

        if(A.equals(B)){
            System.out.println(".equals(): True");
        }else{
            System.out.println(".equals(): False");
        }
    }

    public static void main(String[] args){
        // String A = new String("HELLO"); 
        // String B = new String("HELLO"); 
        // equalTest(A, B);

        food ass = new tuna();
        ass.eat();
        ass.yuck();
    }
}