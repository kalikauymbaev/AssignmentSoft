public class MazeDirector {
    private MazeBuilder builder;

    public MazeDirector(MazeBuilder builder) {
        this.builder = builder;
    }

    public void construct() {
        builder.buildRoom(1);
        builder.buildRoom(2);
        builder.buildDoor(1, 2);
        // More rooms and doors can be added here
    }

    public Maze getMaze() {
        return builder.getMaze();
    }
}
