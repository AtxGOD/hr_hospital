from odoo import fields, models


class HospitalChangeVisitTimeWizard(models.TransientModel):
    _name = "hospital.change.visit.time.wizard"
    _description = "Change visit time"

    doctor_id = fields.Many2one(comodel_name='hospital.doctor')
    disease_id = fields.Many2one(
        comodel_name='hospital.disease',
        string='Disease',
    )
    time_date = fields.Datetime(
        string='Visit time',
        default=fields.Datetime.today,
        help='The date when the patient will visit doctor.',
    )

    def action_change_visit_time(self):
        result = self.env['hospital.visit'].search([
            ('patient_id.id', '=', self._context['active_id']),
            ('done', '=', False),
        ])

        if result:
            result[0].time_date = self.time_date
        else:
            self.env['hospital.visit'].create({
                'doctor_id': self.doctor_id.id,
                'disease_id': self.disease_id.id,
                'time_date': self.time_date,
                'patient_id': self._context['active_id'],
            })
