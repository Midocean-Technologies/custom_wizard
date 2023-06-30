from odoo import api, fields, models
from datetime import date


class patient(models.Model):
    _name = "patient"
    _description = "Hospital patient"
    _rec_name = "name"

    patient_id = fields.Integer(string="patient Id")
    name = fields.Char(string="Name")
    dob = fields.Date(string="Date Of Birth")
    age = fields.Integer(string="Age", compute='_compute_age', tracking=True)
    ph_no = fields.Char(string="Phone Number")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], String="Gender")

    @api.depends('dob')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.dob:
                rec.age = today.year - rec.dob.year
            else:
                rec.age = 1
