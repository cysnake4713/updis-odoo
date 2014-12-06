# -*- coding: utf-8 -*-
{
    'name': 'UPDIS Project Module',
    'version': '0.2',
    'category': 'up_project_management',
    'complexity': "easy",
    'description': """
UPDIS Project Module.""",
    'author': 'cysnake4713',
    'website': 'http://openerp.com',
    'depends': ['base', 'mail'],
    'update_xml': [
        'security/updis_security.xml',
        'security/ir.model.access.csv',

        'views/project_view.xml',
        'views/project_menu.xml',
    ],
    'demo_xml': [],
    'test': [],
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
