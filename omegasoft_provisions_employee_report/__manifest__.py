{
    "name": "Omegasoft C.A Provisions Employee Report",
    "version": "16.0.0.0.16",
    "category": "Human Resources/Employee",
    "application": False,
    "author": "Omegasoft C.A., Odoo Community Association (OCA)",
    "contributor": [
        "Daniel Ospino - daniel.ospino@omegasoftve.com",
        "Rene Gomez - rene.gomez@omegasoftve.com",
    ],
    "website": "https://github.com/OCA/l10n-venezuela",
    "summary": "Provisions Employee Report.",
    "depends": [
        "base",
        "hr_contract",
        "omegasoft_contract_social_benefit_liabilities_fields",
        "omegasoft_contract_vacations_fields",
    ],
    "data": [
        "security/ir.model.access.csv",
        "report/hr_employee_provisions_report.xml",
    ],
    "installable": True,
    "auto_install": False,
    "license": "LGPL-3",
}
