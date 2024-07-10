from odoo import models, fields, api

class Deposit(models.Model):
    _inherit = 'account.payment'

    is_internal_transfer = fields.Boolean(readonly=True)
    # payment_type = fields.Selection(readonly=False, required=False, default='outbound')
    partner_bank_id = fields.Many2one(comodel_name='res.partner.bank', invisible=True, readonly=False)

    @api.model
    def default_get(self, fields_list):
        res = super(Deposit, self).default_get(fields_list)
        res['payment_type'] = 'outbound'
        return res