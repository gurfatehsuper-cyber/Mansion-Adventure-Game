"""
Room class represents a room in a text-based adventure game.
It keeps track of the room's name, description, connected rooms, and whether it has been visited.
We will add more attributes and methods as needed to support game functionality.
"""
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connected_rooms = []
        self.visited = False

    def connect_room(self, room):
        """Connect this room to another room in both directions."""
        if room not in self.connected_rooms:
            self.connected_rooms.append(room)
        if self not in room.connected_rooms:
            room.connected_rooms.append(self)

    def get_connected_room(self, room_name):
        """Return a directly connected room matching room_name, or None."""
        target = room_name.strip().lower()
        for room in self.connected_rooms:
            if room.name.lower() == target:
                return room
        return None
