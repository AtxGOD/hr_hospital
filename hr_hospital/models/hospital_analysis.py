from odoo import api, fields, models


class HospitalAnalysis(models.Model):
    _name = 'hospital.analysis'
    _description = 'Analysis'

    name = fields.Char(
        string='Analysis name',
        required=True,
    )
    doctor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        string='Doctor',
    )
    patient_id = fields.Many2one(
        comodel_name='hospital.patient',
        string='Patient',
    )
    patient_number = fields.Char()

    @api.onchange('patient_id')
    def _onchange_patient_id(self):
        self.patient_number = self.patient_id.phone_number

        #test
