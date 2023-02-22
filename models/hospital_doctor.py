from odoo import fields, models


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctors'

    name = fields.Char(string='Doctor name', required=True)

    time_visit_ids = fields.Many2many(
        string='Time visit',
        comodel_name='hospital.visit',
    )
