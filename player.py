"""
Player class represents a player in a text-based adventure game.
It keeps track of the player's name, current room, and visited rooms.
Provides methods to look around, move between rooms, and display status.
This class will be updated as the game evolves to include more features and interactions.
"""
from game_exceptions import InvalidMoveError
from room import Room
from mission import MissionQueue

class Player:
    def __init__(self, name: str, starting_room: Room) -> None:
        self.name = name
        self.current_room = starting_room
        self.visited_rooms = [starting_room]
        self.movement_history: list[Room] = [] # New attribute to track movement history for the Go Back feature. LAB 09 Part 1
        self.missions = MissionQueue() # New attribute to manage the player's missions. LAB 09 Part 2

    def look(self) -> None:
        """Display information about the player's current room."""
        print(f"\nCurrent Room: {self.current_room.name}")
        print(self.current_room.description)
        print("\nConnected rooms:")

        if self.current_room.connected_rooms:
            for room in self.current_room.connected_rooms:
                print(f"- {room.name}")
        else:
            print("- None")

    def move(self, room_name: str) -> None:
        """Move to a directly connected room or raise InvalidMoveError."""
        next_room = self.current_room.get_connected_room(room_name)
        if next_room is None:
            raise InvalidMoveError(self.current_room.name, room_name)        
        # After this check, next_room is guaranteed to be a valid connected room.
        # We need to record the current room in the movement history before moving to the next room.
                
        # ===================================================================
        # New code for Lab_09, PART 1
        # Append the current room to the movement history stack.
        # ===================================================================
        self.movement_history.append(self.current_room) 
        
        self.current_room = next_room
        if next_room not in self.visited_rooms:
            self.visited_rooms.append(next_room)
        print(f"You moved to {next_room.name}.")


        
    # ===================================================================
    # New code for Lab_09, PART 1
    # Implement the go_back method to return to the previous room.
    # ===================================================================   
    
    def go_back(self) -> None:
        """Return to the most recent room in the movement history stack."""
        if not self.movement_history:
            print("No previous room to return to.")
            return

        self.current_room = self.movement_history.pop()
        print(f"You returned to {self.current_room.name}.")

    # ===================================================================   

    def show_status(self) -> None:
        print("\n================ PLAYER STATUS ================")
        print(f"Player: {self.name}")
        print(f"Current Room: {self.current_room.name}")
        print(f"Rooms Visited: {len(self.visited_rooms)}")

    def show_visited_rooms(self) -> None:
        print("\nRooms Visited:")
        for index, room in enumerate(self.visited_rooms, start=1):
            print(f"{index}. {room.name}")