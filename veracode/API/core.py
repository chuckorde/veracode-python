import requests
import json
import os
import configparser
import time
import hmac
import codecs
from hashlib import sha256
from requests.adapters import HTTPAdapter
from urllib.parse import urlparse
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
        self.__api_id = os.environ.get('VERACODE_API_ID', None)
        self.__api_secret = os.environ.get('VERACODE_API_SECRET', None)
    
        if not (self.__api_id and self.__api_secret):
            self.profile = os.environ.get('VERACODE_API_PROFILE', 'DEFAULT')
            conf = configparser.ConfigParser()
            conf.read(os.path.expanduser('~/.veracode/credentials'))
            self.__api_id = conf.get(self.profile, 'VERACODE_API_ID')
            self.__api_secret = conf.get(self.profile, 'VERACODE_API_SECRET')

        self.__api_server = server or 'https://analysiscenter.veracode.com/api/'
        self.__end_point = end_point
        if api_version:
            self.__server = '/'.join(map(lambda x: str(x).rstrip('/'),
            [self.__api_server, api_version, self.__end_point]))
        else:
            self.__server = '/'.join(map(lambda x: str(x).rstrip('/'),
            [self.__api_server, self.__end_point]))

    def __veracode_hmac(self, host, url, method):
        signing_data = 'id={api_id}&host={host}&url={url}&method={method}'\
                .format(api_id=self.__api_id.lower(),
                        host=host.lower(),
                        url=url, method=method.upper())

        timestamp = int(round(time.time() * 1000))
        nonce = os.urandom(16).hex()

        key_nonce = hmac.new(
            codecs.decode(self.__api_secret, 'hex_codec'),
            codecs.decode(nonce, 'hex_codec'), sha256).digest()

        key_date = hmac.new(key_nonce, str(timestamp).encode(), sha256).digest()
        signature_key = hmac.new(
                key_date, 'vcode_request_version_1'.encode(), sha256).digest()
        signature = hmac.new(
                signature_key, signing_data.encode(), sha256).hexdigest()

        return '{auth} id={id},ts={ts},nonce={nonce},sig={sig}'.format(
            auth='VERACODE-HMAC-SHA-256',
            id=self.__api_id,
            ts=timestamp,
            nonce=nonce,
            sig=signature)

    def __prepared_request(self, method, query, file=None):
        logger.debug('{}, {}, STARTED'.format(self.__end_point, query))

        session = requests.Session()
        session.mount(self.__server, HTTPAdapter(max_retries=3))
        request = requests.Request(method, self.__server, params=query,
                files=file)
        prepared_request = request.prepare()
        prepared_request.headers['Authorization'] = self.__veracode_hmac(
            urlparse(self.__server).hostname, prepared_request.path_url, method)
        res = session.send(prepared_request)

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

