# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Bill of Service - Project Integration",
    "version": "14.0.1.2.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        "ssi_bill_of_service",
        "ssi_task_work_log",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/bill_of_service_views.xml",
    ],
    "demo": [],
    "images": [],
}
