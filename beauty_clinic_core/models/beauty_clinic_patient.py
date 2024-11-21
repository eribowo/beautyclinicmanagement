from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    status = fields.Selection([
        ('patient', 'Pasien'),
        ('non_patient', 'Non Pasien'),
    ], string='Status')
