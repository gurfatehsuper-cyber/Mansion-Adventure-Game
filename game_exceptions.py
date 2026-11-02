"""
Custom exceptions for the text-based adventure game.
Includes exceptions for invalid room searches and invalid moves.
By evolving the game, more custom exceptions can be added as needed.
"""
class InvalidRoomError(Exception):
    """
    Raised when the user searches for a room that does not exist.
    """
    def __init__(self, room_name):
        self.message = f"There is no room named '{room_name}'"
        super().__init__(self.message)
        
        
class InvalidMoveError(Exception):
    """
    Raised when the user attempts to move to a room that is not connected.
    """
    def __init__(self, current_room, target_room):
        self.message = f"You cannot move directly from {current_room} to {target_room}."
        super().__init__(self.message)
