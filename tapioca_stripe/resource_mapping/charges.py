# -*- coding: utf-8 -*-

CHARGES_MAPPING = {
    'charges_create': {
        'resource': '/charges',
        'docs': (
            'https://stripe.com/docs/api/charges/'
            'create'
        ),
        'methods': ['POST'],
    },
    'charges_retrieve': {
        'resource': '/charges/{id}',
        'docs': (
            'https://stripe.com/docs/api/charges/'
            'retrieve'
        ),
        'methods': ['GET'],
    },
    'charges_update': {
        'resource': '/charges/{id}',
        'docs': (
            'https://stripe.com/docs/api/charges/'
            'update'
        ),
        'methods': ['POST'],
    },
    'charges_capture': {
        'resource': '/charges/{id}/capture',
        'docs': (
            'https://stripe.com/docs/api/charges/'
            'capture'
        ),
        'methods': ['POST'],
    },
    'charges_list': {
        'resource': '/charges',
        'docs': (
            'https://stripe.com/docs/api/charges/'
            'list'
        ),
        'methods': ['GET'],
    },
}
