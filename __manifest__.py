# -*- coding: utf-8 -*-

{
    'name': "API Exchange Rate",
    'summary': "Automatización para obtener y actualizar tasas del BCV",
    'description': """
        Módulo para consultar tasas del BCV y actualizar monedas en Odoo 18.
        - EUR funciona exactamente igual que en Odoo 17.
        - USD ahora se convierte en VES con toda la lógica heredada.
        - Cron externo llamará al método _save_exchange_rate().
    """,

    'author': "Ing. Gabriel Torrealba (Software Engineer)",
    'website': "",
    'category': 'Accounting',
    'version': '18.0.1.0',

    # Dependencias necesarias
    'depends': [
        'base',
        'account',
    ],

    # Archivos cargados
    'data': [
        'security/ir.model.access.csv',
        # decimal_precision ya no se usa en Odoo 18, pero lo dejamos vacío para trazabilidad
        'data/decimal_precision.xml',
        # El cron se elimina del módulo porque tú lo crearás manualmente
        'data/ir_cron.xml',
        'views/res_holiday.xml',
        'views/res_config_settings_views.xml',
    ],

    # Permite cargar datos sin modo demo
    'installable': True,
    'application': False,
}
