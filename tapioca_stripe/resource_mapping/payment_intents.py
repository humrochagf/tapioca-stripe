# -*- coding: utf-8 -*-

PAYMENT_INTENTS_MAPPING = {
    'payment_intents_create': {
        'resource': '/payment_intents',
        'docs': (
            'https://stripe.com/docs/api/payment_intents/'
            'create'
        ),
        'methods': ['POST'],
    },
    'payment_intents_retrieve': {
        'resource': '/payment_intents/{id}',
        'docs': (
            'https://stripe.com/docs/api/payment_intents/'
            'retrieve'
        ),
        'methods': ['GET'],
    },
    'payment_intents_update': {
        'resource': '/payment_intents/{id}',
        'docs': (
            'https://stripe.com/docs/api/payment_intents/'
            'update'
        ),
        'methods': ['POST'],
    },
    'payment_intents_confirm': {
        'resource': '/payment_intents/{id}/confirm',
        'docs': (
            'https://stripe.com/docs/api/payment_intents/'
            'confirm'
        ),
        'methods': ['POST'],
    },
    'payment_intents_capture': {
        'resource': '/payment_intents/{id}/capture',
        'docs': (
            'https://stripe.com/docs/api/payment_intents/'
            'capture'
        ),
        'methods': ['POST'],
    },
    'payment_intents_cancel': {
        'resource': '/payment_intents/{id}/cancel',
        'docs': (
            'https://stripe.com/docs/api/payment_intents/'
            'cancel'
        ),
        'methods': ['POST'],
    },
    'payment_intents_list': {
        'resource': '/payment_intents',
        'docs': (
            'https://stripe.com/docs/api/payment_intents/'
            'list'
        ),
        'methods': ['GET'],
    },
}
