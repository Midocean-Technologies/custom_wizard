from odoo import api, fields, models
from datetime import datetime


class appointments(models.Model):
    _name = "appointments"
    _description = "Hospital Patient Appointments"
    _rec_name = "patient_id"

    appointment_id = fields.Integer(string='Appointment Id')
    patient_id= fields.Many2one(comodel_name='patient6', string="Patient")
    a_time = fields.Datetime(string='Appointment Time')

