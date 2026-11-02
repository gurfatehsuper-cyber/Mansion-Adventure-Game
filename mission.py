from collections import deque

class Mission:
    def __init__(self, description: str) -> None:
        self.description = description
        self.completed = False

    def complete(self) -> None:
        self.completed = True
        
# ===================================================================
# New code for Lab_09, PART 2
# Implement a mission queue to manage current, completed, and pending missions.
# ===================================================================
class MissionQueue:
    def __init__(self, missions: list[Mission] = []) -> None:
        self.missions: deque[Mission] = deque(missions)
        self.completed_missions: list[Mission] = []

        def add_mission(self, mission: str) -> None:
            if mission.strip():
                self.missions.append(Mission(mission.strip()))

    def complete_current_mission(self) -> None:
        if not self.missions:
            print("No current mission to complete.")
            return

        mission = self.missions.popleft()
        mission.complete()
        self.completed_missions.append(mission)
        print(f"Completed: {mission.description}")

    def show_current_mission(self) -> None:
        if not self.missions:
            print("No current mission.")
            return

        print(f"Current Mission: {self.missions[0].description}")

    def show_completed_missions(self) -> None:
        if not self.completed_missions:
            print("No completed missions.")
            return

        print("Completed missions:")
        for mission in self.completed_missions:
            print(f"- {mission.description}")

    def show_pending_missions(self) -> None:
        if not self.missions:
            print("No pending missions.")
            return

        print("Pending missions:")
        for mission in self.missions:
            print(f"- {mission.description}")
# ===================================================================