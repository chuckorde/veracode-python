from veracode.SDK.core import Base


class GetTeamList(Base):
    def __init__(self):
        super(GetTeamList, self).__init__(
                module='admin',
                cls='GetTeamList',
                fn='get',
                args=None)

class CreateTeam(Base):
    def __init__(self, team_name, members=[]):
        super(CreateTeam, self).__init__(
                module='admin',
                cls='CreateTeam',
                fn='create',
                args={
                    'team_name':team_name,
                    'members': ','.join([m if members else '' for m in members])
                })

