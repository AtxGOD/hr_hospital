from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class HospitalDoctorSchedule(models.Model):
    _name = 'hospital.doctor.schedule'
    _description = 'Doctor Schedule'

    doctor_id = fields.Many2one(
        comodel_name='hospital.doctor',
    )
    patient_id = fields.Many2one(
        comodel_name='hospital.patient',
    )
    reception_time = fields.Integer(string='Time')
    reception_date = fields.Date(
        string='Reception date',
        default=fields.Datetime.today,
    )

    @api.constrains('reception_time')
    def check_reception_time(self):
        for rec in self:
            result = self.env['hospital.doctor.schedule'].search([
                ('reception_time', '=', rec.reception_time),
                ('reception_date', '=', rec.reception_date),
                ('id', '!=', rec.id)
            ])
            if result:
                raise ValidationError(_('Chose another time'))

    def name_get(self):
        result = []
        for rec in self:
            name = rec.doctor_id.name
            result.append((rec.id, name))
        return result
