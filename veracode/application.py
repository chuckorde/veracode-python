import sys, os
import logging
from glob import glob
from veracode import SDK, build, sandbox
from veracode.exceptions import *

if sys.version_info[0] >= 3:
    basestring = str

class Application(object):
    """
    # create an appliation with only the required properties
    >>> app = Application()
    >>> app.name = 'TEST_APPLICATION'
    >>> app.business_criticality = 'High'

    # save returns a new object
    >>> app = app.save()
    """
    def __new__(self, name=None, sandbox=None, build=None):
        if name:
            return ExistingApplication(name, sandbox, build)
        else:
            return NewApplication()

    @classmethod
    def list(self, name_only=True):
        """ Returns a list of applications for the current account

        >>> apps = Application.list()
        >>> isinstance(apps, list)
        True
        """
        apps = SDK.upload.GetAppList()
        if name_only:
            return [app.app_name for app in apps.app]
        return [(app.app_id, app.app_name) for app in apps.app]


class NewApplication(object):
    """ NewApplication: Not directly called

    >>> app = Application()
    >>> app
    <Veracode Application: [Not Saved]>

    >>> isinstance(app, NewApplication)
    True
    """
    def __init__(self):
        # TODO: Properties class!
        self.id = None
        self.name = None
        self.vendor_id = None
        self.business_criticality = None
        self.policy = None
        self.business_unit = None
        self.business_owner = None
        self.business_owner_email = None
        self.teams = []
        self.origin = None
        self.industry = None
        self.app_type = None
        self.deployment_method = None
        self.web_application = None
        self.archer_app_name = None
        self.tags = []
        self.next_day_scheduling_enabled = None
        # where do you set the description?

        # needed for pre-save sanity
        self.sandbox = sandbox.Sandbox(app_name=self.name)


    def save(self):
        """ Returns a new instance of ExistingApplication.
        use `app = app.save()` after setting name and business_criticality

        >>> app = Application()
        >>> app.name = 'TEMP_APPLICATION'
        >>> app.business_criticality = 'Low'
        >>> app = app.save()

        # confirm that the app was created
        >>> app = Application('TEMP_APPLICATION')

        # returned instance should be ExistingApplication
        >>> isinstance(app, ExistingApplication)
        True

        # clean up
        >>> app.delete()
        True
        """
        payload = {
            'app_name': self.name,
            'vendor_id': self.vendor_id,
            'business_criticality': self.business_criticality,
            'policy': self.policy,
            'business_unit': self.business_unit,
            'business_owner': self.business_owner,
            'business_owner_email': self.business_owner_email,
            'teams': self.teams,
            'origin': self.origin,
            'industry': self.industry,
            'app_type': self.app_type,
            'deployment_method': self.deployment_method,
            'web_application': self.web_application,
            'archer_app_name': self.archer_app_name,
            'tags': self.tags,
            'next_day_scheduling_enabled':self.next_day_scheduling_enabled
        }
        SDK.upload.CreateApp(**payload)
        return ExistingApplication(self.name)

    def __repr__(self):
        return '<Veracode Application: [Not Saved]>'


