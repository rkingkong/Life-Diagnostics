# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = 'product.template'

    is_married_pair = fields.Boolean('Married Pair', copy=False,
                                     help="Helps to know which parts will be \
                                     auto-concatenated when choosing \
                                     components lots.")
