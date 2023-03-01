from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class HospitalHistoryDoctorChange(models.Model):
    _name = 'hospital.history.doctor.change'
    _description = 'History Doctor Change'

    doctor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        string='Doctor',
    )
    patient_id = fields.Many2one(
        comodel_name='hospital.patient',
        string='Patient',
    )
    time_date = fields.Datetime(
        string='Doctor appointment',
        default=fields.Datetime.today,
        help='doctor appointment time.',
    )
