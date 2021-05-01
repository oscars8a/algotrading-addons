from odoo import fields, models


class AlgoStrategie(models.Model):
    _name = 'algo.strategy'
    _description = 'Strategy'

    strategy = fields.Selection(
        [
            ('golden_cross', 'Golden Cross'),
        ],
        string='Strategy',
        required=True,
    )
    investment_id = fields.Many2one(
        comodel_name='',
        string='Investment',
    )

    def run(self, investment):
        self.investment_id = investment
        if self.strategy == 'golden_cross':
            self._golden_cross()

    def _golden_cross(self):
        pass
