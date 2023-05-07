# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class BillOfService(models.Model):
    _name = "bill_of_service"
    _inherit = ["bill_of_service"]

    task_ids = fields.One2many(
        string="Tasks",
        comodel_name="bill_of_service.task",
        inverse_name="bos_id",
        copy=True,
    )
    total_work_estimation = fields.Float(
        string="Total Work Estimation",
        compute="_compute_total_work_estimation",
        store=True,
    )

    @api.depends(
        "task_ids.work_estimation",
    )
    def _compute_total_work_estimation(self):
        for record in self:
            result = 0.0
            for task in record.task_ids:
                result += task.total_work_estimation
            record.total_work_estimation = result
