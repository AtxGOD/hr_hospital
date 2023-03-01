from odoo import fields, models


class HospitalPersonAbstractMixing(models.AbstractModel):
    _name = 'hospital.person.abstract.mixing'
    _description = 'Person model mixin'

    name = fields.Char(required=True)
    phone_number = fields.Char()
    email = fields.Char()
    photo = fields.Binary()
    gender = fields.Selection(
        selection=[('male', 'Male'),
                   ('female', 'Female')],
        default='male'
    )
