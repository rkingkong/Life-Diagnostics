# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, models
from odoo.exceptions import UserError


class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'

    @api.multi
    def record_production(self):
        """To create the final lot id which will be the\
        concatenate of the bom lot ids"""
        for workorder in self:
            if workorder.product_id.is_married_pair and\
                    workorder.product_id.tracking == 'lot':
                final_lots = []
                for move_line in self.active_move_line_ids:
                    if move_line.product_id.tracking != 'none' and \
                            not move_line.lot_id:
                        raise UserError(
                            _('You should provide a lot/serial number \
                                for a component'))
                    final_lots.append(move_line.lot_id.name)
                final_lot_id = self.env['stock.production.lot'].create(
                    {'name': " / ".join(final_lots),
                     'product_id': workorder.product_id.id,
                     'product_uom_id': workorder.product_uom_id.id,
                     })
                workorder.write({
                    'final_lot_id': final_lot_id.id})
        return super(MrpWorkorder, self).record_production()
