# Part of Odoo. See LICENSE file for full copyright and licensing details.

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

    expiration_date = fields.Date(help="Helps to know the expiration\
        Date of product.")

    def _action_done(self):
        """Inherit this method to include Expiration date in lot id generated."""
        super(StockMoveLine, self)._action_done()
        for stock in self:
            if stock.lot_id and stock.expiration_date:
                stock.lot_id.expiration_date = stock.expiration_date

    @api.onchange('lot_id')
    @api.depends('lot_id')
    def onchange_lot_id(self):
        """Inherit this method to include expiration date if alredy present in lot_id."""
        self.expiration_date = False
        if self.lot_id and self.lot_id.expiration_date:
            self.expiration_date = self.lot_id.expiration_date
