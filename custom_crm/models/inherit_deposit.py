from odoo import models, fields, api, exceptions
import logging

logger = logging.getLogger(__name__)

class Deposit(models.Model):
    _inherit = 'account.payment'

    codigo_ref = fields.Char(string='Ref. papeleta')

    nota = fields.Char(string='Nota')

    cuenta_bancaria = fields.Many2one(
        comodel_name='res.partner.bank',
        string='Cuenta de banco'
    )

    payment_method_line_id = fields.Many2one(
        comodel_name='account.payment.method.line',
        required=False        
    )

    journal_id = fields.Many2one(
        comodel_name='account.journal',
        required=False        
    )

    estado = fields.Selection(
        [
            ('S', 'Subido'),
            ('C', 'Confirmado'),
            ('F', 'Facturado')
        ],
        readonly=True,
    )
    
    @api.model
    def load(self, data):
        try:
            for record in data:
                if 'codigo_ref' in record:
                    record['codigo_ref'] = 25

                self.create(record)

        except Exception as e:
            raise exceptions.UserError(f'error al importar datos {str(e)}')
