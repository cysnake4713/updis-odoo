# -*- coding: utf-8 -*-
{
    'name': 'Dashboard Module',
    'version': '0.2',
    'category': 'dashboard',
    'complexity': "easy",
    'description': """
UPDIS Project Module.""",
    'author': 'cysnake4713',
    'website': 'http://odoosoft.com',
    'depends': ['base', 'website'],
    'data': [
        'views/dashboard_menu.xml',
        'views/dashboard_template.xml',
        # 'views/dashboard_backend_navbar.xml',
        'views/website_backend_navbar.xml',
    ],
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
