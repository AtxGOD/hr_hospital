from odoo import fields, models


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['hospital.person.abstract.mixing']
    _description = 'Hospital Patients'

    birthday_date = fields.Date()
    age = fields.Integer(compute='calculate_date')
    passport_info = fields.Char()
    contact_person = fields.Char()
    doctor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        string='Doctor name',
    )
    visit_history_ids = fields.One2many(
        comodel_name='hospital.history.doctor.change',
        inverse_name='patient_id',
    )
    diagnosis_history_ids = fields.One2many(
        comodel_name='hospital.diagnosis',
        inverse_name='patient_id',
    )

    def calculate_date(self):
        for rec in self:
            age = 0
            if rec.birthday_date:
                age = fields.Date.today().year - rec.birthday_date.year - \
                      ((fields.Date.today().month, fields.Date.today().day) <
                       (rec.birthday_date.month, rec.birthday_date.day))
            rec.age = age

    def action_open_doctor_schedule(self):
        view_id_list = self.env.ref('hr_hospital.hospital_doctor_schedule_tree').id

        return {
            'type': 'ir.actions.act_window',
            'name': 'Doctor Schedule',
            'res_model': 'hospital.doctor.schedule',
            'domain': [('patient_id', '=', self.id)],
            'context': {},
            'views': [[view_id_list, 'tree'], [False, 'form']],
            'target': 'current',
        }

    def action_new_appointment(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'New Appointments',
            'res_model': 'hospital.doctor.schedule',
            'domain': [],
            'context': {'default_patient_id': self.id},
            'views': [[False, 'form']],
            'target': 'current',
        }
