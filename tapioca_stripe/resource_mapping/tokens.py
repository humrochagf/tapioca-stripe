# -*- coding: utf-8 -*-

TOKENS_MAPPING = {
    'tokens_create': {
        'resource': '/tokens',
        'docs': (
            'https://stripe.com/docs/api/tokens'
        ),
        'methods': ['POST'],
    },
    'tokens_retrieve': {
        'resource': '/tokens/{id}',
        'docs': (
            'https://stripe.com/docs/api/tokens/'
            'retrieve'
        ),
        'methods': ['GET'],
    },
}
