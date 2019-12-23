import sys, os
import logging
from datetime import datetime
from veracode import SDK, application
from veracode.SDK.utils import Properties
from veracode.exceptions import *

if sys.version_info[0] >= 3:
    basestring = str


class Build(object):
    """ class: veracode.build.Build
    """
    def __new__(self, app=None):
        if app:
            return ExistingBuild(app=app)
        else:
            return NewBuild()


class ExistingBuild(object):
    """ class: veracode.build.ExistingBuild
    """
    def __init__(self, app):
        self._app = app

    def list(self):
        builds = SDK.upload.GetBuildList(
                app_id=self._app.id, sandbox_id=self._app.sandbox.id)
        if not hasattr(builds, 'build'):
            return []
        if isinstance(builds.build, list):
            return [NewBuild(build, self._app) for build in builds.build]
        return [NewBuild(builds.build, self._app)]


class NewBuild(Properties):
    """ class: veracode.build.NewBuild
    """
    def __init__(self, obj=None, app=None):
        if not app:
            app = application.Application()
        self._app = app

        self._properties = ['build_id', 'version']
        self._renamed_properties = ['id', 'version']
        self._update_properties(obj)

        self._info = None
        self._report = None
        self._modules = []

        if obj:
            self.obj = obj
            if hasattr(obj, 'build'):
                self.version = obj.build.version

    def _get_build_info(self):
        if self._info is None:
            try:
                self._info = SDK.upload.GetBuildInfo(
                                        app_id=self._app.id,
                                        build_id=self.id)
            except VeracodeInvalidArgumentError:
                raise VeracodeBuildError(
                        'The application does not have any builds.')

    @property
    def info(self):
        self._get_build_info()
        return Info(self._info.build)

    @property
    def analysis(self):
        self._get_build_info()
        return Analysis(self._info.build)

    @property
    def policy(self):
        self._get_build_info()
        return Policy(self._info.build)

    @property
    def name(self):
        return self.version

    @name.setter
    def name(self, name):
        self.version = name

    def upload(self, files, compress=False):
        if isinstance(files, list):
            self._modules = [os.path.expanduser(f) for f in files]

        elif isinstance(files, basestring):
            self._modules = glob(os.path.expanduser(files))

        for f in self._modules:
            SDK.upload.UploadFile(
                    app_id=self._app.id,
                    sandbox_id=self._app.sandbox.id,
                    file=f)

    def scan(self,  auto_scan=True,
            scan_all_nonfatal_top_level_modules=True):

        SDK.upload.BeginPrescan(
                app_id=self._app.id,
                sandbox_id=self._app.sandbox.id,
                auto_scan=auto_scan,
                scan_all_nonfatal_top_level_modules=\
                        scan_all_nonfatal_top_level_modules)

    def delete(self):
        res = SDK.upload.DeleteBuild(app_id=self._app.id,
                sandbox_id=self._app.sandbox.id)
        return res.status_code == 200

    @property
    def report(self):
        if not self._report:
            if self.id:
                self._report = Report(self)
        return self._report

    def __repr__(self):
        return "<Veracode Build: version='{}', id={}>".format(
                self.version, self.id)

class Info(Properties):
    def __init__(self, obj=None):
        self._properties = [
            'grace_period_expired',
            'legacy_scan_engine',
            'lifecycle_stage',
            'platform',
            'rules_status',
            'scan_overdue',
            'submitter',
            'version'
        ]
        self._update_properties(obj)

    def __repr__(self):
        return "<Veracode Build Info: scan_overdue='{}', submitter='{}'>"\
                .format(self.scan_overdue, self.submitter)

class Analysis(Properties):
    def __init__(self, obj=None):
        self._properties = [
            'analysis_type',
            'engine_version',
            'published_date',
            'status'
        ]
        self._renamed_properties = [
                'type', 'engine_version','published_date','status']
        self._update_properties()

        if hasattr(obj, 'analysis_unit'):
            self._update_properties(obj.analysis_unit)

    def __bool__(self):
        return self.type is not None

    def __repr__(self):
        return "<Veracode Build Analysis: type='{}', status='{}'>".format(
            self.type, self.status)

class Policy(Properties):
    def __init__(self, obj=None):
        self._properties = [
            'policy_compliance_status',
            'policy_name',
            'policy_updated_date',
            'policy_version'
        ]
        self._renamed_properties = [
                'compliance', 'name', 'updated_date', 'version']
        self._update_properties(obj)

    def __repr__(self):
        return "<Veracode Build Policy: name='{}', compliance={}>".format(
            self.name, self.compliance)

    def __bool__(self):
        return self.name is not None


class Report(object):
    def __init__(self, obj):
        self._build = obj
        data = SDK.results.DetailedReport(build_id=self._build.id)
        # TODO: this needs more inspection and should use util class
        for prop in dir(data):
            if prop.startswith('_'):
                continue
            setattr(self, prop, getattr(data, prop))

    @property
    def flaws(self):
        def exists(obj, prop):
            if not hasattr(obj, prop):
                return []
            if not isinstance(getattr(obj, prop), list):
                return [getattr(obj, prop)]
            return getattr(obj, prop)

        for sev in self.severity:
            for cat in exists(sev, 'category'):
                for cwe in exists(cat, 'cwe'):
                    for staticflaw in exists(cwe, 'staticflaws'):
                        for flaw in exists(staticflaw, 'flaw'):
                            yield(Flaw(flaw))

    def __repr__(self):
        if not hasattr(self, 'sandbox_name'):
            self.sandbox_name = None
        return ("<Veracode Report: application='{}', sandbox='{}', "
                "build='{}', flaws={}>".format(
                     self.app_name, self.sandbox_name,
                     self._build.version, self.total_flaws))

class Flaw(Properties):
    def __init__(self, flaw):
        self._properties =[
            'affects_policy_compliance',
            'categoryid',
            'categoryname',
            'cia_impact',
            'count',
            'cweid',
            'date_first_occurrence',
            'description',
            'exploitLevel',
            'functionprototype',
            'functionrelativelocation',
            'grace_period_expires',
            'issueid',
            'line',
            'mitigation_status',
            'mitigation_status_desc',
            'module',
            'note',
            'pcirelated',
            'remediation_status',
            'remediationeffort',
            'scope',
            'severity',
            'sourcefile',
            'sourcefilepath',
            'type'
        ]
        self._update_properties(flaw)

        if self.mitigation_status.lower() == 'none':
            self.mitigation_status = None

    def __repr__(self):
        return "<Veracode Flaw: CWE='{}', severity={}>".format(
                self.cweid, self.severity)

