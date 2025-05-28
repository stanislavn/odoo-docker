from odoo import models, fields, api

class ResCompany(models.Model):
    _inherit = 'res.company'

    vat_local = fields.Char(
        string='DIČ',
        help='Slovak VAT number (DIČ)',
        size=12,
    )