{
    "name": "Omegasoft C.A Employee ARI report",
    "version": "16.0.0.0.1",
    "category": "Human Resources/Contracts",
    "author": "Omegasoft C.A., Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/l10n-venezuela",
    "depends": [
        "hr",
        "omegasoft_payroll_res_config_settings",
        "omegasoft_hr_employee_family_information",
        "omegasoft_contract_parafiscal_contributions_fields",
        "omegasoft_hr_employee_code",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/ir_cron_data.xml",
        "views/ari_employee_setting_views.xml",
        "views/custom_payroll_res_config_settings.xml",
        "views/hr_employee.xml",
    ],
    "assets": {
        "web.assets_backend": ["omegasoft_employee_ari/static/src/js/yearpicker.js"],
    },
    "license": "LGPL-3",
}
