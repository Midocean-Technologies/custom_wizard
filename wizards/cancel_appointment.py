from odoo import api, fields, models
from datetime import datetime


class cancelappointment(models.TransientModel):
    _name = "cancel.appointments"
    _description = "Cancel Appointments Wizard"
    _rec_name = "appointment_id"

    appointment_id = fields.Many2one(comodel_name='appointments',string='Appointment')

    def action_cancel(self):
        return

