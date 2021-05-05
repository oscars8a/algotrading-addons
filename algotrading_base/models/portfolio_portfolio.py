###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import fields, models


class PortfolioPortfolio(models.Model):
    _name = 'portfolio.portfolio'
    _description = 'New Description'

    name = fields.Char(
        string='Name'
    )
    lines = fields.One2many(
        comodel_name='portfolio.line',
        inverse_name='portfolio_id',
        string='Lines',
    )
