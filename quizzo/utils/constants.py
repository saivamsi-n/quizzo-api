from enum import Enum


class OptionTypes(Enum):
    mcq = "mcq"
    essay = "essay"


OptionChoices = [(e.value, e.value) for e in OptionTypes]


class LeaderBoardSearchTypes(Enum):
    school = "School"
    all = "All"
    city = "City"


OptionChoices = [(e.value, e.value) for e in OptionTypes]
LeaderBoardSearchChoices = [(e.value, e.value) for e in LeaderBoardSearchTypes]
