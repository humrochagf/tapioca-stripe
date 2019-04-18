# -*- coding: utf-8 -*-

import json

from requests.auth import HTTPBasicAuth
from tapioca import TapiocaAdapter, generate_wrapper_from_adapter

from .resource_mapping import RESOURCE_MAPPING


class FormRequestJSONResponseAdapterMixin(object):

    def format_data_to_request(self, data):
        return data

    def response_to_native(self, response):
        if response.content.strip():
            return response.json()

    def get_error_message(self, data, response=None):
        if not data and response.content.strip():
            data = json.loads(response.content.decode('utf-8'))

        if data:
            return data.get('error', None)


class StripeClientAdapter(FormRequestJSONResponseAdapterMixin, TapiocaAdapter):

    api_root = 'https://api.stripe.com/v1'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(StripeClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs
        )

        params['auth'] = HTTPBasicAuth(api_params.get('api_key'), '')

        return params

    def get_api_root(self, api_params, **kwargs):
        # stripe file creation specific endpoint
        if kwargs.get('resource_name') == 'files_create':
            return 'https://files.stripe.com/v1'

        return self.api_root

    def get_iterator_list(self, response_data):
        return response_data

    def get_iterator_next_request_kwargs(self, iterator_request_kwargs,
                                         response_data, response):
        pass


Stripe = generate_wrapper_from_adapter(StripeClientAdapter)
