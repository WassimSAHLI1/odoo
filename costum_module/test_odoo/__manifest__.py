# __manifest__.py
{
    'name': 'test_odoo',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Module pour collecter les feedbacks des clients sur les produits achetés',
    'description': """
        Ce module permet de collecter les feedbacks des clients sur les produits achetés.
    """,
    'author': 'Wassim_sahli',
    'depends': ['base', 'product'],
    'data': [
        'views/costumer_feedback_views.xml',
        'security/ir.model.access.csv',
        'report/costumer_feedback_report.xml',
        
    ],
    'installable': True,
    'application': True,
}