from odoo import fields, models


class HospitalVisit(models.Model):
    _name = 'hospital.visit'
    _description = 'Patient visits'

    doctor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        string='Doctor',
    )
    patient_id = fields.Many2one(
        comodel_name='hospital.patient',
        string='Patient',
    )
    time = fields.Date(
        string='Visit time',
        default=fields.Date.today,
        help='The date when the patient will visit doctor.',
    )
