from odoo import fields, models


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _inherit = ['hospital.person.abstract.mixing']
    _description = 'Hospital Doctors'

    specialty = fields.Char()
    intern = fields.Boolean()
    doctor_mentor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        domain="[('intern', '=', False)]",
    )
    intern_ids = fields.One2many(
        comodel_name='hospital.doctor',
        inverse_name='doctor_mentor_id',
        string="Interns",
    )
    patients_ids = fields.One2many(
        comodel_name='hospital.patient',
        inverse_name='doctor_id',
        string="Patients",
    )

    test_data = fields.Date(default=fields.Datetime.today)

    def action_new_appointment(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'New Appointments',
            'res_model': 'hospital.doctor.schedule',
            'domain': [],
            'context': {'default_doctor_id': self.id},
            'views': [[False, 'form']],
            'target': 'current',
        }
