# -*- coding: utf-8 -*-

from requests.auth import HTTPBasicAuth
from tapioca import (
    JSONAdapterMixin, TapiocaAdapter, generate_wrapper_from_adapter
)

from .resource_mapping import RESOURCE_MAPPING


class StripeClientAdapter(JSONAdapterMixin, TapiocaAdapter):

    api_root = 'https://api.stripe.com/v1'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(StripeClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs
        )

        params['auth'] = HTTPBasicAuth(api_params.get('api_key'), '')

        return params

    def get_api_root(self, api_params):
        return self.api_root

    def get_iterator_list(self, response_data):
        return response_data

    def get_iterator_next_request_kwargs(self, iterator_request_kwargs,
                                         response_data, response):
        pass


Stripe = generate_wrapper_from_adapter(StripeClientAdapter)
