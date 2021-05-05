###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import fields, models


class ExchangeExchange(models.Model):
    _name = 'exchange.exchange'
    _description = 'Exchange'

    cron_id = fields.Many2one(
        comodel_name='ir.cron',
        string='Cron',
    )
    logo = fields.Binary(
        string='Logo',
    )
    name = fields.Char(
        string='Name',
    )
