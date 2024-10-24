{
    "name": "Omegasoft C.A Retenciones municipales",
    "version": "16.0.0.0.1",
    "category": "Accounting/Localizations/Account Charts",
    "author": "Omegasoft C.A., Odoo Community Association (OCA)",
    "contributor": [
        "Naudy Mendez - naudy.mendez@omegasoftve.com",
    ],
    "website": "https://github.com/OCA/l10n-venezuela",
    "summary": "Retenciones municipales",
    "depends": [
        "l10n_ve_config_withholding",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/account_municipal_concept.xml",
        "views/res_config_settings_views.xml",
        "views/res_partner_views.xml",
        "views/account_withholding_municipal.xml",
        "views/account_move_views.xml",
        "report/account_withholding_municipal_report.xml",
        "data/mail_template_data.xml",
    ],
    "application": False,
    "installable": True,
    "auto_install": False,
    "license": "LGPL-3",
}
