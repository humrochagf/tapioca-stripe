# -*- coding: utf-8 -*-

PRODUCTS_MAPPING = {
    'products_create': {
        'resource': '/products',
        'docs': (
            'https://stripe.com/docs/api/products/'
            'create'
        ),
        'methods': ['POST'],
    },
    'products_retrieve': {
        'resource': '/products/{id}',
        'docs': (
            'https://stripe.com/docs/api/products/'
            'retrieve'
        ),
        'methods': ['GET'],
    },
    'products_update': {
        'resource': '/products/{id}',
        'docs': (
            'https://stripe.com/docs/api/products/'
            'update'
        ),
        'methods': ['POST'],
    },
    'products_list': {
        'resource': '/products',
        'docs': (
            'https://stripe.com/docs/api/products/'
            'list'
        ),
        'methods': ['GET'],
    },
    'products_delete': {
        'resource': '/products/{id}',
        'docs': (
            'https://stripe.com/docs/api/products/'
            'delete'
        ),
        'methods': ['DELETE'],
    },
}
