class binarySearch{

    public static int binSearch(int[] arr, int l, int r, int target){
        if(l <= r){

            int m = (l + r)/2;

            if(arr[m] == target){
                return m;
            }
            if(target > arr[m]){
                return binSearch(arr, m+1, r, target);
            }
            if(target < arr[m]){
                return binSearch(arr, l, m-1, target);
            }
        }

        return -1;
    }


    public static void main(String[] args){
        int[] arr = {1,5,7,9,10,12,52,55,67,90};

        int target = 52;
        int location = binSearch(arr, 0, arr.length-1, target);

        System.out.println(location);

    }
}