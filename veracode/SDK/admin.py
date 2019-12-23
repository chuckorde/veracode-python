from veracode.SDK.core import Base

class DeleteUser(Base):
    """ class: veracode.SDK.admin.DeleteUser

        params:
			username: required
			custom_id: optional

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
				username,
				custom_id=None,
        ):

        super(DeleteUser, self).__init__(
            module='admin',
            cls='DeleteUser',
            fn='get',
            args={
				'username':username,
				'custom_id':custom_id,
            })

class UpdateUser(Base):
    """ class: veracode.SDK.admin.UpdateUser

        params:
			username: required
			teams: optional
			roles: optional
			requires_token: optional
			phone: optional
			new_custom_id: optional
			login_enabled: optional
			last_name: optional
			keep_elearning_active: optional
			is_saml_user: optional
			is_elearning_manager: optional
			has_ip_restrictions: optional
			first_name: optional
			email_address: optional
			elearning_track: optional
			elearning_manager: optional
			elearning_curriculum: optional
			custom_two: optional
			custom_three: optional
			custom_one: optional
			custom_id: optional
			custom_four: optional
			custom_five: optional
			allowed_ip_addresses: optional

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
				username,
				teams=None,
				roles=None,
				requires_token=None,
				phone=None,
				new_custom_id=None,
				login_enabled=None,
				last_name=None,
				keep_elearning_active=None,
				is_saml_user=None,
				is_elearning_manager=None,
				has_ip_restrictions=None,
				first_name=None,
				email_address=None,
				elearning_track=None,
				elearning_manager=None,
				elearning_curriculum=None,
				custom_two=None,
				custom_three=None,
				custom_one=None,
				custom_id=None,
				custom_four=None,
				custom_five=None,
				allowed_ip_addresses=None,
        ):

        super(UpdateUser, self).__init__(
            module='admin',
            cls='UpdateUser',
            fn='get',
            args={
				'username':username,
				'teams':teams,
				'roles':roles,
				'requires_token':requires_token,
				'phone':phone,
				'new_custom_id':new_custom_id,
				'login_enabled':login_enabled,
				'last_name':last_name,
				'keep_elearning_active':keep_elearning_active,
				'is_saml_user':is_saml_user,
				'is_elearning_manager':is_elearning_manager,
				'has_ip_restrictions':has_ip_restrictions,
				'first_name':first_name,
				'email_address':email_address,
				'elearning_track':elearning_track,
				'elearning_manager':elearning_manager,
				'elearning_curriculum':elearning_curriculum,
				'custom_two':custom_two,
				'custom_three':custom_three,
				'custom_one':custom_one,
				'custom_id':custom_id,
				'custom_four':custom_four,
				'custom_five':custom_five,
				'allowed_ip_addresses':allowed_ip_addresses,
            })

class GetTrackList(Base):
    """ class: veracode.SDK.admin.GetTrackList

        params:


        returns: A python object that represents the returned API data.
    """
    def __init__(self,

        ):

        super(GetTrackList, self).__init__(
            module='admin',
            cls='GetTrackList',
            fn='get',
            args={

            })

class GetMaintenanceScheduleInfo(Base):
    """ class: veracode.SDK.admin.GetMaintenanceScheduleInfo

        params:


        returns: A python object that represents the returned API data.
    """
    def __init__(self,

        ):

        super(GetMaintenanceScheduleInfo, self).__init__(
            module='admin',
            cls='GetMaintenanceScheduleInfo',
            fn='get',
            args={

            })

class GetTeamList(Base):
    """ class: veracode.SDK.admin.GetTeamList

        params:


        returns: A python object that represents the returned API data.
    """
    def __init__(self,

        ):

        super(GetTeamList, self).__init__(
            module='admin',
            cls='GetTeamList',
            fn='get',
            args={

            })

class GetUserInfo(Base):
    """ class: veracode.SDK.admin.GetUserInfo

        params:
			username: required
			custom_id: optional

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
				username,
				custom_id=None,
        ):

        super(GetUserInfo, self).__init__(
            module='admin',
            cls='GetUserInfo',
            fn='get',
            args={
				'username':username,
				'custom_id':custom_id,
            })

class DeleteTeam(Base):
    """ class: veracode.SDK.admin.DeleteTeam

        params:
			team_id: required

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
				team_id,
        ):

        super(DeleteTeam, self).__init__(
            module='admin',
            cls='DeleteTeam',
            fn='get',
            args={
				'team_id':team_id,
            })

