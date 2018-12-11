# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'SALE-MRP Customisation',
    'version': '11.0.1.0.0',
    'summary': 'Customisation in SALE-MRP',
    'sequence': 30,
    'description': """

    """,
    'category': 'Sales',
    'website': '',
    'images': [],
    'depends': ['mrp', 'sale_stock', 'purchase'],
    'data': [
        'views/product_views.xml',
        'views/stock_quant_views.xml',
        'views/stock_picking.xml',
        'views/mrp_product_produce_views.xml',
        'views/stock_production_lot_views.xml',
        'views/stock_move_line_views.xml',
        'report/report_deliveryslip.xml',
        'report/stock_picking_report_views.xml',
        'report/report_label_sale_order_number.xml',
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
# Part of Odoo. See LICENSE file for full copyright and licensing details.
