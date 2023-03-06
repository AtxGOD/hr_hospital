# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

{
    'name': 'Hr hospital',
    'version': '15.0.1.0.0',
    'category': 'Extra Tools',
    'summary': """Hr hospital (Test project for odoo school).""",
    'license': 'LGPL-3',
    'author': 'Yura Pustashinskii',
    'website': 'https://github.com/AtxGOD/odoo_school_hr_hospital',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/hospital_change_doctor_wizard_view.xml',
        'wizard/hospital_report_disease_wizard_view.xml',
        'wizard/hospital_change_visit_time_view.xml',
        'views/hospital_menus.xml',
        'views/hospital_diagnosis_views.xml',
        'views/hospital_analysis_views.xml',
        'views/hospital_disease_views.xml',
        'views/hospital_patient_views.xml',
        'views/hospital_doctor_schedule_views.xml',
        'views/hospital_doctor_views.xml',
        'data/hospital_disease_data.xml',
        'report/disease_report.xml',
        'report/report.xml',
    ],
    'demo': [
        'data/hospital_doctor_demo.xml',
        'data/hospital_patient_demo.xml',
    ],
    'support': 'vista2990@gmail.com',
    'application': True,
    'installable': True,
    'auto_install': False,
}
