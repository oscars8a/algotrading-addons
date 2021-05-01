from odoo import fields, models


class FinancialProduct(models.Model):
    _name = 'financial.product'
    _description = 'Financial Product, Stock, Currency ...'

    name = fields.Char(
        string='Description',
    )
    ticker = fields.Char(
        string='Ticker',
    )
    total_amount = fields.Float(
        string='Total Amount',
    )
    lines_ids = fields.One2many(
        comodel_name='portfolio.line',
        inverse_name='f_product_id',
        string='Portfolio Lines',
    )
