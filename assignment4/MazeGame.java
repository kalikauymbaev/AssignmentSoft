public class MazeGame {
    // public static void main(String[] argv) {
    //     StandardMazeBuilder builder = new StandardMazeBuilder();
    //     MazeDirector director = new MazeDirector(builder);
    //     director.construct();
    //     Maze maze = director.getMaze();
    // }


    private PrototypeRegistry registry;

    public MazeGame(PrototypeRegistry registry) {
        this.registry = registry;
    }

    public Maze createMaze() {
        Maze aMaze = new Maze();
        Room r1 = (Room)registry.getPrototype("Room");
        Room r2 = (Room)registry.getPrototype("Room");
        DoorWall d = (DoorWall)registry.getPrototype("DoorWall");
        
        aMaze.addRoom(r1);
        aMaze.addRoom(r2);
        
        // ... setup the sides for rooms using registry prototypes ...
        
        return aMaze;
    }
    
    public static void main(String [] argv) {
        PrototypeRegistry registry = new PrototypeRegistry();
        registry.addPrototype("Room", new Room(0));
        registry.addPrototype("Wall", new Wall());
        registry.addPrototype("DoorWall", new DoorWall(null, null)); // Room references will be set later
        
        MazeGame game = new MazeGame(registry);
        game.createMaze();
    }
}
