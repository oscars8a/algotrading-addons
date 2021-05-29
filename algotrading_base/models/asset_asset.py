###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import fields, models


class FinancialProduct(models.Model):
    _name = 'asset.asset'
    _description = 'Asset, Stock, Currency ...'

    base = fields.Char(
        string='Base Currency',
    )
    lines_ids = fields.One2many(
        comodel_name='portfolio.line',
        inverse_name='f_product_id',
        string='Portfolio Lines',
    )
    logo = fields.Binary(
        string='Logo',
    )
    name = fields.Char(
        string='Description',
    )
    quote = fields.Char(
        string='Quote Currency',
    )
    ticker = fields.Char(
        string='Ticker',
    )
    total_amount = fields.Float(
        string='Total Amount',
    )
