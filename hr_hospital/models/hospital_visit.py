from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


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
    disease_id = fields.Many2one(
        comodel_name='hospital.disease',
        string='Disease',
    )
    done = fields.Boolean()
    time_date = fields.Datetime(
        string='Visit time',
        default=fields.Datetime.today,
        help='The date when the patient will visit doctor.',
    )

    @api.constrains('time_date')
    def check_time_date(self):
        for rec in self:
            result = self.env['hospital.visit'].search([
                ('doctor_id', '=', rec.doctor_id),
                ('patient_id', '=', rec.patient_id),
                ('time_date', '=', rec.time_date),
                ('id', '!=', rec.id)
            ])
            if result:
                raise ValidationError(_('Chose another time'))
