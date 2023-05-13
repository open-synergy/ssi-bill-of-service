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
    parent_id = fields.Many2one(
        string="Parent BoS",
        comodel_name="bill_of_service",
    )
    child_ids = fields.One2many(
        string="Child BoS",
        comodel_name="bill_of_service",
        inverse_name="parent_id",
    )
    all_structure_ids = fields.Many2many(
        string="All Bill of Service",
        comodel_name="bill_of_service",
        compute="_compute_all_structure_ids",
        store=False,
    )
    component_ids = fields.Many2many(
        string="Component Bill of Service",
        comodel_name="bill_of_service",
        relation="rel_bos_to_component",
        column1="bos_id",
        column2="component_id",
    )
    product_tmpl_id = fields.Many2one(
        string="Product Template",
        comodel_name="product.template",
        required=False,
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

    def _compute_all_structure_ids(self):
        for record in self:
            result = self.env["bill_of_service"]
            parent = record.parent_id
            while parent:
                result += parent
                parent = parent.parent_id
            record.all_structure_ids = result + record

            if record.component_ids:
                for component in record.component_ids:
                    record.all_structure_ids += component.all_structure_ids
