###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import fields, models


class AlgoStrategie(models.Model):
    _name = 'algo.strategy'
    _description = 'Strategy'

    strategy = fields.Selection(
        [
            ('hold', 'Hold And Buy'),
        ],
        string='Strategy',
        required=True,
    )
    investment_id = fields.Many2one(
        comodel_name='',
        string='Investment',
    )

    def start(self, investment):
        self.investment_id = investment
        self.run()

    def run(self):
        if not self.investment_id:
            return
        if self.strategy == 'hold':
            return self._hold()

    def _hold(self):
        pass
