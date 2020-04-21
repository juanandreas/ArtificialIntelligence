class test{

    static class Calc{
        public int plus(int x){
            return x + 5;
        }

        public void printass(){
            System.out.println("ass");
        }
    }

    public static int plus(int x){
        return x + 2;
    }

    public static int plus(int x, int y){
        return x + y;
    }

    public static void main(String[] args){
        System.out.println(plus(2));
        System.out.println(plus(2,3));

        Calc c = new Calc();
        System.out.println(c.plus(2));
        c.printass();
    }
}