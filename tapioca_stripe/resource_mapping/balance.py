# -*- coding: utf-8 -*-

BALANCE_MAPPING = {
    'balance_retrieve': {
        'resource': '/balance',
        'docs': (
            'https://stripe.com/docs/api/balance/'
            'balance_retrieve'
        ),
        'methods': ['GET'],
    },
    'balance_transaction_retrieve': {
        'resource': '/balance/history/{id}',
        'docs': (
            'https://stripe.com/docs/api/balance/'
            'balance_transaction_retrieve'
        ),
        'methods': ['GET'],
    },
    'balance_transaction_list': {
        'resource': '/balance/history',
        'docs': (
            'https://stripe.com/docs/api/balance/'
            'balance_history'
        ),
        'methods': ['GET'],
    },
}
