{
    'name': 'Slovak Invoice Extensions',
    'version': '1.0',
    'category': 'Accounting/Localizations',
    'summary': 'Slovak invoice requirements and extensions',
    'description': """
        This module extends Odoo to meet Slovak invoice requirements:
        - Adds DIČ field for Slovak companies and partners
        - Adds taxable supply date
        - Adds specific symbol field
        - Modifies payment reference generation
        - Updates invoice report layout
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': [
        'base',
        'account',
        'l10n_sk',
    ],
    'data': [
        'views/res_company_views.xml',
        'views/res_partner_views.xml',
        'views/account_move_views.xml',
        'views/account_move_report_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}