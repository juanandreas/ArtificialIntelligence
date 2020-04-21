import java.util.Arrays; 
import java.util.stream.IntStream;


class twosum{

    public static void sumsToTarget(int[] arr, int k) {
        int[] res = new int[2];
        
        Arrays.sort(arr);
        for (int i = 0; i < arr.length; i++) {
            int siblingIndex = Arrays.binarySearch(arr, k-arr[i]);
            System.out.println(i +" "+siblingIndex);
            if (siblingIndex >= 0) { // Found it!
                /* If this points at us, then the pair exists only if
                * there is another copy of the element. Look ahead of
                * us and behind us.
                */

                if (siblingIndex != i){
                    System.out.println("pass");
                    res[0] = i;
                    res[1] = siblingIndex;
                    Arrays.toString(res);
                }
            }
        }
        Arrays.toString(res);;
    }

    public static void main(String args[]){
        
        int k = 6;
        int[] arr = {3,2,4};
        sumsToTarget(arr, k);
    }

}