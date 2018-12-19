# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = 'product.template'

    is_married_pair = fields.Boolean('Married Pair', copy=False,
                                     help="Helps to know which parts will be \
                                     auto-concatenated when choosing \
                                     components lots.")
