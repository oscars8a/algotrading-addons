###############################################################################
#
#    Óscar Soto Ochoa (@oscars8a)
#    Copyright (C) 2021-Today Oscar Soto Ochoa <oscars8a.github.io>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
{
    'name': 'Algotrading Base',
    'summary': 'Algorithmic trading for Odoo.',
    'author': 'Oscar Soto Ochoa',
    'website': 'https://github.com/oscars8a',
    'license': 'LGPL-3',
    'category': 'Trading',
    'version': '14.0.1.0.0',
    'data': [
        'data/exchanges.xml',
        'security/ir.model.access.csv',
        'views/algo_investment.xml',
        'views/algo_strategy.xml',
        'views/algotrading_base.xml',
        'views/exchange_exchange.xml',
        'views/financial_product.xml',
        'views/portfolio_line.xml',
        'views/portfolio_portfolio.xml',
    ],
    'application': True,
}
