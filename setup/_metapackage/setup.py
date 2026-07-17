import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-bill-of-service",
    description="Meta package for open-synergy-ssi-bill-of-service Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_bill_of_service',
        'odoo14-addon-ssi_bill_of_service_operating_unit',
        'odoo14-addon-ssi_bill_of_service_project',
        'odoo14-addon-ssi_bill_of_service_work_log',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
