 /*
 Given a tile class, where each tile knows: 
 the tile to the east, north, west, and south, 
 along with whether it is a golden tile or not. 
 Tiles are laid out in a large square (of unknown size), 
 and there is only 1 golden tile. 
 You start at one tile within the sqare (unknown) 
 and need to find a path to the 
 golden tile (list directions of east/south/north/west, in order).  
 */
 import java.util.ArrayList;


 class tile{
     
    tile north;
    tile south;
    tile east;
    tile west;
    boolean golden;
    String id;
    
    tile(boolean G, String coord){
        north = null;
        south = null;
        east = null;
        west = null;
        golden = G;
        id = coord;
    }

    boolean isGoldenTile(tile T){
        if(T.golden == true){
            return true;
        }
        return false;
    }

    void printTileId(){
        System.out.println(id);
    }

    String getTileId(){
        return id;
    }

    tile getNorth(){
        return north;
    }

    tile getSouth(){
        return south;
    }

    tile getEast(){
        return east;
    }

    tile getWest(){
        return west;
    }

    void makeNorth(tile that){
        north = that;
    }

    void makeSouth(tile that){
        south = that;
    }

    void makeEast(tile that){
        east = that;
    }

    void makeWest(tile that){
        west = that;
    }

 }