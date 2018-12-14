# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProcurementRule(models.Model):
    _inherit = 'procurement.rule'

    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, values, group_id):
        """Inherit this method to include Sale Line variable in stock move model."""
        result = super(ProcurementRule, self)._get_stock_move_values(
            product_id, product_qty, product_uom, location_id, name, origin, values, group_id)
        product_name = self.env['product.product'].browse(
            result['product_id']).name
        result['sale_line'] = result['origin'] + '-' + product_name
        return result


class StockMove(models.Model):
    _inherit = 'stock.move'

    sale_line = fields.Char('Sale Line', help="Help us to know the Sale Order\
        number and Sale order line of that order.")


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    expiration_date = fields.Datetime(help="Helps to know the expiration\
        Date of product.")

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    picking_expiration_date = fields.Date(help="Helps to know the expiration\
        Date of product.", string="Expiration Date")

    @api.multi
    def button_validate(self):
        """Inherit this method to include expiration date if alredy present in lot_id."""
        res = super(StockPicking, self).button_validate()
        for move in self.move_line_ids:
            if move.lot_id and move.expiration_date:
                move.lot_id.removal_date = move.expiration_date
        return res
