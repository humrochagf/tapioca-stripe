# -*- coding: utf-8 -*-

FILE_LINKS_MAPPING = {
    'file_links_create': {
        'resource': '/file_links',
        'docs': (
            'https://stripe.com/docs/api/file_links/'
            'create'
        ),
        'methods': ['POST'],
    },
    'file_links_retrieve': {
        'resource': '/file_links/{id}',
        'docs': (
            'https://stripe.com/docs/api/file_links/'
            'retrieve'
        ),
        'methods': ['GET'],
    },
    'file_links_update': {
        'resource': '/file_links/{id}',
        'docs': (
            'https://stripe.com/docs/api/file_links/'
            'update'
        ),
        'methods': ['POST'],
    },
    'file_links_list': {
        'resource': '/file_links',
        'docs': (
            'https://stripe.com/docs/api/file_links/'
            'list'
        ),
        'methods': ['GET'],
    },
}
