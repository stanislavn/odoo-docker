from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    vat_local = fields.Char(
        string='DIČ',
        help='Slovak VAT number (DIČ)',
        size=12,
    )
    show_vat_local = fields.Boolean(compute='_compute_show_vat_local', store=False)

    @api.depends('country_id')
    def _compute_show_vat_local(self):
        for rec in self:
            rec.show_vat_local = rec.country_id.code == 'SK'

    @api.onchange('country_id')
    def _onchange_country_id(self):
        if self.country_id and self.country_id.code != 'SK':
            self.vat_local = False
