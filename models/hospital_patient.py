from odoo import fields, models


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patients'

    name = fields.Char(required=True)
    gender = fields.Selection(
        selection=[('male', 'Male'),
                   ('female', 'Female')],
        default='male'
    )
    disease = fields.Many2many(
        comodel_name='hospital.disease',
    )
    doctor = fields.Many2one(
        comodel_name='hospital.doctor',
    )
    description = fields.Text(
        string='Description'
    )
    time_visit = fields.Many2many(
        comodel_name='hospital.visit',
    )
