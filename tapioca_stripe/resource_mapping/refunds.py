# -*- coding: utf-8 -*-

REFUNDS_MAPPING = {
    'refunds_create': {
        'resource': '/refunds',
        'docs': (
            'https://stripe.com/docs/api/refunds/'
            'create'
        ),
        'methods': ['POST'],
    },
    'refunds_retrieve': {
        'resource': '/refunds/{id}',
        'docs': (
            'https://stripe.com/docs/api/refunds/'
            'retrieve'
        ),
        'methods': ['GET'],
    },
    'refunds_update': {
        'resource': '/refunds/{id}',
        'docs': (
            'https://stripe.com/docs/api/refunds/'
            'update'
        ),
        'methods': ['POST'],
    },
    'refunds_list': {
        'resource': '/refunds',
        'docs': (
            'https://stripe.com/docs/api/refunds/'
            'list'
        ),
        'methods': ['GET'],
    },
}
