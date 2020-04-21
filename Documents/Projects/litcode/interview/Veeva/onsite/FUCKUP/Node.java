class Node{
    Node Mom;
    Node Dad;
    Node Child;
    String name;

    Node(String s){
        Mom = null;
        Dad = null;
        name = s;
    }

    void setMom(Node m){
        Mom = m;
    }

    void setDad(Node d){
        Dad = d;
    }

    // @Override
    // public boolean equals(Object obj){
    //     Node that = (Node) obj;
    //     System.out.println("huh???");
    //     if(this.name == that.name){
    //         return true;
    //     }else{
    //         return false;
    //     }
    // }
}