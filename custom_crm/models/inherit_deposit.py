from odoo import models, fields, api, exceptions

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
        comodel_name='account_journal',
        required=False        
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
