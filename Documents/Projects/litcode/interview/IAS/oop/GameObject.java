public abstract class GameObject{
    public abstract void talk();

    public static void main(String[] args){
        Player player = new Player();
        player.talk();

        Enemy enemy = new Enemy();
        enemy.talk();
    }
}