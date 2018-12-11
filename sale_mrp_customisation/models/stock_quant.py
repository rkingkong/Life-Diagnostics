# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    expiration_date = fields.Date(help="Helps to know the expiration\
        Date of product.", compute="_compute_expiration_date")

    @api.multi
    def _compute_expiration_date(self):
        """Inherit this method to compute expiration date from lot_id itself."""
        for stock in self:
            if stock.lot_id and stock.lot_id.expiration_date:
                stock.expiration_date = stock.lot_id.expiration_date
