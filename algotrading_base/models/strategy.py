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

    def start(self, investment):
        self.investment_id = investment
        self.run()

    def run(self):
        if not self.investment_id:
            return
        if self.strategy == 'golden_cross':
            return self._golden_cross()
    # inherit:
    #   super().run()
    #   if self.strategy == 'new_strategy':
    #       return self._new_strategy()

    def _golden_cross(self):
        pass
