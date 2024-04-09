public class StandardMazeBuilder implements MazeBuilder {
    private Maze currentMaze;

    public StandardMazeBuilder() {
        currentMaze = new Maze();
    }

    public void buildRoom(int roomNo) {
        Room room = new Room(roomNo);
        currentMaze.addRoom(room);
        room.setSide(Direction.NORTH, new Wall());
        room.setSide(Direction.EAST, new Wall());
        room.setSide(Direction.SOUTH, new Wall());
        room.setSide(Direction.WEST, new Wall());
    }

    public void buildDoor(int roomFrom, int roomTo) {
        Room r1 = currentMaze.roomNo(roomFrom);
        Room r2 = currentMaze.roomNo(roomTo);
        DoorWall d = new DoorWall(r1, r2);

        r1.setSide(commonWall(r1, r2), d);
        r2.setSide(commonWall(r2, r1), d);
    }

    public Maze getMaze() {
        return currentMaze;
    }

    // Method to find the common wall between two rooms.
    private Direction commonWall(Room r1, Room r2) {
        // Logic to find the common wall direction
        return Direction.NORTH; // Placeholder
    }
}
