# -*- coding: utf-8 -*-

from odoo import fields, models


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    removal_date = fields.Datetime(
        related='lot_id.removal_date', store=True, string='Expiration Date')
    note = fields.Text(string='Notes', help="Helps to add note on the quant.")
