from mailbox import NotEmptyError


class Pet:
    def __init__(self, pet_name) -> None:
        self.pet_name = pet_name
    
class Team:
    def __init__(self, team_name):
        self.team_name = team_name

class TeamMascot(Pet, Team):
    def __init__(self, pet_name, team_name) -> None:
        Pet.__init__(self, pet_name)
        Team.__init__(self, team_name)
    
    def __str__(self):
        return f'{self.pet_name} is the {self.team_name} Mascot!'