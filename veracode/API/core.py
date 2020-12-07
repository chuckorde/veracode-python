import requests
from hashlib import sha256
from requests.adapters import HTTPAdapter
from urllib.parse import urlparse
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC
from veracode.API.exceptions import *

from veracode.log import veracode_logger
logger = veracode_logger('veracode')

class REST(object):
    class response:
        def __init__(self, status_code, data, res):
            self.status_code = status_code
            self.data = data
            self.res = res

    def __init__(self, end_point, api_version, server=None):
        self.__api_server = server or \
                'https://analysiscenter.veracode.com/api/'
        self.__end_point = end_point
        if api_version:
            self.__server = '/'.join(map(lambda x: str(x).rstrip('/'),
            [self.__api_server, api_version, self.__end_point]))
        else:
            self.__server = '/'.join(map(lambda x: str(x).rstrip('/'),
            [self.__api_server, self.__end_point]))

    def __prepared_request(self, method, query, file=None):
        logger.debug('{}, {}, STARTED'.format(self.__end_point, query))

        session = requests.Session()
        session.mount(self.__server, HTTPAdapter(max_retries=3))
        request = requests.Request(method, self.__server, params=query,
                files=file, auth=RequestsAuthPluginVeracodeHMAC())
        prepared_request = request.prepare()

        # Merge environment settings into session
        # This allows things like, REQUESTS_CA_BUNDLE, to be used
        settings = session.merge_environment_settings(
                prepared_request.url, {}, None, None, None)
        res = session.send(prepared_request, **settings)

        logger.debug('{}, {}, COMPLETED'.format(self.__end_point, query))
        logger.info('request URL: {}'.format(res.request.path_url))

        return res

    def GET(self, query=None, format='text'):
        res = self.__prepared_request('GET', query)
        return self.response(res.status_code, getattr(res, format), res)

    def POST(self, query=None, file=None):
        res = self.__prepared_request('POST', query=query, file=file)
        return self.response(res.status_code, res.text, res)

    def PUT(self):
        raise VeracodeNotImplemented('PUT not implemented.')

    def PATCH(self):
        raise VeracodeNotImplemented('PATCH not implemented.')

    def DELETE(self):
        raise VeracodeNotImplemented('DELETE not implemented.')

