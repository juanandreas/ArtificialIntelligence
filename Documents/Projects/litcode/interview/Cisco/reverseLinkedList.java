class reverseLinkedList{

    private static class Node{
        public int val;
        public Node next = null;

        public Node(int v){
            val = v;
        }
    }

    public static void printL(Node n){
        while(n != null){
            System.out.print(n.val);
            if(n.next == null){
                System.out.println("/");
            }else{
                System.out.print("->");
            }
            n = n.next;
        }
    }

    public static Node reverse(Node n){
        Node left = n;
        Node right = n.next;
        left.next = null;`
        while(right != null){
            Node temp = right.next;
            right.next = left;
            left = right;
            right = temp;
        }

        return left;
    }

    public static void main(String[] args){
        
        Node one = new Node(1);
        Node two = new Node(2);
        Node three = new Node(3);

        one.next = two;
        two.next = three;

        printL(one);
        printL(reverse(one));

    }

}