from odoo import fields, models


class HospitalReportDiseaseWizard(models.TransientModel):
    _name = "hospital.report.disease.wizard"
    _description = "Report on diseases Wizard"

    date_from = fields.Date(string='Date from for report')
    date_to = fields.Date(string='Date to for report')

    def action_report_disease(self):
        domain = []
        date_from = self.date_from
        if date_from:
            domain += [('diagnosis_date', '>=', date_from)]
        date_to = self.date_to
        if date_to:
            domain += [('diagnosis_date', '<=', date_to)]
        result = self.env['hospital.diagnosis'].search(domain)
        diseases = {}
        diseases_list = []
        for res in result:
            if diseases.get(res.disease_id.name):
                diseases[res.disease_id.name] += 1
            else:
                diseases[res.disease_id.name] = 1
        for key, value in diseases.items():
            diseases_list.append({
                'disease': key,
                'count': value
            })
        data = {
            'diseases': diseases_list
        }
        return self.env.ref('hr_hospital.report_disease_report').report_action(self, data=data)