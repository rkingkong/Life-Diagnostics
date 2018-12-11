# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class MrpProductProduce(models.TransientModel):
    _inherit = "mrp.product.produce"
    _description = "Record Production"

    expiration_date = fields.Date(help="Helps to know the expiration\
        Date of product.")

    @api.model
    def default_get(self, fields):
        """ Compute default lot id which will be the
            concatenate lot id of the bom materials.
        """
        final_lots = []
        res = super(MrpProductProduce, self).default_get(fields)
        production = self.env['mrp.production'].browse(
            self._context['active_id'])
        if 'produce_line_ids' in fields:
            if production.product_id.is_married_pair and\
                    production.product_id.tracking == 'lot':
                for lines in res['produce_line_ids']:
                    if lines[2]['lot_id']:
                        lot_id = self.env['stock.production.lot'].browse(
                            lines[2]['lot_id'])
                        final_lots.append(lot_id.name)
                final_lot_id = self.env['stock.production.lot'].search(
                    [('name', '=', " / ".join(final_lots))])
                if not final_lot_id:
                    final_lot_id = self.env['stock.production.lot'].create(
                        {'name': " / ".join(final_lots),
                         'product_id': production.product_id.id,
                         'product_uom_id': production.product_uom_id.id,
                         })
                if 'lot_id' in fields:
                    res['lot_id'] = final_lot_id.id
        return res

    @api.multi
    def do_produce(self):
        """Inherit this method to add expiration date on lot which is created
        by default get."""
        res = super(MrpProductProduce, self).do_produce()
        if self.expiration_date and self.lot_id:
            self.lot_id.expiration_date = self.expiration_date
        return res
