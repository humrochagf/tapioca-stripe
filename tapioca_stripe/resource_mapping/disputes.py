# -*- coding: utf-8 -*-

DISPUTES_MAPPING = {
    'disputes_retrieve': {
        'resource': '/disputes/{id}',
        'docs': (
            'https://stripe.com/docs/api/disputes/'
            'retrieve'
        ),
        'methods': ['GET'],
    },
    'disputes_update': {
        'resource': '/disputes/{id}',
        'docs': (
            'https://stripe.com/docs/api/disputes/'
            'update'
        ),
        'methods': ['POST'],
    },
    'disputes_close': {
        'resource': '/disputes/{id}/close',
        'docs': (
            'https://stripe.com/docs/api/disputes/'
            'close'
        ),
        'methods': ['POST'],
    },
    'disputes_list': {
        'resource': '/disputes',
        'docs': (
            'https://stripe.com/docs/api/disputes/'
            'list'
        ),
        'methods': ['GET'],
    },
}
