# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class BillOfServicePricelist(models.Model):  # pylint: disable=too-few-public-methods
    _name = "bill_of_service_pricelist"
    _inherit = [
        "bill_of_service_pricelist",
        "mixin.single_operating_unit",
    ]
