# -*- coding: utf-8 -*-

PAYOUTS_MAPPING = {
    'payouts_create': {
        'resource': '/payouts',
        'docs': (
            'https://stripe.com/docs/api/payouts/'
            'create'
        ),
        'methods': ['POST'],
    },
    'payouts_retrieve': {
        'resource': '/payouts/{id}',
        'docs': (
            'https://stripe.com/docs/api/payouts/'
            'retrieve'
        ),
        'methods': ['GET'],
    },
    'payouts_update': {
        'resource': '/payouts/{id}',
        'docs': (
            'https://stripe.com/docs/api/payouts/'
            'update'
        ),
        'methods': ['POST'],
    },
    'payouts_cancel': {
        'resource': '/payouts/{id}/cancel',
        'docs': (
            'https://stripe.com/docs/api/payouts/'
            'cancel'
        ),
        'methods': ['POST'],
    },
    'payouts_list': {
        'resource': '/payouts',
        'docs': (
            'https://stripe.com/docs/api/payouts/'
            'list'
        ),
        'methods': ['GET'],
    },
}
