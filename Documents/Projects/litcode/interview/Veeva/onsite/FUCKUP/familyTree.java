import java.util.*;
class familyTree{

    public static Boolean isRelated(Node left, Node right){
        
        if(left == null || right == null){
            return false;
        }

        // System.out.println(left.name +" "+ right.name);
        
        if(left.equals(right)){
            return true;
        }
        
        return (isRelated(left.Mom, right.Mom) || 
        isRelated(left.Dad, right.Dad) || 
        isRelated(left.Mom, right.Dad) || 
        isRelated(left.Dad, right.Dad));
    }

    public static void main(String[] args){
        // Node Emma = new Node("Emma");
        // Node Kate = new Node("Kate");
        // Node Jerry = new Node("Jerry");
        // Node Dylan = new Node("Dylan");
        // Node Nancy = new Node("Nancy");
        // Node Ryan = new Node("Ryan");
        // Node Bob = new Node("Bob");
        // Node Lisa = new Node("Lisa");
        Node Jerod = new Node("Jerod");
        Node Daniel = new Node("Jerod");
        // Node Juan = new Node("Juan");

        // Node Zenitsu = new Node("Zenitsu");

        // Jerod.setDad(Ryan);
        // Daniel.setDad(Ryan);
        // Juan.setDad(Bob);
        // Juan.setMom(Lisa);

        // Ryan.setDad(Jerry);
        // Ryan.setMom(Kate);
        // Bob.setDad(Dylan);
        // Bob.setMom(Nancy);

        // Kate.setMom(Emma);
        // Dylan.setMom(Emma);

        // if(isRelated(Jerod, Daniel)){
        //     System.out.println("True");
        // }else{
        //     System.out.println("False");
        // }

        System.out.println(Jerod.equals(Daniel));

        HashMap<Node, String> book = new HashMap<>();

        book.put(Jerod, "Jerod");
        book.put(Daniel, "Daniel");

        System.out.println(book.get(Jerod));
    }
}