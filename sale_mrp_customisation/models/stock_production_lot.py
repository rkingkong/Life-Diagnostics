# -*- coding: utf-8 -*-

from odoo import fields, models


class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    expiration_date = fields.Date(help="Helps to know the expiration\
        Date of product.")
