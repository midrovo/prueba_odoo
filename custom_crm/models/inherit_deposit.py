from odoo import models, fields, api

class Deposit(models.Model):
    _inherit = 'account.payment'

    is_internal_transfer = fields.Boolean(readonly=True)
    payment_type = fields.Selection(
        [('inbound', 'Recibir'), ('outbound', 'Enviar')],
        readonly=False,
        required=False,
        default='outbound')
    partner_bank_id = fields.Many2one(comodel_name='res.partner.bank', invisible=True, readonly=False)
