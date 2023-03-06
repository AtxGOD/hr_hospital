from odoo import fields, models


class HospitalDisease(models.Model):
    _name = 'hospital.disease'
    _description = 'Disease'

    name = fields.Char(
        string='Disease name',
        required=True,
    )
    parent_id = fields.Many2one(
        'hospital.disease',
        string='Disease Category',
        ondelete="cascade",
    )
    child_ids = fields.One2many(
        comodel_name='hospital.disease',
        inverse_name='parent_id',
        string='Disease Categories',
    )
