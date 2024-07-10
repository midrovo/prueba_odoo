from odoo import models, fields, api

class Deposit(models.Model):
    _inherit = 'account.payment'

    is_internal_transfer = fields.Boolean(readonly=True)
    payment_type = fields.Selection(
        [('inbound', 'Recibir'), ('outbound', 'Enviar')],
        readonly=False,
        required=False,
        default='outbound',
        widget='check')
    partner_bank_id = fields.Many2one(comodel_name='res.partner.bank', invisible=True, readonly=False)

    @api.onchange('payment_type')
    def _onchange_payment_type(self):
        pass
