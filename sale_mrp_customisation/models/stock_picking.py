# -*- encoding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import Warning

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
