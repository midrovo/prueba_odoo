from odoo import models, fields, api
import datetime

class Visit(models.Model):
    _name = 'custom_crm.visit'
    _description = 'visit'

    name = fields.Char(string="descripcion")
    customer = fields.Many2one(string="cliente",
                               comodel_name='res.partner')
    date = fields.Datetime(string="fecha")
    type = fields.Selection(
        [("P", "Presencial"),
         ("W", "Whatsapp"),
         ("T", "Telefonico")],
         string="Tipo",
         required=True)
    done = fields.Boolean(string="Realizada", readonly=True)
    image = fields.Binary(string="Imagen")

    def toggle_state(self):
        self.done = not self.done

    def f_create(self):
        visit = {
            "name": "ORM test",
            "customer": 1,
            "date": str(datetime.date(2020, 8, 6)),
            "type": "P",
            "done": False
        }

        self.env["custom_crm.visit"].create(visit)

    def f_search_update(self):
        visit = self.env["custom_crm.visit"].search([("name", "=", "ORM test")])

        visit_b = self.env["custom_crm.visit"].browse([8])

        visit.write({
            "name": "ORM test write"
        })

    def f_delete(self):
        visit = self.env["custom_crm.visit"].browse([8])

        visit.unlink()

class VisitReport(models.AbstractModel):
    _name = "report.custom_crm.report_visit_card"

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report =report_obj._get_report_from_name("custom_crm.report_visit_card")

        return {
            "doc_ids": docids,
            "doc_model": self.env["custom_crm.visit"],
            "docs": self.env["custom_crm.visit"].browse(docids)
        }
    
class CustomSaleOrder(models.Model):
    _inherit = 'sale.order'

    zone = fields.Selection([('N', 'Norte'), ('C', 'Centro'), ('S', 'Sur')], string="Zona comercial")