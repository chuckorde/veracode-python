import sys, os
import logging
from veracode import SDK
from veracode.SDK.utils import Properties
from veracode.exceptions import *

if sys.version_info[0] >= 3:
    basestring = str


class Build(object):
    """ class: veracode.build.Build
    """
    def __new__(self, app_id=None, sandbox_id=None):
        if app_id:
            return ExistingBuild(app_id=app_id,sandbox_id=sandbox_id )
        else:
            return NewBuild()


class ExistingBuild(object):
    """ class: veracode.build.ExistingBuild
    """
    def __init__(self, app_id, sandbox_id=None):
        if isinstance(app_id, int):
            self.app_id = app_id
            self.sandbox_id = sandbox_id

    def list(self):
        builds = SDK.upload.GetBuildList(app_id=self.app_id, sandbox_id=self.sandbox_id)
        if not hasattr(builds, 'build'):
            return []
        if isinstance(builds.build, list):
            return [NewBuild(build, self.app_id) for build in builds.build]
        return [NewBuild(builds.build, self.app_id)]


class NewBuild(Properties):
    """ class: veracode.build.NewBuild
    """
    def __init__(self, obj=None, app_id=None):
        self.app_id = app_id

        self._properties = ['build_id', 'version']
        self._renamed_properties = ['id', 'version']
        self._update_properties(obj)

        self.info = Info()
        self.analysis = Analysis()
        self.policy = Policy()

        self._report = None

        if self.app_id:
            info = SDK.upload.GetBuildInfo(app_id=self.app_id, build_id=self.id)
            if hasattr(info, 'build'):
                self.info = Info(info.build)
                self.analysis = Analysis(info.build)
                self.policy = Policy(info.build)

    def save(self):
        pass

    def delete(self):
        res = SDK.upload.DeleteBuild(app_id=self.app_id,
                sandbox_id=self.report.sandbox_id)
        return res.status_code == 200

    @property
    def report(self):
        if not self._report:
            if self.id:
                self._report = Report(self)
        return self._report

    def __repr__(self):
        return "<Veracode Build: version='{}', id={}>".format(self.version, self.id)


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
        return "<Veracode Build Info: scan_overdue='{}', submitter='{}'>".format(
            self.scan_overdue, self.submitter)

class Analysis(Properties):
    def __init__(self, obj=None):
        self._properties = [
            'analysis_type',
            'engine_version',
            'publish_date',
            'status'
        ]
        self._renamed_properties = [
                'type', 'engine_version','publish_date','status']
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
            'policy_updaed_date',
            'policy_version'
        ]
        self._renamed_properties = ['compliance', 'name', 'updated', 'version']
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
        return "<Veracode Report: application='{}', sandbox='{}', build='{}', flaws={}>".format(
            self.app_name, self.sandbox_name, self._build.version, self.total_flaws)

class Flaw(object):
    def __init__(self, flaw):
        props =[
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
        for prop in props:
            if hasattr(flaw, prop):
                setattr(self, prop, getattr(flaw, prop))
            else:
                setattr(self, prop, None)

            if self.mitigation_status == 'None':
                self.mitigation_status = None

    def __repr__(self):
        return "<Veracode Flaw: CWE='{}', severity={}>".format(self.cweid, self.severity)

