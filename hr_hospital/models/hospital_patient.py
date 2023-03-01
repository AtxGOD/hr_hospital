from odoo import fields, models


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['hospital.person.abstract.mixing']
    _description = 'Hospital Patients'

    birthday_date = fields.Date()
    age = fields.Integer(compute='calculate_date')
    passport_info = fields.Char()
    contact_person = fields.Char()
    doctor_id = fields.Many2one(comodel_name='hospital.doctor', string='Doctor name')

    def calculate_date(self):
        for rec in self:
            age = 0
            if rec.birthday_date:
                age = fields.Date.today().year - rec.birthday_date.year - \
                      ((fields.Date.today().month, fields.Date.today().day) <
                       (rec.birthday_date.month, rec.birthday_date.day))
            rec.age = age
