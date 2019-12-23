import sys
from veracode import SDK
from veracode.exceptions import *
from veracode.SDK.utils import Properties

if sys.version_info[0] >= 3:
    basestring = str

def _to_list(obj):
    if isinstance(obj, basestring):
        return [obj]
    if isinstance(obj, list):
        return obj
    return []

class User(object):
    def __new__(self, username=None):
        if username:
            return ExistingUser(username=username)
        else:
            return NewUser()

    @classmethod
    def list(self, email=None, first_name=None, last_name=None,
            name_only=True):
        users = SDK.admin.GetUserList(
                    first_name=first_name,
                    last_name=last_name,
                    email_address=email)
        if name_only:
            for u in _to_list(users.users.usernames):
                yield u
        else:
            for username in _to_list(users.users.usernames):
                try:
                    u = SDK.admin.GetUserInfo(username).login_account
                except VeracodeInvalidArgumentError:
                    sys.exit('Error: User does not exist.')
                if not hasattr(u, 'last_successful_login_date'):
                    u.last_successful_login_date = None
                yield (u.first_name, u.last_name, u.email_address,
                       u.last_successful_login_date)

class ExistingUser(Properties):
    def __init__(self, username=None, obj=None):
        if obj:
            user = obj
        else:
            user = SDK.admin.GetUserInfo(username=username)

        self._properties = [
            'phone',
            'has_ip_restriction',
            'allowed_ip_addresses',
            'is_saml_user',
            'login_enabled',
            'requires_token',
            'custom_id',
            'title',
            'is_elearning_manager',
            'elearning_manager',
            'elearning_track',
            'elearning_curriculum',
            'keep_elearning_active',
            'custom_one',
            'custom_two',
            'custom_three',
            'custom_four',
            'custom_five']

        self.username = user.username
        self._update_properties(obj)
        for (k,v) in user.login_account.__dict__.items():
            setattr(self, k,v)

        self.roles = _to_list(self.roles)
        self.teams = _to_list(self.teams)
        self.email = self.email_address

    def save(self):
        payload = {
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email_address': self.email_address,
            'phone': self.phone,
            'teams': ','.join(self.teams),
            'roles': ','.join(self.roles),
            # 'new_custom_id': self.custom_id,
            # 'has_ip_restrictions': self.has_ip_restrictions,
            # 'allowed_ip_addresses': self.allowed_ip_addresses,
            # 'is_saml_user': self.is_saml_user,
            # 'login_enabled': self.login_enabled,
            # 'requires_token': self.requires_token,
            # 'is_elearning_manager': self.is_elearning_manager,
            # 'elearning_manager': self.elearning_manager,
            # 'elearning_track': self.elearning_track,
            # 'elearning_curriculum': self.elearning_curriculum,
            # 'keep_elearning_active': self.keep_elearning_active,
            # 'custom_one': self.custom_one,
            # 'custom_two': self.custom_two,
            # 'custom_three': self.custom_three,
            # 'custom_four': self.custom_four,
            # 'custom_five': self.custom_five
        }
        SDK.admin.UpdateUser(**payload)
        return ExistingUser(username=self.username)

    def delete(self):
        return SDK.admin.DeleteUser(self.email_address).status_code == 200

    def __repr__(self):
        return "<Veracode User: name='{} {}', email='{}'>"\
                .format(self.first_name, self.last_name, self.email_address)

class NewUser(object):
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.email = None
        self.is_saml_user = None
        self.custom_id = None
        self.login_enabled = None
        self.phone = None
        self.requires_token = None
        self.title = None
        self.teams = []
        self.roles = []

    def save(self):
        payload = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email_address': self.email,
            'is_saml_user': self.is_saml_user,
            'custom_id': self.custom_id,
            'login_enabled': self.login_enabled,
            'phone': self.phone,
            'requires_token': self.requires_token,
            'teams': ','.join(self.teams),
            'roles': ','.join(self.roles),
            'title': self.title
        }
        user = SDK.admin.CreateUser(**payload)
        return ExistingUser(obj=user)
        # return ExistingUser(email=user.login_account.email_address)

    def __repr__(self):
        return "<Veracode User: [Not Saved]>"




