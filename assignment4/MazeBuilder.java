public interface MazeBuilder {
    void buildRoom(int roomNo);
    void buildDoor(int roomFrom, int roomTo);
    Maze getMaze();
}
