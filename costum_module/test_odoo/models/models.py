# -*- coding: utf-8 -*-
from odoo import models, fields

class CustomerFeedback(models.Model):
    _name = 'customer.feedback'
    _description = 'Customer Feedback'

    customer_name = fields.Char(string='Nom du Client', required=True)
    date = fields.Date(string='Date', required=True)
    invoice_reference = fields.Char(string='Référence de Facture', required=True)
    product_id = fields.Many2one('product.product', string='Produit', required=True)
    communication_method = fields.Selection([
        ('phone', 'Téléphone'),
        ('email', 'Email'),
        ('other', 'Autre'),
    ], string='Moyen de Communication', required=True)
    feedback = fields.Text(string='Feedback', required=True)

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    customer_feedback_ids = fields.One2many('customer.feedback', 'product_id', string='Feedbacks Clients')
