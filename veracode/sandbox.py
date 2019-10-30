import sys, os
import logging
from glob import glob
from veracode import SDK, application
from veracode.exceptions import *

if sys.version_info[0] >= 3:
    basestring = str


class Sandbox(object):
    def __new__(self, app_name=None):
        if app_name:
            return ExistingSandbox(app_name)
        else:
            return NewSandbox()

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
        if isinstance(app_name, basestring):
            app = application.Application(app_name)
            self.app_id = app.id

    def list(self):
        sandboxes = SDK.sandbox.getSandboxList(app_id=self.app_id)
        if not hasattr(sandboxes, 'sandbox'):
            return []
        if isinstance(sandboxes.sandbox, list):
            return [NewSandbox(sandbox) for sandbox in sandboxes.sandbox]
        return [NewSandbox(sandboxes.sandbox)]

