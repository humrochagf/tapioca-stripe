# -*- coding: utf-8 -*-

CUSTOMERS_MAPPING = {
    'customers_create': {
        'resource': '/customers',
        'docs': (
            'https://stripe.com/docs/api/customers/'
            'create'
        ),
        'methods': ['POST'],
    },
    'customers_retrieve': {
        'resource': '/customers/{id}',
        'docs': (
            'https://stripe.com/docs/api/customers/'
            'retrieve'
        ),
        'methods': ['GET'],
    },
    'customers_update': {
        'resource': '/customers/{id}',
        'docs': (
            'https://stripe.com/docs/api/customers/'
            'update'
        ),
        'methods': ['POST'],
    },
    'customers_delete': {
        'resource': '/customers/{id}',
        'docs': (
            'https://stripe.com/docs/api/customers/'
            'delete'
        ),
        'methods': ['DELETE'],
    },
    'customers_list': {
        'resource': '/customers',
        'docs': (
            'https://stripe.com/docs/api/customers/'
            'list'
        ),
        'methods': ['GET'],
    },
}
