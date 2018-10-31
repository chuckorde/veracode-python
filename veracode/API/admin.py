from veracode.API.core import REST

class GetTeamList(REST):
    def __init__(self):
        super(GetTeamList, self).__init__('getteamlist.do', 3.0)

    @classmethod
    def get(self):
        return self().GET()

class CreateTeam(REST):
    def __init__(self):
        super(CreateTeam, self).__init__('createteam.do', 3.0)

    @classmethod
    def create(self, team_name, members=None):
        return self().GET({
            'team_name':team_name,
            'members': members
            })

