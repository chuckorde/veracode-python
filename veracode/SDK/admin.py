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

class CreateApp(Base):
    def __init__(self, app_name, business_criticality,
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
        super(CreateApp, self).__init__(
                module='admin',
                cls='CreateApp',
                fn='create',
                args={
                    'app_name':app_name,
                    'business_criticality':business_criticality,
                    'vendor_id':vendor_id,
                    'policy':policy,
                    'business_unit':business_unit,
                    'business_owner':business_owner,
                    'buisness_owner_email':buisness_owner_email,
                    'teams':','.join([t if teams else '' for t in teams]),
                    'origin':origin,
                    'industry':industry,
                    'app_type':app_type,
                    'deployment_method':deployment_method,
                    'web_application':web_application,
                    'archer_app_name':archer_app_name,
                    'tags':','.join([t if tags else '' for t in tags]),
                    'next_day_scheduling_enabled':next_day_scheduling_enabled
                })

