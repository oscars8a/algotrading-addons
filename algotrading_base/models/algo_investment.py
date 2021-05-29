###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import fields, models


class AlgoInvestment(models.Model):
    _name = 'algo.investment'
    _description = 'Investment'

    exchange_id = fields.Many2one(
        comodel_name='exchange.exchange',
        string='Exchange',
    )
    f_produc_id = fields.Many2one(
        comodel_name='asset.asset',
        string='Product',
    )
    name = fields.Char(
        string='Description',
    )
    status = fields.Selection(
        [
            ('benchmark', 'Benchmark'),
            ('production', 'Production'),
            ('test', 'Test'),
        ],
        string='status',
    )
    strategy_id = fields.Many2one(
        comodel_name='algo.strategy',
        string='Strategy',
    )
    temporality = fields.Selection(
        [
            ('1m', '1m'),
            ('5m', '5m'),
            ('15m', '15m'),
            ('30m', '30m'),
            ('1h', '1h'),
            ('2h', '2h'),
            ('4h', '4h'),
            ('6h', '6h'),
            ('12h', '12h'),
            ('1d', '1d'),
            ('3d', '3d'),
            ('1s', '1s'),
            ('1Ms', '1M'),
        ],
        string='Temporality',
    )
    ticker = fields.Char(
        related='f_produc_id.ticker',
    )
