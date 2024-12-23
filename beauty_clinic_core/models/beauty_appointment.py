from odoo import models, fields, api

class BeautyClinicAppointment(models.Model):
    _name = 'beauty.clinic.appointment'
    _description = "Beauty Clinic Appointment"

    name = fields.Char(string='Appointment Number', required=True, copy=False, readonly=True, default=lambda self: 'New')
    patient_id = fields.Many2one('res.partner', string="Patient", required=True)
    service_id = fields.Many2one('product.product', string="Service", required=True)
    appointment_date = fields.Datetime(string="Appointment Date", required=True)
    phone = fields.Char(string="Phone", compute='_compute_phone', inverse='_inverse_phone')
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('done', 'Done'), ('cancelled', 'Cancelled')], string="Status", readonly=True, default='draft')

    @api.depends('patient_id.phone')
    def _compute_phone(self):
        for record in self:
            record.phone = record.patient_id.phone

    def _inverse_phone(self):
        for record in self:
            record.patient_id.phone = record.phone

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('beauty.clinic.appointment') or 'New'
        result = super(BeautyClinicAppointment, self).create(vals)
        return result
