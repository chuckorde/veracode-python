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

class CreateApp(REST):
    def __init__(self):
        super(CreateApp, self).__init__('createapp.do', 5.0)

    @classmethod
    def create(self, app_name, business_criticality,
            vendor_id=None,
            policy=None,
            business_unit=None,
            business_owner=None,
            buisness_owner_email=None,
            teams=None,
            origin=None,
            industry=None,
            app_type=None,
            deployment_method=None,
            web_application=None,
            archer_app_name=None,
            tags=None,
            next_day_scheduling_enabled=None
            ):
        return self().GET({
            'app_name':app_name,
            'business_criticality':business_criticality,
            'vendor_id':vendor_id,
            'policy':policy,
            'business_unit':business_unit,
            'business_owner':business_owner,
            'buisness_owner_email':buisness_owner_email,
            'teams':teams,
            'origin':origin,
            'industry':industry,
            'app_type':app_type,
            'deployment_method':deployment_method,
            'web_application':web_application,
            'archer_app_name':archer_app_name,
            'tags':tags,
            'next_day_scheduling_enabled':next_day_scheduling_enabled
            })
