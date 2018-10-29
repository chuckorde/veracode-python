from veracode import SDK


class Application(object):
    def __init__(self, app_name):
        self._get_app_by_name(app_name)
        self._app = self._get_app_by_name(app_name)
        self._builds = None
        self._build_info = None
        self._summary = None
        self._details = None

        self.app_id = self._app.app_id

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
            self._build_info = SDK.upload.GetBuildInfo(self.app_id)
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
