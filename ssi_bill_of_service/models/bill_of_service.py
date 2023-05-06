# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class BillOfService(models.Model):
    _name = "bill_of_service"
    _description = "Bill Of Service"
    _inherit = ["mixin.master_data"]

    name = fields.Char(
        help="Bill of Service's name",
    )
    code = fields.Char(
        help="Bill of Service's code. Duplicate not allowed",
    )
    type_id = fields.Many2one(
        string="Type",
        comodel_name="bill_of_service_type",
        required=True,
        ondelete="restrict",
    )
    allowed_product_category_ids = fields.Many2many(
        string="Allowed Product Categories",
        comodel_name="product.category",
        related="type_id.allowed_product_category_ids",
        store=False,
    )
    allowed_product_tmpl_ids = fields.Many2many(
        string="Allowed Product Templates",
        comodel_name="product.template",
        related="type_id.allowed_product_tmpl_ids",
        store=False,
    )
    product_tmpl_id = fields.Many2one(
        string="Product Template",
        comodel_name="product.template",
        required=True,
        ondelete="restrict",
    )
    product_id = fields.Many2one(
        string="Product",
        comodel_name="product.product",
        ondelete="restrict",
    )
    product_qty = fields.Float(
        string="Product Qty",
        default=1.0,
        required=True,
    )
    product_uom_id = fields.Many2one(
        string="UoM",
        comodel_name="uom.uom",
        required=True,
        ondelete="restrict",
    )
