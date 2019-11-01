import sys, os
import logging
from glob import glob
from veracode import SDK, sandbox, build
# from veracode.SDK.exceptions import *
from veracode.exceptions import *

if sys.version_info[0] >= 3:
	basestring = str

class Application(object):
	def __new__(self, name=None, sandbox=None, build=None):
		if name:
			return ExistingApplication(name, sandbox, build)
		else:
			return NewApplication()

	@classmethod
	def list(self):
		apps = SDK.upload.GetAppList()
		return [app.app_name for app in apps.app]


class NewApplication(object):
	def __init__(self):
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
		# where do you set the description

	def save(self):
		"""Returns a new instance of ExistingApplication.
		use `app = app.save()` after setting name and business_criticality
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


class ExistingApplication(object):
	def __init__(self, app_name, sandbox_name=None, build_name=None):
		self._flaws = None
		self._build = None
		# self._build_id = None
		self._builds = None
		# self._build_info = None
		self._summary = None
		self._details = None
		self._sandboxes = None
		self._teams = None
		self._tags = None

		self._new_files = []


		self._app = self._get_app_by_name(app_name)
		self.id = self._app.app_id
		self.name = self._app.app_name

		self._sandbox = self._get_sandbox_by_name(sandbox_name)
		self._build = self._get_build_by_name(build_name)

		self.business_criticality = None
		self.policy = None
		self.business_unit = None
		self.business_owner = None
		self.business_owner_email = None
		# teams
		self.origin = None
		self.industry = None
		self.app_type = None
		self.deployment_method = None
		self.archer_app_name = None
		# tags
		self.custom_field_name = None
		self.custom_field_value = None
		self.next_day_scheduling_enabled = None



	def _get_app_by_name(self, app_name):
		apps = SDK.upload.GetAppList()
		for app in apps.app:
			if app.app_name == app_name:
				return app
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
		return "<Veracode Application: name='{}', id={}>".format(self.name, self.id)


	def save(self):
		payload = {
			'app_id': self.id,
			'app_name': self.name,
			'business_criticality': self.business_criticality,
			'policy': self.policy,
			'business_unit': self.business_unit,
			'business_owner': self.business_owner,
			'business_owner_email': self.business_owner_email,
			'teams': list(self.teams),
			'origin': self.origin,
			'industry': self.industry,
			'app_type': self.app_type,
			'deployment_method': self.deployment_method,
			'archer_app_name': self.archer_app_name,
			'tags': list(self.tags),
			'custom_field_name': self.custom_field_name,
			'custom_field_value': self.custom_field_value,
			'next_day_scheduling_enabled': self.next_day_scheduling_enabled
		}
		SDK.upload.UpdateApp(**payload)

	def delete(self):
		SDK.upload.DeleteApp(self.id)

	def upload_files(self, item, sandbox=None, fn=None):
		self.sandbox = sandbox if sandbox else None
		if isinstance(item, list):
			self._new_files = os.path.expanduser(item)
		elif isinstance(item, basestring):
			self._new_files = [os.path.expanduser(f) for f in glob(item)]
		for f in self._new_files:
			if fn: fn(f)
			SDK.upload.UploadFile(
					app_id=self.id, sandbox_id=self.sandbox.id, file=f)

	def scan(self, sandbox=None, auto_scan=True,
			scan_all_nonfatal_top_level_modules=True):

		self.sandbox = sandbox if sandbox else None
		SDK.upload.BeginPrescan(
				app_id=self.id,
				sandbox_id=self.sandbox.id,
				auto_scan=auto_scan,
				scan_all_nonfatal_top_level_modules=scan_all_nonfatal_top_level_modules)

	@property
	def sandboxes(self):
		if not self._sandboxes:
			self._sandboxes = sandbox.Sandbox(self.name).list()
		return self._sandboxes

	@property
	def sandbox(self):
		if self._sandbox.id:
			return self._sandbox
		return None

	@sandbox.setter
	def sandbox(self, obj):
		if not obj:
			self._sandbox = sandbox.Sandbox()
		elif isinstance(obj, basestring):
			self._sandbox = self._get_sandbox_by_name(obj)
		elif isinstance(obj, sandbox.NewSandbox):
			self._sandbox = obj
		self._build = build.Build()
		self._builds = None

	@property
	def builds(self):
		if not self._builds:
			self._builds = build.Build(self.id, self._sandbox.id).list()
		return self._builds


	@property
	def build(self):
		if self._build.id:
			return self._build
		# do we want an empty build object or a nontype except on build.report?
		if len(self.builds) <= 0:
			return None
		return self.builds[0]

	@build.setter
	def build(self, obj):
		if not obj:
			self._build = build.NewBuild()
		elif isinstance(obj, build.NewBuild):
			self._build = obj
		elif isinstance(obj, basestring):
			self._build = self._get_build_by_name(obj)

#
#	  @property
#	  def builds(self):
#		  self._builds = _Builds(self).get()
#		  if isinstance(self._builds, list):
#			  builds = self._builds
#		  else:
#			  builds = [self._builds]
#		  if len(builds) > 0:
#			  self._build = builds[0]
#		  self._builds = builds
#		  return self._builds[::-1]
#
#	  @property
#	  def has_builds(self):
#		  return len(self.builds) > 0
#
#	  @property
#	  def build_info(self):
#		  try:
#			  self._build_info = SDK.upload.GetBuildInfo(
#					  self.id,
#					  sandbox_id=self.sandbox_id,
#					  build_id=self.build.build_id)
#		  except VeracodeInvalidArgumentError as e:
#			  raise VeracodeApplicationBuildError((
#				  'The application does not have any builds.'))
#		  return self._build_info
#
#
#	  @property
#	  def application_files(self):
#		  file_list = SDK.upload.GetFileList(
#				  app_id=self.id, sandbox_id=self.sandbox_id)
#		  if isinstance(file_list.file, list):
#			  return [f.file_name for f in file_list.file]
#		  return [file_list.file.file_name]
#
#	  @property
#	  def summary(self):
#		  if not self._summary:
#			  if not self._build_info:
#				  self._build = self.build_info.build
#			  self._summary = SDK.results.SummaryReport(
#				  build_id=self.build_info.build_id)
#		  return self._summary
#
#	  @property
#	  def details(self):
#		  if not self._details:
#			  if not self._build_info:
#				  self._build = self.build_info.build
#			  self._details = SDK.results.DetailedReport(
#				  build_id=self.build_info.build_id)
#		  return self._details
#
#	  @property
#	  def teams(self):
#		  if self.has_builds:
#			  teams_list =	_AppTeams(self)
#			  if isinstance(teams_list, list):
#				  return teams_list
#			  return [teams_list]
#		  return []
#
#	  @teams.setter
#	  def teams(self, item):
#		  self.teams.clear()
#		  if isinstance(item, list):
#			  for i in item:
#				  self.teams.append(i)
#		  if isinstance(item, basestring):
#			  for i in item.split(','):
#				  self.teams.append(i)
#
#	  @property
#	  def tags(self):
#		  tag_list = _BuildTags(self)
#		  if isinstance(tag_list, list):
#			  return tag_list
#		  return [tag_list]
#
#	  @tags.setter
#	  def tags(self, item):
#		  self.tags.clear()
#		  if isinstance(item, list):
#			  for i in item:
#				  self.tags.append(i)
#		  if isinstance(item, basestring):
#			  for i in item.split(','):
#				  self.tags.append(i)
#
#
# class _AppTeams(list):
#	  def __init__(self, app):
#		  super(_AppTeams, self).__init__()
#		  self.app = app
#		  self._teams = self.app.summary.teams
#
#	  def append(self, item):
#		  self._teams.append(item)
#
#	  def remove(self, item):
#		  self._teams.remove(item)
#
#	  def clear(self):
#		  self._teams.clear()
#
#	  def __iter__(self):
#		  return iter(self._teams)
#
#	  def __str__(self):
#		  return self._teams.__str__()
#
#	  def __nonzero__(self):
#		  if self._teams.__len__() == 0:
#			  return True
#		  return self._teams.__len__()
#
#	  __bool__ = __nonzero__
#
# # move to build class
# class _BuildTags(list):
#	  def __init__(self, app):
#		  super(_BuildTags, self).__init__()
#		  self.app = app
#		  self._tags = self.app.summary.tags
#
#	  def append(self, item):
#		  self._tags.append(item)
#
#	  def remove(self, item):
#		  self._tags.remove(item)
#
#	  def clear(self):
#		  self._tags.clear()
#
#	  def __iter__(self):
#		  return iter(self._tags)
#
#	  def __str__(self):
#		  return self._tags.__str__()
#
#	  def __nonzero__(self):
#		  if self._tags.__len__() == 0:
#			  return True
#		  return self._tags.__len__()
#
#	  __bool__ = __nonzero__
#
# class _Builds(list):
#	  def __init__(self, app):
#		  self.app = app
#		  super(_Builds, self).__init__()
#
#	  def get(self):
#		  builds = SDK.upload.GetBuildList(self.app.id, self.app.sandbox_id)
#		  if not hasattr(builds, 'build'):
#			  return []
#		  return builds.build
#
# # TODO: move to utils
# def _get_props(obj):
#	  if isinstance(obj, list):
#		  if len(obj) > 0:
#			  obj = obj[0]
#	  return [p for p in dir(obj) if not p.startswith('_')]
#
# def _find(obj, val, properties):
#	  data = []
#	  def find_obj(parent, obj):
#		  if isinstance(parent, list):
#			  for child in parent:
#				  for prop in properties:
#					  if hasattr(child, prop):
#						  find_obj(getattr(child, prop), obj)
#		  else:
#			  if hasattr(parent, obj):
#				  data.append(getattr(parent, obj))
#			  for prop in properties:
#				  if hasattr(parent, prop):
#					  if hasattr(parent, obj):
#						  data.append(getattr(parent, obj))
#					  else:
#						  find_obj(getattr(parent, prop), obj)
#	  find_obj(obj, val)
#	  flat_data = []
#	  for d in data:
#		  if isinstance(d, list):
#			  for f in d:
#				  flat_data.append(f)
#		  else:
#			  flat_data.append(d)
#	  return flat_data

