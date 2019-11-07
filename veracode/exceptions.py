from veracode.SDK.exceptions import *
from veracode.API.exceptions import *

class VeracodeApplicationError(Exception):
    pass

class VeracodeApplicationBuildError(Exception):
    pass

class VeracodeSandboxError(Exception):
    pass

class VeracodeBuildError(Exception):
    pass
