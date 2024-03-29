# pylint: disable=manifest-required-author
# Copyright 2017 Humanytek.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': "Compromise Products",
    'summary': """
    Allows to reserve, liberate and compromise raw materials for each product
    of a sale order.
    """,
    'author': "Humanytek",
    'website': "http://www.humanytek.com",
    'license': 'AGPL-3',
    'category': 'Sales',
    'version': '14.0.0.0.1',
    'depends': [
        'sale',
        'stock',
        'mrp_sale_info',
        'product_brand',
    ],
    'data': [
        'security/ir.model.access.csv',
        "views/stock_location_views.xml",
        'views/sale_view.xml',
        'views/product_compromise_view.xml',
        'wizard/compromise_view.xml',
    ],
    'demo': [
    ],
    'installable': True,
}
