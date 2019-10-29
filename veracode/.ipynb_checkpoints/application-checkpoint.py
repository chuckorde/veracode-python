from veracode import SDK
from veracode.SDK.exceptions import *
from .exceptions import *


class Application(object):
    def __init__(self, app_name):
        self._app = self._get_app_by_name(app_name)
        self._builds = None
        self._build_info = None
        self._summary = None
        self._details = None
        if not self._app:
            raise VeracodeApplicationError((
                'The requested application does not exist.'))
        self.app_id = self._app.app_id
        self.app_name = self._app.app_name

    def _get_app_by_name(self, app_name):
        apps = SDK.upload.GetAppList()
        for app in apps.app:
            if app.app_name == app_name:
                return app
        return None

    @property
    def builds(self):
        if not self._builds:
            self._builds = SDK.upload.GetBuildList(self.app_id)
        if isinstance(self._builds, list):
            return self._builds
        return [self._builds]

    @property
    def build_info(self):
        if not self._build_info:
            try:
                self._build_info = SDK.upload.GetBuildInfo(self.app_id)
            except VeracodeInvalidArgumentError as e:
                raise VeracodeApplicationBuildError((
                    'The application does not have any builds.'))
        return self._build_info

    @property
    def summary(self):
        if not self._summary:
            if not self._build_info:
                _ = self.build_info
            self._summary = SDK.results.SummaryReport(
                build_id=self.build_info.build_id)
        return self._summary

    @property
    def details(self):
        if not self._details:
            if not self._build_info:
                _ = self.build_info
            self._details = SDK.results.DetailedReport(
                build_id=self.build_info.build_id)
        return self._details

    @property
    def has_builds(self):
        try:
            self.summary
        except VeracodeApplicationBuildError:
            return False
        return True

    def update_teams(self, teams):
        SDK.upload.UpdateApp(
                app_name=self.app_name,
                app_id=self.app_id,
                teams=teams)        

    @classmethod
    def create(self):
        print('vreate')


