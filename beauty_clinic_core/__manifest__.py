{
    'name': "Beauty Clinic Management",
    'version': '1.0',
    'depends': ['base', 'hr', 'sale', 'stock', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'security/beauty_clinic_security.xml',
        'views/appointment_views.xml',
        'views/patient_views.xml',
        'views/beauty_clinic_menus.xml',
        'data/beauty_appointment_data.xml',
    ],
    'installable': True,
    'application': True,
}
