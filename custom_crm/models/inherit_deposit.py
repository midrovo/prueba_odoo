from odoo import models, fields, api

class Deposit(models.Model):
    _inherit = 'account.payment'

    partner_bank_id = fields.Many2one(invisible=True)