"""Utility functions for exploring and managing rooms in the adventure game.
Includes functions for exploring rooms, counting rooms, finding rooms, resetting visited flags,
loading items from a file, and searching and sorting items.
"""

from room import Room
from item import Item

def explore_room(room: Room) -> None:
    """Recursively display all reachable rooms once."""
    if room.visited:
        return

    room.visited = True
    print(f"Room: {room.name}")
    print(room.description)

    for connected_room in room.connected_rooms:
        explore_room(connected_room)


def count_rooms(room: Room) -> int:
    """Recursively count all reachable rooms once."""
    if room.visited:
        return 0

    room.visited = True
    total = 1

    for connected_room in room.connected_rooms:
        total += count_rooms(connected_room)

    return total


def find_room(room: Room, target_name: str) -> Room | None:
    """Recursively search for a room by name."""
    if room.visited:
        return None

    room.visited = True

    if room.name.lower() == target_name.strip().lower():
        return room

    for connected_room in room.connected_rooms:
        result = find_room(connected_room, target_name)
        if result is not None:
            return result

    return None


def reset_visited(room: Room) -> None:
    """Recursively reset the visited flag for every reachable room."""
    if not room.visited:
        return

    room.visited = False

    for connected_room in room.connected_rooms:
        reset_visited(connected_room)


def load_items(filename:str)->list[Item]:
    """Load item names from a text file and return Item objects."""
    items:list[Item] = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            name = line.strip()

            if name:
                items.append(Item(name))

    return items

##### Searching algorithms for Item objects by name #####
def linear_search(items, target_name):
    """Search Item objects one by one and return (item, comparisons)."""
    target_name = target_name.lower()
    comparisons = 0

    for item in items:
        comparisons += 1

        if item.name.lower() == target_name:
            return item, comparisons

    return None, comparisons

def binary_search(items, target_name):
    """Binary-search a case-insensitively sorted list of Item objects."""
    target_name = target_name.lower()
    left = 0
    right = len(items) - 1
    comparisons = 0

    while left <= right:
        middle = (left + right) // 2
        middle_name = items[middle].name.lower()
        comparisons += 1

        if middle_name == target_name:
            return items[middle], comparisons
        elif middle_name < target_name:
            left = middle + 1
        else:
            right = middle - 1

    return None, comparisons

##### Sorting algorithms for Item objects by name #####
def bubble_sort(sorted_items: list[Item]) -> tuple[list[Item], int]:
    """Sort Item objects by name using bubble sort and return (sorted_items, comparisons)."""
    sorted_items = sorted_items[:]
    n = len(sorted_items)
    comparisons = 0

    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if sorted_items[j].name.lower() > sorted_items[j+1].name.lower():
                sorted_items[j], sorted_items[j+1] = sorted_items[j+1], sorted_items[j]

    return sorted_items, comparisons

def selection_sort(items: list[Item]) -> tuple[list[Item], int]:
    """Sort Item objects by name using selection sort and return (sorted_items, comparisons)."""
    sorted_items = items[:]
    n = len(sorted_items)
    comparisons = 0

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            comparisons += 1
            if sorted_items[j].name.lower() < sorted_items[min_index].name.lower():
                min_index = j
        if min_index != i:
            sorted_items[i], sorted_items[min_index] = sorted_items[min_index], sorted_items[i]

    return sorted_items, comparisons

def insertion_sort(items: list[Item]) -> tuple[list[Item], int]:
    """Sort Item objects by name using insertion sort and return (sorted_items, comparisons)."""
    sorted_items = items[:]
    comparisons = 0

    for i in range(1, len(sorted_items)):
        key_item = sorted_items[i]
        j = i - 1
        while j >= 0 and sorted_items[j].name.lower() > key_item.name.lower():
            comparisons += 1
            sorted_items[j + 1] = sorted_items[j]
            j -= 1
        sorted_items[j + 1] = key_item

    return sorted_items, comparisons

# ===================================================================
# New code for Lab_09, PART 3
# Implement merge sort for Item objects with comparison count.
# ===================================================================

def merge_sort(items: list[Item]) -> tuple[list[Item], int]:
    """Sort Item objects by name using merge sort and return (sorted_items, comparisons)."""
    if len(items) <= 1:
        return items[:], 0

    middle = len(items) // 2
    left, left_comparisons = merge_sort(items[:middle])
    right, right_comparisons = merge_sort(items[middle:])

    merged, merge_comparisons = _merge(left, right)

    return merged, left_comparisons + right_comparisons + merge_comparisons


def _merge(left: list[Item], right: list[Item]) -> tuple[list[Item], int]:
    result = []
    i = 0
    j = 0
    comparisons = 0

    while i < len(left) and j < len(right):
        comparisons += 1

        if left[i].name.lower() <= right[j].name.lower():
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result, comparisons

# ===================================================================