from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    VALID_CLIMBERS = {
        "SummitClimber": SummitClimber,
        "ArcticClimber": ArcticClimber,
    }

    VALID_PEAKS = {
        "SummitPeak": SummitPeak,
        "ArcticPeak": ArcticPeak,
    }

    def __init__(self):
        self.climbers: List[BaseClimber] = []
        self.peaks: List[BasePeak] = []

    def register_climber(self, climber_type: str, climber_name: str):
        try:
            climber = self.VALID_CLIMBERS[climber_type](climber_name)
        except KeyError:
             return (f"{climber_type} doesn't exist in our register.")

        try:
            next(filter(lambda c: c.name == climber_name, self.climbers))
            return f"{climber_name} has been already registered."
        except StopIteration:
            self.climbers.append(climber)
            return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):

        try:
            peak = self.VALID_PEAKS[peak_type](peak_name,peak_elevation)
            self.peaks.append(peak)
            return f"{peak_name} is successfully added to the wish list as a {peak_type}."
        except KeyError:
            return (f"{peak_type} is an unknown type of peak.")



    def check_gear(self,climber_name: str, peak_name: str, gear: List[str]):
        climber = next(filter(lambda c:c.name == climber_name, self.climbers))
        peak = next(filter(lambda p:p.name == peak_name, self.peaks))

        if gear == peak.get_recommended_gear():
            return f"{climber_name} is prepared to climb {peak_name}."
        climber.is_prepared = False

        return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(g for g in sorted(peak.get_recommended_gear()) if not g in gear)}."

    def perform_climbing(self,climber_name: str, peak_name: str):
        try:
            climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        except StopIteration:
            return f"Climber {climber_name} is not registered yet."

        try:
            peak = next(filter(lambda p:p.name == peak_name, self.peaks))
        except StopIteration:
            return f"Peak {peak_name} is not part of the wish list."

        if climber.is_prepared and climber.can_climb():
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."
        elif not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        climber.rest()
        return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        climbers_that_can_climb = filter(lambda c: len(c.conquered_peaks) > 0, self.climbers)
        climbers = sorted(climbers_that_can_climb, key=lambda c: (-len(c.conquered_peaks), c.name))

        total_peaks_climbed = len({p for c in climbers for p in c.conquered_peaks}) # create set to  remove duplicate Peak names

        return f"Total climbed peaks: {total_peaks_climbed}\n" + \
            "**Climber's statistics:**\n" + \
            "\n".join(str(c) for c in climbers)

