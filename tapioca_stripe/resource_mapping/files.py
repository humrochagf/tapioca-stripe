# -*- coding: utf-8 -*-

FILES_MAPPING = {
    'files_create': {
        'resource': '/files',
        'docs': (
            'https://stripe.com/docs/api/files/'
            'create'
        ),
        'methods': ['POST'],
    },
    'files_retrieve': {
        'resource': '/files/{id}',
        'docs': (
            'https://stripe.com/docs/api/files/'
            'retrieve'
        ),
        'methods': ['GET'],
    },
    'files_list': {
        'resource': '/files',
        'docs': (
            'https://stripe.com/docs/api/files/'
            'list'
        ),
        'methods': ['GET'],
    },
}
