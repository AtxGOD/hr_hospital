# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

{
    'name': 'Hr hospital',
    'version': '15.0.1.0.0',
    'sequence': -100,
    'category': 'Extra Tools',
    'summary': """Hr hospital (Test project for odoo school).""",
    'license': 'LGPL-3',
    'author': 'Yura Pustashinskii',
    'website': 'https://github.com/AtxGOD/',
    'depends': [
        'base',
        'contacts',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_menus.xml',
        'views/hospital_patient_view.xml',
        'views/hospital_doctor_view.xml',
        'data/hospital_disease_master.xml',
    ],
    'demo': [
        'data/hospital_doctor_demo.xml',
        'data/hospital_patient_demo.xml',
    ],
    'support': 'support@garazd.biz',
    'application': True,
    'installable': True,
    'auto_install': False,
}
