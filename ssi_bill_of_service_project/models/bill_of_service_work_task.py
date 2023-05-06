# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class BillOfServiceTask(models.Model):
    _name = "bill_of_service.task"
    _description = "Bill Of Service Task"
    _order = "sequence, bos_id, id"

    sequence = fields.Integer(
        string="Sequence",
        required=True,
        default=10,
    )
    bos_id = fields.Many2one(
        string="Bill Of Service",
        comodel_name="bill_of_service",
        required=True,
        ondelete="cascade",
    )
    name = fields.Char(
        string="Task Summary",
        required=True,
    )
    type_id = fields.Many2one(
        string="Type",
        comodel_name="task.type",
        required=True,
    )
    type_category_id = fields.Many2one(
        string="Type Category",
        comodel_name="task.type_category",
        related="type_id.category_id",
        store=True,
    )
    allowed_product_ids = fields.Many2many(
        string="Allowed Products",
        comodel_name="product.product",
        related="type_id.work_log_product_ids",
        store=False,
    )
    product_id = fields.Many2one(
        string="Product",
        comodel_name="product.product",
        required=True,
    )
    difficulty = fields.Selection(
        string="Difficulty",
        index=True,
        selection=[
            ("0", "Low"),
            ("1", "Medium"),
            ("2", "High"),
            ("3", "Very High"),
        ],
        default="0",
        required=True,
    )
    num_of_parellel = fields.Integer(
        string="Num of Parallel Task",
        required=True,
        default=1,
    )
    work_estimation = fields.Float(
        string="Work Estimation",
    )

    @api.onchange(
        "type_id",
        "difficulty",
        "num_of_parellel",
    )
    def onchange_work_estimation(self):
        self.work_estimation = 0.0
        if self.type_id:
            standard_work_estimation = self.type_id.work_estimation
            field_name = "work_estimation_offset_" + self.difficulty
            offset_work_estimation = getattr(self.type_id, field_name)
            self.work_estimation = (
                standard_work_estimation + offset_work_estimation
            ) * self.num_of_parellel

    @api.onchange(
        "type_id",
    )
    def onchange_name(self):
        self.name = False
        if self.type_id:
            self.name = self.type_id.name

    @api.onchange(
        "type_id",
    )
    def onchange_product_id(self):
        self.product_id = False
