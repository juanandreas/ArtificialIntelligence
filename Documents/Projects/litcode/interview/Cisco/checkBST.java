class checkBST{

    private static class Node{
        int val;
        Node left = null;
        Node right = null;

        Node(int v){
            val = v;
        }
    }

    public static void preOrder(Node node){
        if(node == null){
            return;
        }
        System.out.print(node.val + " ");
        preOrder(node.left);
        preOrder(node.right);
    }

    public static Node sortedArrayToBST(int[] arr, int start, int end){
        if(start > end){
            return null;
        }
        
        int mid = (start+end)/2;

        Node top = new Node(arr[mid]);

        top.left = sortedArrayToBST(arr, start, mid-1);
        top.right = sortedArrayToBST(arr, mid+1, end);

        return top;
    }

    public static void isBST(Node t, int min, int max){


        System.out.println("True");
    }

    public static void main(String[] args){
        int[] arr = {1,2,3,4,5,6,7,8,9};
        
        Node tree = sortedArrayToBST(arr, 0, arr.length-1);
        preOrder(tree);

        isBST(tree, 0, 100);
    }
}