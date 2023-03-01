from odoo import fields, models


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _inherit = ['hospital.person.abstract.mixing']
    _description = 'Hospital Doctors'

    specialty = fields.Char()
    intern = fields.Boolean()
    doctor_mentor = fields.Many2one(comodel_name='hospital.doctor',
                                    domain="[('intern', '=', False)]",
                                    )