class CreateUser(Base):
    """ class: veracode.SDK.admin.CreateUser

        params:
			last_name: required
			first_name: required
			email_address: required
			title: optional
			teams: optional
			roles: optional
			requires_token: optional
			phone: optional
			login_enabled: optional
			is_saml_user: optional
			custom_id: optional

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
				last_name,
				first_name,
				email_address,
				title=None,
				teams=None,
				roles=None,
				requires_token=None,
				phone=None,
				login_enabled=None,
				is_saml_user=None,
				custom_id=None,
        ):

        super(CreateUser, self).__init__(
            module='admin',
            cls='CreateUser',
            fn='get',
            args={
				'last_name':last_name,
				'first_name':first_name,
				'email_address':email_address,
				'title':title,
				'teams':teams,
				'roles':roles,
				'requires_token':requires_token,
				'phone':phone,
				'login_enabled':login_enabled,
				'is_saml_user':is_saml_user,
				'custom_id':custom_id,
            })

class GetUserList(Base):
    """ class: veracode.SDK.admin.GetUserList

        params:
			last_name: optional
			first_name: optional
			email_address: optional
			teams: optional
			roles: optional
			requires_token: optional
			phone: optional
			login_enabled: optional
			login_account_type: optional
			keep_elearning_active: optional
			is_saml_user: optional
			is_elearning_manager: optional
			elearning_track: optional
			elearning_manager: optional
			elearning_curriculum: optional
			custom_two: optional
			custom_three: optional
			custom_one: optional
			custom_id: optional
			custom_four: optional
			custom_five: optional

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
				last_name=None,
				first_name=None,
				email_address=None,
				teams=None,
				roles=None,
				requires_token=None,
				phone=None,
				login_enabled=None,
				login_account_type=None,
				keep_elearning_active=None,
				is_saml_user=None,
				is_elearning_manager=None,
				elearning_track=None,
				elearning_manager=None,
				elearning_curriculum=None,
				custom_two=None,
				custom_three=None,
				custom_one=None,
				custom_id=None,
				custom_four=None,
				custom_five=None,
        ):

        super(GetUserList, self).__init__(
            module='admin',
            cls='GetUserList',
            fn='get',
            args={
				'last_name':last_name,
				'first_name':first_name,
				'email_address':email_address,
				'teams':teams,
				'roles':roles,
				'requires_token':requires_token,
				'phone':phone,
				'login_enabled':login_enabled,
				'login_account_type':login_account_type,
				'keep_elearning_active':keep_elearning_active,
				'is_saml_user':is_saml_user,
				'is_elearning_manager':is_elearning_manager,
				'elearning_track':elearning_track,
				'elearning_manager':elearning_manager,
				'elearning_curriculum':elearning_curriculum,
				'custom_two':custom_two,
				'custom_three':custom_three,
				'custom_one':custom_one,
				'custom_id':custom_id,
				'custom_four':custom_four,
				'custom_five':custom_five,
            })

class GetTeamInfo(Base):
    """ class: veracode.SDK.admin.GetTeamInfo

        params:
			team_id: required
			include_users: optional
			include_applications: optional

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
				team_id,
				include_users=None,
				include_applications=None,
        ):

        super(GetTeamInfo, self).__init__(
            module='admin',
            cls='GetTeamInfo',
            fn='get',
            args={
				'team_id':team_id,
				'include_users':include_users,
				'include_applications':include_applications,
            })

class GetCurricumList(Base):
    """ class: veracode.SDK.admin.GetCurricumList

        params:


        returns: A python object that represents the returned API data.
    """
    def __init__(self,

        ):

        super(GetCurricumList, self).__init__(
            module='admin',
            cls='GetCurricumList',
            fn='get',
            args={

            })

class CreateTeam(Base):
    """ class: veracode.SDK.admin.CreateTeam

        params:
			team_name: optional
			members: optional

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
				team_name=None,
				members=None,
        ):

        super(CreateTeam, self).__init__(
            module='admin',
            cls='CreateTeam',
            fn='get',
            args={
				'team_name':team_name,
				'members':members,
            })

class UpdateTeam(Base):
    """ class: veracode.SDK.admin.UpdateTeam

        params:
			team_id: required
			members: required
			team_name: optional

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
				team_id,
				members,
				team_name=None,
        ):

        super(UpdateTeam, self).__init__(
            module='admin',
            cls='UpdateTeam',
            fn='get',
            args={
				'team_id':team_id,
				'members':members,
				'team_name':team_name,
            })

