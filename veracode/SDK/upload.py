import inspect
from veracode import SDK


class BeginPreScan(SDK.core.Base):
    def __init__(self,
                app_id,
                auto_scan=None,
                sandbox_id=None,
                scan_all_nonfatal_top_level_modules=None
                ):
        self._module, self._cls, self._fn, self._obj, self._args = self.reflect(
                self, __name__, inspect.currentframe())
        super(self._obj, self).__init__(
                self._module, self._cls, self._fn, self._args)


class BeginScan(SDK.core.Base):
    def __init__(self,
                app_id,
                scan_all_top_level_modules=None,
                scan_selected_modules=None,
                scan_previously_selected_modules=None,
                sandbox_id=None
                ):
        self._module, self._cls, self._fn, self._obj, self._args = self.reflect(
                self, __name__, inspect.currentframe())
        super(self._obj, self).__init__(
                self._module, self._cls, self._fn, self._args)


class BeginScan(SDK.core.Base):
    def __init__(self,
                app_id,
                scan_all_top_level_modules=None,
                scan_selected_modules=None,
                scan_previously_selected_modules=None,
                sandbox_id=None
                ):
        self._module, self._cls, self._fn, self._obj, self._args = self.reflect(
                self, __name__, inspect.currentframe())
        super(self._obj, self).__init__(
                self._module, self._cls, self._fn, self._args)


class CreateApp(SDK.core.Base):
    def __init__(self,
                app_name,
                business_criticality,
                vendor_id=None,
                policy=None,
                business_unit=None,
                business_owner=None,
                business_owner_email=None,
                teams=None,
                origin=None,
                industry=None,
                app_type=None,
                deployment_method=None,
                web_application=None,
                archer_app_name=None,
                tags=None,
                next_day_scheduling_enabled=None
                ):
        self._module, self._cls, self._fn, self._obj, self._args = self.reflect(
                self, __name__, inspect.currentframe())
        super(self._obj, self).__init__(
                self._module, self._cls, self._fn, self._args)


class CreateBuild(SDK.core.Base):
    def __init__(self,
                app_id,
                version,
                # platform : deprecated
                lifecycle_stage=None,
                launch_stage=None,
                sandbox_id=None,
                legacy_scan_engine=None
                ):
        self._module, self._cls, self._fn, self._obj, self._args = self.reflect(
                self, __name__, inspect.currentframe())
        super(self._obj, self).__init__(
                self._module, self._cls, self._fn, self._args)


class DeleteApp(SDK.core.Base):
    def __init__(self, app_id):
        self._module, self._cls, self._fn, self._obj, self._args = self.reflect(
                self, __name__, inspect.currentframe())
        super(self._obj, self).__init__(
                self._module, self._cls, self._fn, self._args)


class DeleteBuild(SDK.core.Base):
    def __init__(self,
                app_id,
                sandbox_id=None,
                ):
        self._module, self._cls, self._fn, self._obj, self._args = self.reflect(
                self, __name__, inspect.currentframe())
        super(self._obj, self).__init__(
                self._module, self._cls, self._fn, self._args)



class GetAppInfo(SDK.core.Base):
    def __init__(self, app_id):
        self._module, self._cls, self._fn, self._obj, self._args = self.reflect(
                self, __name__, inspect.currentframe())
        super(self._obj, self).__init__(
                self._module, self._cls, self._fn, self._args)

class GetAppList(SDK.core.Base):
    def __init__(self, include_user_info=None):
        self._module, self._cls, self._fn, self._obj, self._args = self.reflect(
                self, __name__, inspect.currentframe())
        super(self._obj, self).__init__(
                self._module, self._cls, self._fn, self._args)


class GetBuildInfo(SDK.core.Base):
    def __init__(self, app_id, build_id=None, sandbox_id=None):
        self._module, self._cls, self._fn, self._obj, self._args = self.reflect(
                self, __name__, inspect.currentframe())
        super(self._obj, self).__init__(
                self._module, self._cls, self._fn, self._args)


class GetBuildList(SDK.core.Base):
    def __init__(self, app_id, sandbox_id=None):
        self._module, self._cls, self._fn, self._obj, self._args = self.reflect(
                self, __name__, inspect.currentframe())
        super(self._obj, self).__init__(
                self._module, self._cls, self._fn, self._args)


class GetFileList(SDK.core.Base):
    def __init__(self, app_id, build_id=None, sandbox_id=None):
        self._module, self._cls, self._fn, self._obj, self._args = self.reflect(
                self, __name__, inspect.currentframe())
        super(self._obj, self).__init__(
                self._module, self._cls, self._fn, self._args)


class GetPolicyList(SDK.core.Base):
    def __init__(self, app_id, build_id=None, sandbox_id=None):
        self._module, self._cls, self._fn, self._obj, self._args = self.reflect(
                self, __name__, inspect.currentframe())
        super(self._obj, self).__init__(
                self._module, self._cls, self._fn, self._args)


class GetPreScanResults(SDK.core.Base):
    def __init__(self, app_id, build_id=None, sandbox_id=None):
        self._module, self._cls, self._fn, self._obj, self._args = self.reflect(
                self, __name__, inspect.currentframe())
        super(self._obj, self).__init__(
                self._module, self._cls, self._fn, self._args)



class GetVendorList(SDK.core.Base):
    def __init__(self, app_id, file_id, sandbox_id=None):
        self._module, self._cls, self._fn, self._obj, self._args = self.reflect(
                self, __name__, inspect.currentframe())
        super(self._obj, self).__init__(
                self._module, self._cls, self._fn, self._args)


class RemoveFile(SDK.core.Base):
    def __init__(self, app_id, file_id, sandbox_id=None):
        self._module, self._cls, self._fn, self._obj, self._args = self.reflect(
                self, __name__, inspect.currentframe())
        super(self._obj, self).__init__(
                self._module, self._cls, self._fn, self._args)


class UpdateApp(SDK.core.Base):
    def __init__(self,
            app_id,
            app_name,
            description=None,
            business_criticality=None,
            policy=None,
            business_unit=None,
            business_owner=None,
            business_owner_email=None,
            teams=None,
            origin=None,
            industry=None,
            app_type=None,
            deployment_method=None,
            archer_app_name=None,
            tags=None,
            custom_field_name=None,
            next_day_scheduling_enabled=None):
        self._module, self._cls, self._fn, self._obj, self._args = self.reflect(
                self, __name__, inspect.currentframe())
        super(self._obj, self).__init__(
                self._module, self._cls, self._fn, self._args)

class UpdateBuild(SDK.core.Base):
    def __init__(self,
            app_id,
            build_id,
            version,
            lifecycle_stage=None,
            launch_date=None,
            sandbox_id=None
            ):
        self._module, self._cls, self._fn, self._obj, self._args = self.reflect(
                self, __name__, inspect.currentframe())
        super(self._obj, self).__init__(
                self._module, self._cls, self._fn, self._args)

