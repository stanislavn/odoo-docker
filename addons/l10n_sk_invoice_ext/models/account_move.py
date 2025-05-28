from odoo import models, fields, api, _
from odoo.exceptions import UserError
import re

class AccountMove(models.Model):
    _inherit = 'account.move'

    taxable_supply_date = fields.Date(
        string='Dátum zdaniteľného plnenia',
        help='Date of taxable supply',
    )
    specific_symbol = fields.Char(
        string='Špecifický symbol',
        help='Specific symbol for payment',
        size=10,
    )
    partner_company_registry = fields.Char(
        string='IČO',
        related='partner_id.company_registry',
        store=False,
        readonly=True,
    )
    partner_vat_local = fields.Char(
        string='DIČ',
        related='partner_id.vat_local',
        store=False,
        readonly=True,
    )

    @api.onchange('invoice_date')
    def _onchange_invoice_date(self):
        if not self.taxable_supply_date:
            self.taxable_supply_date = self.invoice_date

    @api.constrains('specific_symbol')
    def _check_specific_symbol(self):
        for record in self:
            if record.specific_symbol and not record.specific_symbol.isdigit():
                raise UserError(_('Špecifický symbol musí obsahovať len čísla.'))
            if record.specific_symbol and len(record.specific_symbol) > 10:
                raise UserError(_('Špecifický symbol nesmie byť dlhší ako 10 čísel.'))

    @api.constrains('taxable_supply_date', 'invoice_date')
    def _check_taxable_supply_date(self):
        for record in self:
            if record.taxable_supply_date and record.invoice_date:
                if record.taxable_supply_date > record.invoice_date:
                    raise UserError(_('Dátum zdaniteľného plnenia nemôže byť neskôr ako dátum faktúry.'))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('taxable_supply_date') and vals.get('invoice_date'):
                vals['taxable_supply_date'] = vals['invoice_date']
        return super().create(vals_list)

    def _get_payment_reference(self):
        self.ensure_one()
        if self.payment_reference:
            # Remove non-digit characters
            ref = re.sub(r'\D', '', self.payment_reference)
            if len(ref) > 10:
                raise UserError(_('Variabilný symbol nesmie byť dlhší ako 10 čísel.'))
            return ref
        return super()._get_payment_reference()

    def _get_name_invoice_report(self):
        self.ensure_one()
        return self.name.replace('/', '')