class ExistingApplication(object):
    """ ExistingApplication: Not directly called

    # fetch the test application
    >>> app = Application('TEST_APPLICATION')
    >>> isinstance(app, ExistingApplication)
    True

    # attempting to fetch an app that doesn't exist should raise
    # VeracodeApplicationError
    >>> app = Application('APPLICATION_DOESNT_EXIST')
    Traceback (most recent call last):
        ...
    veracode.exceptions.VeracodeApplicationError: The requested application does not exist.
    """

    def __init__(self, app_name, sandbox_name=None, build_name=None):
        self._flaws = None
        self._build = None
        self._builds = None
        self._summary = None
        self._details = None
        self._sandboxes = None
        self._teams = None
        self._tags = None

        self.info = self._get_app_by_name(app_name).application
        self.id = self.info.app_id
        self.name = self.info.app_name
        self.teams = []
        self.tags = []

        self._sandbox = self._get_sandbox_by_name(sandbox_name)
        self._build = self._get_build_by_name(build_name)
        self._builds = []

        props = [
            'business_criticality',
            'policy',
            'business_owner',
            'business_owner_email',
            'business_unit',
            'origin',
            'industry',
            'app_type',
            'deployment_method',
            'archer_app_name',
            'custom_field_name',
            'custom_field_value',
            'next_day_scheduling_enabled'
        ]
        # TODO: use util class
        for prop in props:
            if hasattr(self.info, prop):
                setattr(self, prop, getattr(self.info, prop))
            else:
                setattr(self, prop, None)

    def _get_app_by_name(self, app_name):
        apps = SDK.upload.GetAppList()
        for app in apps.app:
            if app.app_name == app_name:
                return SDK.upload.GetAppInfo(app.app_id)
        raise VeracodeApplicationError((
            'The requested application does not exist.'))

    def _get_sandbox_by_name(self, sandbox_name):
        if not sandbox_name:
            return sandbox.Sandbox()
        for s in self.sandboxes:
            if s.name == sandbox_name:
                return s
        raise VeracodeSandboxError((
            'The requested sandbox does not exist.'))

    def _get_build_by_name(self, build_name):
        if not build_name:
            return build.Build()
        for s in self.builds:
            if s.version == build_name:
                return s
        raise VeracodeBuildError(('The requested build does not exist.'))

    def __repr__(self):
        return "<Veracode Application: name='{}', id={}>".format(
                self.name, self.id)

    # def upload(self, files, compress=False):
    #     if isinstance(files, list):
    #         files = [os.path.expanduser(f) for f in files]
    #
    #     elif isinstance(files, basestring):
    #         files = glob(os.path.expanduser(files))
    #
    #     for f in files:
    #         SDK.upload.UploadFile(
    #                 app_id=self.id, sandbox_id=self.sandbox.id, file=f)
    #
    # def scan(self, sandbox=None, auto_scan=True,
    #         scan_all_nonfatal_top_level_modules=True):
    #
    #     self.sandbox = sandbox if sandbox else None
    #     SDK.upload.BeginPrescan(
    #             app_id=self.id,
    #             sandbox_id=self.sandbox.id,
    #             auto_scan=auto_scan,
    #             scan_all_nonfatal_top_level_modules=\
    #                     scan_all_nonfatal_top_level_modules)

    def save(self):
        payload = {
            'app_id': self.id,
            'app_name': self.name,
            'business_criticality': self.business_criticality,
            'policy': self.policy,
            'business_unit': self.business_unit,
            'business_owner': self.business_owner,
            'business_owner_email': self.business_owner_email,
            'teams': self.teams,
            'origin': self.origin,
            'industry': self.industry,
            'app_type': self.app_type,
            'deployment_method': self.deployment_method,
            'archer_app_name': self.archer_app_name,
            'tags': self.tags,
            'custom_field_name': self.custom_field_name,
            'custom_field_value': self.custom_field_value,
            'next_day_scheduling_enabled': self.next_day_scheduling_enabled
        }
        return SDK.upload.UpdateApp(**payload).status_code == 200

    def delete(self):
        return SDK.upload.DeleteApp(self.id).status_code == 200

    @property
    def sandboxes(self):
        """ property: a list of zero or more sandboxes for the current
        application.

            args: None

            returns: list of Sandbox objects, or empty list

        >>> app = Application('TEST_APPLICATION')
        >>> isinstance(app.sandboxes, list)
        True
        """
        if not self._sandboxes:
            self._sandboxes = sandbox.Sandbox.list(app_id=self.id)
        return self._sandboxes

    @property
    def sandbox(self):
        """ property: the current application sandbox (if exists)

            args: None

            returns: a Sandbox object or None

        >>> app = Application('TEST_APPLICATION')

        # passing a string will lookup the sandbox by name, and raise exception
        # if no sandbox by that name exists
        >>> app.sandbox = 'TEST_SANDBOX1'
        Traceback (most recent call last):
            ...
        veracode.exceptions.VeracodeSandboxError: ... sandbox does not exist.
        """
        if self._sandbox.id:
            return self._sandbox
        return sandbox.Sandbox()

    @sandbox.setter
    def sandbox(self, obj):
        """  property (setter): updates the app sandbox with a Sandbox object
             or a string name of an existing Sandbox

             args: existing sandbox name, or Sandbox object

             returns: None

             tests: doctest runs from the getter
        """
        if not obj:
            self._sandbox = sandbox.Sandbox()
        elif isinstance(obj, basestring):
            self._sandbox = self._get_sandbox_by_name(obj)
        elif isinstance(obj, sandbox.NewSandbox):
            if not obj.id:
                sandbox_name = obj.name
                SDK.sandbox.CreateSandbox(
                        app_id=self.id, sandbox_name=sandbox_name)
                self._sandboxes = None
                obj = self._get_sandbox_by_name(sandbox_name)
            self._sandbox = obj
        self._build = build.NewBuild(app=self)
        self._builds = []

    @property
    def builds(self):
        if not self._builds:
            self._builds = build.Build(self).list()
        return self._builds[::-1]

    @property
    def build(self):
        if self._build.id:
            return self._build
        if len(self.builds) <= 0:
            self._build = build.NewBuild()
            self._build._app = self
            self._builds.append(self._build)
            return self._build
        return self.builds[0]

    @build.setter
    def build(self, obj):
        if obj == None:
            self._build = build.NewBuild(app=self)
        else:
            if isinstance(obj, basestring):
                self._build = self._get_build_by_name(obj)

            elif isinstance(obj, build.NewBuild):
                try:
                    self._build = self._get_build_by_name(obj.version)
                except:
                    new_build = SDK.upload.CreateBuild(
                            version=obj.version,
                            app_id=self.id,
                            sandbox_id=self.sandbox.id)
                    self._build = build.NewBuild(app=self, obj=new_build)
        self._builds = []

