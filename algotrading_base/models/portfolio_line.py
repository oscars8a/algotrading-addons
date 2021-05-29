###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import fields, models


class PortfolioLine(models.Model):
    _name = 'portfolio.line'
    _description = 'Portfolio line'
    _order = 'portfolio_id'

    f_product_id = fields.Many2one(
        comodel_name='asset.asset',
        string='Product',
    )
    exchange_id = fields.Many2one(
        comodel_name='exchange.exchange',
        string='Exchange',
    )
    qty = fields.Float(
        string='Qty',
    )
    amount = fields.Float(
        string='Amount',
    )
    portfolio_id = fields.Many2one(
        comodel_name='portfolio.portfolio',
        string='Portfolio',
    )
