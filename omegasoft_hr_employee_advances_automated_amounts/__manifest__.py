{
    "name": "Omegasoft - HR Employee Advances, Loans and Discounts Automated Amounts",
    "version": "16.0.0.0.1",
    "category": "Human Resources/Contracts",
    "application": False,
    "author": "Omegasoft C.A., Odoo Community Association (OCA)",
    "contributor": [
        "Gabriel Peraza - gabriel.peraza@omegasoftve.com",
    ],
    "website": "https://github.com/OCA/l10n-venezuela",
    "summary": """
    Fill employee advance form lines according to their benefits automatically""",
    "depends": [
        "hr",
        "hr_payroll",
        "omegasoft_payroll_res_config_settings",
        "omegasoft_hr_employee_code",
        "omegasoft_hr_employee_advances_loans_discounts",
    ],
    "data": [
        "views/hr_employee_advances_loans_discounts.xml",
    ],
    "installable": True,
    "auto_install": False,
    "license": "LGPL-3",
}
