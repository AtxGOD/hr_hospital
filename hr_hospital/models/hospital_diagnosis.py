from odoo import fields, models


class HospitalDiagnosis(models.Model):
    _name = 'hospital.diagnosis'
    _description = 'Hospital diagnoses'

    diagnosis_date = fields.Date()
    doctor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        string='Doctor',
    )
    patient_id = fields.Many2one(
        comodel_name='hospital.patient',
        string='Patient',
    )
    disease_id = fields.Many2one(
        comodel_name='hospital.disease',
        string='Disease',
    )
    appointment = fields.Text()
