###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import fields, models


class AlgoStrategy(models.Model):
    _inherit = 'algo.strategy'

    strategy = fields.Selection(
        selection_add=[
            ('golden_cross', 'Golden Cross'),
        ]
    )

    def run(self):
        super().run()
        if self.strategy == 'golden_cross':
            return self._golden_cross()

    def _golden_cross(self):
        pass
