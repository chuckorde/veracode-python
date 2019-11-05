import sys, os
import logging
from veracode import SDK
from veracode.exceptions import *

if sys.version_info[0] >= 3:
    basestring = str


class Build(object):
    def __new__(self, app_id=None, sandbox_id=None):
        if app_id:
            return ExistingBuild(app_id=app_id,sandbox_id=sandbox_id )
        else:
            return NewBuild()

class NewBuild(object):
    def __init__(self, obj=None, app_id=None):
        self.app_id = app_id
        self.id = None
        self.version = None

        self.grace_period_expired = None
        self.legacy_scan_engine = None
        self.lifecycle_stage = None
        self.platform = None
        self.results_ready = None
        self.scan_overdue = None
        self.submitter = None
        self._report = None


        if obj:
            self.id = obj.build_id
            self.version = obj.version

            self._info = SDK.upload.GetBuildInfo(app_id=self.app_id)
            self.grace_period_expired = self._info.build.grace_period_expired
            self.legacy_scan_engine = self._info.build.legacy_scan_engine
            self.lifecycle_stage = self._info.build.lifecycle_stage
            self.platform = self._info.build.platform
            self.results_ready = self._info.build.results_ready
            self.scan_overdue = self._info.build.scan_overdue
            self.submitter = self._info.build.submitter
            self.analysis = Analysis(self._info.build.analysis_unit)
            self.policy = Policy(self._info.build)

    @property
    def report(self):
        if not self._report:
            if self.id:
                self._report = Report(self)
        return self._report



    def __repr__(self):
        return "<Veracode Build: version='{}', id={}>".format(self.version, self.id)


class ExistingBuild(object):
    def __init__(self, app_id, sandbox_id=None):
        if isinstance(app_id, int):
            self.app_id = app_id
            self.sandbox_id = sandbox_id

    def list(self):
        builds = SDK.upload.GetBuildList(app_id=self.app_id, sandbox_id=self.sandbox_id)
        if not hasattr(builds, 'build'):
            return []
        if isinstance(builds.build, list):
            return [NewBuild(build, self.app_id) for build in builds.build][::-1]
        return [NewBuild(builds.build, self.app_id)]


class Analysis(object):
    def __init__(self, obj):
        self.type = obj.analysis_type
        self.engine_version = obj.engine_version
        self.published_date = obj.published_date
        # self.published_date_sec = obj.published_date_sec
        self.status = obj.status[0]

    def __repr__(self):
        return "<Veracode Build Analysis: type='{}', status={}>".format(
            self.type, self.status)

class Policy(object):
    def __init__(self, obj):
        self.compliance = obj.policy_compliance_status[0]
        self.name = obj.policy_name
        self.updated_date = obj.policy_updated_date
        self.version = obj.policy_version

    def __repr__(self):
        return "<Veracode Build Policy: name='{}', compliance={}>".format(
            self.name, self.compliance)

class Report(object):
    def __init__(self, obj):
        self._build = obj
        data = SDK.results.DetailedReport(build_id=self._build.id)
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
        return "<Veracode Report: application='{}', sandbox='{}' build='{}' flaws={}>".format(
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

        if len(self.remediation_status) > 0:
            self.remediation_status = self.remediation_status[0].capitalize()
        if len(self.mitigation_status) > 0:
            self.mitigation_status = self.mitigation_status[0].capitalize()
            if self.mitigation_status == 'None':
                self.mitigation_status = None

    def __repr__(self):
        return "<Veracode Flaw: CWE='{}', severity={}>".format(self.cweid, self.severity)

