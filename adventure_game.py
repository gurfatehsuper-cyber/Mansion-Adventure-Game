# CSC 1302L - Lab 06
# Name: Your Full Name
# Section: Your Lab Section
"""
Main module for the text-based adventure game.
Handles game setup, player interactions, and the main game loop.
To work correctly, this module requires the supporting classes and functions defined in room.py, player.py, item.py, game_utils.py, and game_exceptions.py.
Before running this module, ensure that this file is located in the root directory of the project and all supporting files are present in the same directory.
In VSCode, you can open root directory of the project by selecting "File" -> "Open Folder..." and choosing the project's root directory.
"""

import time
import random
from room import Room
from player import Player
from game_utils import (
    count_rooms, 
    find_room, 
    reset_visited,
    load_items,
    linear_search,
    binary_search,
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    )
from game_exceptions import InvalidRoomError, InvalidMoveError
from item import Item
from mission import Mission, MissionQueue

def create_missions(num_missions:int=5):
    missions = []
    with open("missions.txt", "r") as file:
        for line in file:
            missions.append(Mission(line.strip()))
    # return num_missions missions randomly selected from the list
    return random.sample(missions, num_missions)

def create_mansion():
    entrance = Room(
        "Entrance",
        "You are standing at the entrance of an old mansion."
    )
    hall = Room(
        "Hall",
        "A long hallway extends through the mansion."
    )
    library = Room(
        "Library",
        "You see shelves filled with dusty books."
    )
    storage = Room(
        "Storage",
        "Old boxes are stacked against the walls."
    )
    kitchen = Room(
        "Kitchen",
        "The kitchen looks abandoned and unusually quiet."
    )
    garden = Room(
        "Garden",
        "You are standing in a quiet garden behind the mansion."
    )

    entrance.connect_room(hall)    
    hall.connect_room(library)
    hall.connect_room(kitchen)    
    library.connect_room(storage)
    kitchen.connect_room(garden)

    return entrance

def display_menu():
    print("\n================== ADVENTURE GAME MENU ==================")
    print("1. Look around")
    print("2. Move to another room")
    print("3. Go back to the previous room")
    print("4. Player status")
    print("5. Show visited rooms")
    print("6. Search for a room")
    print("7. Count rooms")
    print("8. Search item catalog")
    print("9. Show current mission")
    print("10. Complete current mission")
    print("11. Show pending missions")
    print("12. Show completed missions")
    print("13. Add new mission")
    print("14. Exit")

def move_player(player: Player) -> None:
    print(f"\nYou are currently in: {player.current_room.name}")
    print("Connected rooms:")
    for room in player.current_room.connected_rooms:
        print(f"- {room.name}")
    destination = input("Enter room to move to: ").strip()
    player.move(destination)

def search_for_room(entrance: Room) -> None:
    target_name = input("Enter a room to search for: ").strip()

    reset_visited(entrance)
    result = find_room(entrance, target_name)
    reset_visited(entrance)

    if result is None:
        raise InvalidRoomError(target_name)

    print(f"Room found: {result.name}")
    print(result.description)

def show_room_count(entrance: Room) -> None:
    reset_visited(entrance)
    total = count_rooms(entrance)
    reset_visited(entrance)
    print(f"Total rooms: {total}")

def search_item_catalog(items, sorted_items):
    print("\n================ ITEM SEARCH ================")
    target_name = input("Enter item name: ").strip()

    start_time = time.perf_counter()
    linear_result, linear_comparisons = linear_search(items, target_name)
    linear_runtime = time.perf_counter() - start_time

    start_time = time.perf_counter()
    binary_result, binary_comparisons = binary_search(sorted_items, target_name)
    binary_runtime = time.perf_counter() - start_time

    print("\nLinear Search")
    print(f"Found: {'Yes' if linear_result is not None else 'No'}")
    print(f"Comparisons: {linear_comparisons:,}")
    print(f"Runtime: {linear_runtime*1E6:.9f} microseconds")

    print("\nBinary Search")
    print(f"Found: {'Yes' if binary_result is not None else 'No'}")
    print(f"Comparisons: {binary_comparisons:,}")
    print(f"Runtime: {binary_runtime*1E6:.9f} microseconds")

