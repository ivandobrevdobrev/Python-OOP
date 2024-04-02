from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT = {"ElbowPad": ElbowPad, "KneePad": KneePad}
    VALID_TEAM = {"IndoorTeam": IndoorTeam, "OutdoorTeam": OutdoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        try:
            equipment = self.VALID_EQUIPMENT[equipment_type]()
            self.equipment.append(equipment)
            return f"{equipment_type} was successfully added."
        except KeyError:
            raise Exception("Invalid equipment type!")

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        try:
            team = self.VALID_TEAM[team_type](team_name, country, advantage)
        except KeyError:
            raise Exception("Invalid team type!")
        if len(self.teams) < self.capacity:
            self.teams.append(team)
            return f"{team_type} was successfully added."
        else:
            return "Not enough tournament capacity."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment_item = next(filter(lambda e: e.__class__.__name__ == equipment_type, self.equipment))
        team = next(filter(lambda t: t.name == team_name, self.teams))

        if team.budget < equipment_item.price:
            raise Exception("Budget is not enough!")
        else:
            self.equipment.remove(equipment_item)
            team.equipment.append(equipment_item)
            team.budget -= equipment_item.price
            return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        try:
            team = next(filter(lambda t: t.name == team_name, self.teams))
        except StopIteration:
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
        else:
            self.teams.remove(team)
            return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        count = 0
        for eq in self.equipment:

            if equipment_type == eq.__class__.__name__:
                count += 1
                eq.increase_price()
        return f"Successfully changed {count}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = next(filter(lambda t: t.name == team_name1, self.teams))
        team2 = next(filter(lambda t: t.name == team_name2, self.teams))

        if team1.__class__.__name__ != team2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")
        else:
            if team1.sum_points() > team2.sum_points():
                team1.win()
                return f"The winner is {team1.name}."
            elif team1.sum_points() < team2.sum_points():
                team2.win()
                return f"The winner is {team2.name}."
            else:
                return "No winner in this game."

    def get_statistics(self):
        sorted_teams = sorted(self.teams,key= lambda t: -t.wins)

        result = f"Tournament: {self.name}\nNumber of Teams: {len(self.teams)}\nTeams:\n"
        result += "\n".join([team.get_statistics() for team in sorted_teams])

        return result

