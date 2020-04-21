 /*
 Given a tile class, where each tile knows: 
 the tile to the east, north, west, and south, 
 along with whether it is a golden tile or not. 
 Tiles are laid out in a large square (of unknown size), 
 and there is only 1 golden tile. 
 You start at one tile within the square (unknown) 
 and need to find a path to the 
 golden tile (list directions of east/south/north/west, in order).  
 */

// +---+---+
// |00 |01 |
// +---+---+
import java.util.Arrays;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Vector;

class goldenTile{

    public static void prints(String s){
        System.out.println(s);
    }

    public static void printQueue(Vector<tile> q){
        for(int index = 0; index < q.size(); index++) {
            System.out.print(q.get(index).getTileId());
            System.out.print(" ");
        }
        System.out.println();
    }

    // shit code
    public static ArrayList<String> DFS(String move, tile node, ArrayList<String> directions, HashMap<tile, Boolean> visited){
        // System.out.println("======");
        // System.out.println(move);
        // node.printTileId();

        visited.put(node, true);
        if(!move.equals("start")){
            directions.add(move);
        }

        if(node.golden == true){
            return directions;

        }

        if(node.east!=null){
            if(!visited.containsKey(node.east)){
                // System.out.println("east~");
                return DFS("east", node.east, directions, visited);
            }
        }

        if(node.south!=null){
            if(!visited.containsKey(node.south)){
                // System.out.println("south~");
                return DFS("south", node.south, directions, visited);
            }
        }

        if(node.north!=null){
            if(!visited.containsKey(node.north)){
                // System.out.println("north~");
                return DFS("north", node.north, directions, visited);
            }
        }


        if(node.west!=null){
            if(!visited.containsKey(node.west)){
                // System.out.println("west~");
                return DFS("west", node.west, directions, visited);
            }
        }

        return directions;

    }

    public static ArrayList<String> BFS(String move, tile node){
        Vector<tile> q = new Vector<>();
        HashMap<tile, Boolean> visited = new HashMap<>();
        HashMap<tile, ArrayList<String>> directions = new HashMap<>();
        ArrayList<String> before;

        visited.put(node, true);
        q.add(node);
        directions.put(node, new ArrayList<String>());

        tile t;

        while(!q.isEmpty()){
            t = q.firstElement();   // get first
            q.remove(0);            // pop

            // prints("=======x");
            // t.printTileId();
            // prints("=======x");

            if(t.golden){
                // prints("golden found");
                return directions.get(t);
            }

            // iterate all reachables
            if(t.east!=null){
                // prints("eastpass");
                if(!visited.containsKey(t.east.getTileId())){
                    // prints("east~");
                    // t.east.printTileId();
                    visited.put(t.east, true);
                    before = new ArrayList<>(directions.get(t));
                    before.add("east");
                    directions.put(t.east, before);
                    q.add(t.getEast());
                    // prints("queued east");
                }
            }

            if(t.south!=null){
                // prints("southpass");
                if(!visited.containsKey(t.south.getTileId())){
                    // prints("south~");
                    // t.south.printTileId();
                    visited.put(t.south, true);
                    before = new ArrayList<>(directions.get(t));
                    before.add("south");
                    directions.put(t.south, before);
                    q.add(t.getSouth());
                    // prints("queued south");
                }
            }

            if(t.north!=null){
                // prints("northpass");
                if(!visited.containsKey(t.north.getTileId())){
                    // prints("north~");
                    // t.north.printTileId();
                    visited.put(t.north, true);
                    before = new ArrayList<>(directions.get(t));
                    before.add("north");
                    directions.put(t.north, before);
                    q.add(t.getNorth());
                    // prints("queued north");
                }
            }


            if(t.west!=null){
                if(!visited.containsKey(t.west.getTileId())){
                    // prints("west~");
                    // t.west.printTileId();
                    visited.put(t.west, true);
                    before = new ArrayList<>(directions.get(t));
                    before.add("west");
                    directions.put(t.west, before);
                    q.add(t.getWest());
                    // prints("queued west");
                }
            }

            // printQueue(q);

        }

        return directions.get(node);
    }

    public static ArrayList<String> findGold(tile start){
        
        ArrayList<String> directions = new ArrayList<String>();
        HashMap<tile, Boolean> visited = new HashMap<>();

        if (start.golden == true){
            return directions;
        }

        // return DFS("start", start, directions, visited);
        return BFS("start", start);

    }

    public static void main(String[] args){
        /*
        +---+---+---+
        |00 |01 |02 |
        +---+---+---+
        |10 |11 |12 |
        +---+---+---+
        |20 |21 |22 |
        +---+---+---+
        */
 
        tile t_00 = new tile(true, "00");
        tile t_01 = new tile(false, "01");
        tile t_02 = new tile(false, "02");
        tile t_10 = new tile(false, "10");
        tile t_11 = new tile(false, "11");
        tile t_12 = new tile(false, "12");
        tile t_20 = new tile(false, "20");
        tile t_21 = new tile(false, "21");
        tile t_22 = new tile(false, "22");

        t_22.makeNorth(t_12);
        t_22.makeWest(t_21);

        t_21.makeNorth(t_11);
        t_21.makeWest(t_20);
        t_21.makeEast(t_22);

        t_20.makeNorth(t_10);
        t_20.makeEast(t_21);

        t_12.makeNorth(t_02);
        t_12.makeSouth(t_22);
        t_12.makeWest(t_11);

        t_11.makeNorth(t_01);
        t_11.makeWest(t_10);
        t_11.makeEast(t_12);
        t_11.makeSouth(t_21);

        t_10.makeNorth(t_00);
        t_10.makeSouth(t_20);
        t_10.makeEast(t_11);

        t_02.makeWest(t_01);
        t_02.makeSouth(t_12);

        t_01.makeWest(t_00);
        t_01.makeEast(t_02);
        t_01.makeSouth(t_11);

        t_00.makeEast(t_01);
        t_00.makeSouth(t_10);

        /*
        +---+---+---+
        |00 |01 |02 |
        +---+---+---+
        |10 |11 |12 |
        +---+---+---+
        |20 |21 |22 |
        +---+---+---+
        */

        /*
        +---+---+---+
        |00S|01 |02 |
        +---+---+---+
        |10 |   |12 |
        +---+---+---+
        |20 |   |22G|
        +---+---+---+
        */

        
        ArrayList<String> res = findGold(t_22);
        System.out.println(Arrays.toString(res.toArray()));
        
    }
 }