def sort_items_by_name(items: list[Item]) -> list[Item]:
    print("================ ITEM SORT ================")
    print("If you want to compare other sorting algorithms, uncomment the corresponding lines in the code.")
    print("It takes time to sort large lists, so be patient.")
    comparisons = 0
    # Bubble sort the items by name
    start_time = time.perf_counter()
    # _, comparisons = bubble_sort(items) # commented out to focus on Merge Sort, uncomment to compare with other algorithms
    runtime = time.perf_counter() - start_time
    
    print(f"\nBubble Sort Comparisons: {comparisons:,}")
    print(f"Bubble Sort Runtime: {runtime*1E3:.0f} milliseconds")
    
    # Insertion sort the items by name
    start_time = time.perf_counter()
    # _, comparisons = insertion_sort(items) # commented out to focus on Merge Sort, uncomment to compare with other algorithms
    insertion_runtime = time.perf_counter() - start_time
    
    print(f"\nInsertion Sort Comparisons: {comparisons:,}")
    print(f"Insertion Sort Runtime: {insertion_runtime*1E3:.0f} milliseconds")
    
    # Selection sort the items by name
    start_time = time.perf_counter()
    # _, comparisons = selection_sort(items) # commented out to focus on Merge Sort, uncomment to compare with other algorithms
    selection_runtime = time.perf_counter() - start_time

    print(f"\nSelection Sort Comparisons: {comparisons:,}")
    print(f"Selection Sort Runtime: {selection_runtime*1E3:.0f} milliseconds")
    
    # Added for Lab 09 Part 3: Merge Sort
    # Merge sort the items by name
    start_time = time.perf_counter()
    merge_result, merge_comparisons = merge_sort(items)
    merge_runtime = time.perf_counter() - start_time

    print(f"\nMerge Sort Comparisons: {merge_comparisons:,}")
    print(f"Merge Sort Runtime: {merge_runtime*1E3:.0f} milliseconds")
    
    return merge_result

def main():
    entrance = create_mansion()
    
    try:
        items:list[Item] = load_items("items.txt")
        print(f"Loaded {len(items):,} items into the mansion catalog.")
        sorted_items = sort_items_by_name(items)
        print(f"Sorted {len(sorted_items):,} items by name.")
    except FileNotFoundError:
        print("\nError: items.txt was not found.")
        print("Place items.txt in the same folder as adventure_game.py and run again.")
        return

    print(f"================== WELCOME TO THE ADVENTURE GAME ==================")
    name = input("Enter your name: ").strip()
    if not name:
        name = "Unknown_Player"

    player = Player(name, entrance)
    player.missions = MissionQueue(create_missions())
    

    print(f"\nHey, {player.name}!")
    print("You enter an old abandoned mansion.")
    print(f"You are currently standing at the {player.current_room.name}.")

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice: "))

            match choice:
                case 1:
                    player.look()
                case 2:
                    move_player(player)
                case 3:
                    player.go_back() # added for Lab 09 Part 1
                case 4:
                    player.show_status()
                case 5:
                    player.show_visited_rooms()
                case 6:
                    search_for_room(entrance)
                case 7:
                    show_room_count(entrance)
                case 8:
                    search_item_catalog(items, sorted_items)
                case 9:
                    player.missions.show_current_mission() # added for Lab 09 Part 2
                case 10:
                    player.missions.complete_current_mission() # added for Lab 09 Part 2
                case 11:
                    player.missions.show_pending_missions() # added for Lab 09 Part 2
                case 12:
                    player.missions.show_completed_missions() # added for Lab 09 Part 2
                case 13:
                    player.missions.add_mission(input("Enter mission description: ").strip()) # added for Lab 09 Part 2
                case 14:
                    print(f"Thanks for playing, {player.name}!")
                    break # Exit the game loop
                case _:
                    print("Invalid choice. Please select an option between 1 and 14.")
        
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 14.")
            continue
        except InvalidRoomError as error:
            print(error)
            continue
        except InvalidMoveError as error:
            print(error)
            continue

if __name__ == "__main__":
    main()
