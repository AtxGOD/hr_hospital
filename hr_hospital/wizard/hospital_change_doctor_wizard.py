from odoo import fields, models


class HospitalChangeDoctorWizard(models.TransientModel):
    _name = "hospital.change.doctor.wizard"
    _description = "Change Doctor Wizard"

    doctor_id = fields.Many2one(comodel_name='hospital.doctor', required=True)

    def action_change_doctor(self):
        for id in self._context['active_ids']:
            domain = [('id', '=', id)]
            res = self.env['hospital.patient'].search(domain, limit=1)
            res.doctor_id = self.doctor_id
