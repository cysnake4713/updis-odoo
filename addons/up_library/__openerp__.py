# -*- coding: utf-8 -*-
{
    'name': 'Book Library Module',
    'version': '1.0',
    'category': 'up_library',
    'complexity': "easy",
    'description': """
Book Library Management Module.""",
    'author': 'Matt Cai',
    'website': 'http://cysnake.com',
    'depends': ['base', 'hr'],
    'data': [
        'security/up_library_security.xml',
        'security/ir.model.access.csv',

        'views/library_book_view.xml',
        'views/library_config_view.xml',
        'views/library_menu_view.xml',

        'data/library.book.config.csv',

    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}