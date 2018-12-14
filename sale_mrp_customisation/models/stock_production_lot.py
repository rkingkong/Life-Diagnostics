# -*- coding: utf-8 -*-

from odoo import fields, models


class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    removal_date = fields.Datetime(string='Expiration Date',
                                   help='This is the date on which the goods \
                                   with this Serial Number should be removed \
                                   from the stock.')
