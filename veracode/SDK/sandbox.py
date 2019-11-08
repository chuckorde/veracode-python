from veracode.SDK.core import Base

class UpdateSandbox(Base):
    """ class: veracode.SDK.sandbox.UpdateSandbox

        params:
            sandbox_id: required
            custom_field_value: required
            custom_field_name: required

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
                sandbox_id,
                custom_field_value,
                custom_field_name,
        ):

        super(UpdateSandbox, self).__init__(
            module='sandbox',
            cls='UpdateSandbox',
            fn='get',
            args={
                'sandbox_id':sandbox_id,
                'custom_field_value':custom_field_value,
                'custom_field_name':custom_field_name,
            })

class CreateSandbox(Base):
    """ class: veracode.SDK.sandbox.CreateSandbox

        params:
            sandbox_name: required
            app_id: required

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
                sandbox_name,
                app_id,
        ):

        super(CreateSandbox, self).__init__(
            module='sandbox',
            cls='CreateSandbox',
            fn='get',
            args={
                'sandbox_name':sandbox_name,
                'app_id':app_id,
            })

class GetSandboxList(Base):
    """ class: veracode.SDK.sandbox.GetSandboxList

        params:
            app_id: required

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
                app_id,
        ):

        super(GetSandboxList, self).__init__(
            module='sandbox',
            cls='GetSandboxList',
            fn='get',
            args={
                'app_id':app_id,
            })

class PromoteSandbox(Base):
    """ class: veracode.SDK.sandbox.PromoteSandbox

        params:
            build_id: required

        returns: A python object that represents the returned API data.
    """
    def __init__(self,
                build_id,
        ):

        super(PromoteSandbox, self).__init__(
            module='sandbox',
            cls='PromoteSandbox',
            fn='get',
            args={
                'build_id':build_id,
            })

