# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Bill of Service To Pricelist + Operating Unit",
    "version": "14.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "contributors": [
        "Andhitia Rama <andhitia.r@gmail.com>",
    ],
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_bill_of_service",
        "ssi_operating_unit_mixin",
    ],
    "data": [
        "security/res_group/bill_of_service_pricelist.xml",
        "security/ir_rule/bill_of_service_pricelist.xml",
        "view/bill_of_service_pricelist.xml",
    ],
}
