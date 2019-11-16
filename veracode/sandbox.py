import sys, os
import logging
from glob import glob
from veracode import SDK, application
from veracode.exceptions import *

if sys.version_info[0] >= 3:
    basestring = str


class Sandbox(object):
    """
    # fetch application creatde in application testa
    >>> app = application.Application('TEST_APPLICATION')

    # check default states
    >>> app.sandbox == None
    True
    >>> app.sandboxes
    []

    # create a sandbox and assign it to the app
    >>> sb = Sandbox()
    >>> sb.name = 'TEST_APP_SANDBOX1'
    >>> app.sandbox = sb
    >>> app.sandbox.name
    'TEST_APP_SANDBOX1'

    # sleep to give the API time
    >>> import time
    >>> time.sleep(3)

    # create another sandbox and assign it to the app
    >>> sb = Sandbox()
    >>> sb.name = 'TEST_APP_SANDBOX2'
    >>> app.sandbox = sb
    >>> app.sandbox.name
    'TEST_APP_SANDBOX2'

    # check the results
    >>> len(app.sandboxes) == 2
    True

    # should be a LIFO
    >>> app.sandboxes[0].name
    'TEST_APP_SANDBOX2'
    >>> app.sandboxes[1].name
    'TEST_APP_SANDBOX1'
    """
    def __new__(self, app_name=None):
        if app_name:
            return ExistingSandbox(app_name)
        else:
            return NewSandbox()

    @classmethod
    def list(self, app_id):
        sandboxes = SDK.sandbox.GetSandboxList(app_id=app_id)
        if not hasattr(sandboxes, 'sandbox'):
            return []
        if isinstance(sandboxes.sandbox, list):
            return [NewSandbox(sandbox) for sandbox in sandboxes.sandbox][::-1]
        return [NewSandbox(sandboxes.sandbox)]

class NewSandbox(object):
    def __init__(self, obj=None):
        self.id = None
        self.name = None
        self.owner = None
        self.last_modified = None
        self.customfield = None

        if obj:
            self.id = obj.sandbox_id
            self.name = obj.sandbox_name
            self.owner = obj.owner
            self.last_modified = obj.last_modified
            self.customfield = obj.customfield

    def __repr__(self):
        return "<Veracode Sandbox: name='{}', id={}>".format(self.name, self.id)


class ExistingSandbox(object):
    def __init__(self, app_name):
        self.app_id = None
        self.id = None
        if isinstance(app_name, basestring):
            app = application.Application(app_name)
            self.app_id = app.id


