from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_DIVER_TYPE = {
        "ScubaDiver": ScubaDiver,
        "FreeDiver": FreeDiver
    }

    VALID_FISH_TYPE = {
        "DeepSeaFish": DeepSeaFish,
        "PredatoryFish": PredatoryFish
    }

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        try:
            diver = self.VALID_DIVER_TYPE[diver_type](diver_name)
        except KeyError:
            return f"{diver_type} is not allowed in our competition."
        try:
            next(filter(lambda d: d.name == diver_name, self.divers))
            return f"{diver_name} is already a participant."
        except StopIteration:
            self.divers.append(diver)
            return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        try:
            fish = self.VALID_FISH_TYPE[fish_type](fish_name, points)
        except KeyError:
            return f"{fish_type} is forbidden for chasing in our competition."
        try:
            next(filter(lambda f: f.name == fish_name, self.fish))
            return f"{fish_name} is already permitted."
        except StopIteration:
            self.fish.append(fish)
            return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        try:
            diver = next(filter(lambda d: d.name == diver_name, self.divers))
        except StopIteration:
            return f"{diver_name} is not registered for the competition."

        try:
            fish = next(filter(lambda f: f.name == fish_name, self.fish))
        except StopIteration:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            message = f"{diver_name} missed a good {fish_name}."
        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                message = f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                message = f"{diver_name} missed a good {fish_name}."
        else:
            diver.hit(fish)
            message = f"{diver_name} hits a {fish.points}pt. {fish_name}."

        if diver.oxygen_level == 0:
            diver.update_health_status()
        return message

    # TODO  replace the above with diver.update_health_status(), if currently not working

    def health_recovery(self):
        divers_with_issues = [d for d in self.divers if d.has_health_issue]
        for d in divers_with_issues:
            d.update_health_status()
            d.renew_oxy()
        return f"Divers recovered: {len(divers_with_issues)}"

    # TODO if not working, replace with Ines version

    def diver_catch_report(self, diver_name: str):

        diver = [d for d in self.divers if d.name == diver_name][0]
        result = f"**{diver_name} Catch Report**\n"
        fish_details = "\n".join([f.fish_details() for f in diver.catch])
        result += fish_details
        return result

    def competition_statistics(self):
        healthy_divers = [d for d in self.divers if not d.has_health_issue]
        first_sort = sorted(healthy_divers,key= lambda d: (-d.competition_points, - len(d.catch), d.name))

        result = f"**Nautical Catch Challenge Statistics**\n"
        result += "\n".join(str(d) for d in first_sort)
        return result
