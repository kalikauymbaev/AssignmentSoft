public class Room implements Prototype {
    // Existing Room code...
    @Override
    public Prototype clone() {
        // Deep clone the Room with its sides
        Room clonedRoom = new Room(this.roomNo);
        for (Direction direction : sides.keySet()) {
            clonedRoom.setSide(direction, sides.get(direction).clone());
        }
        return clonedRoom;
    }
}

public class Wall implements Prototype {
    // Existing Wall code...
    @Override
    public Prototype clone() {
        // Clone Wall
        return new Wall();
    }
}

public class DoorWall extends Wall {
    // Existing DoorWall code...
    @Override
    public Prototype clone() {
        // Clone DoorWall with references to the rooms it connects
        return new DoorWall(this.r1, this.r2);
    }
}
