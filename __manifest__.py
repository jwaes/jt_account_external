# -*- coding: utf-8 -*-
{
    'name': "jt_account_external",

    'summary': "Add extra fields to account",

    'description': "",

    'author': "jaco tech",
    'website': "https://jaco.tech",
    "license": "AGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        'views/account_account_views.xml',
        'views/account_move_views.xml',
        'views/product_view.xml',
    ],

}
