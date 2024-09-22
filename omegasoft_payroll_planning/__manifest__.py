{
    "name": "Omegasoft C.A Planning & Payroll",
    "version": "16.0.0.0.16",
    "category": "Human Resources/Planning",
    "application": False,
    "author": "Omegasoft C.A",
    "contributor": [
        "Daniel Ospino - daniel.ospino@omegasoftve.com",
        "Rene Gomez - rene.gomez@omegasoftve.com",
    ],
    "website": "https://github.com/macagua/Closter_l10n_ve",
    "summary": "Planning & Payroll",
    "description": """
    Customizations to Planning & Payroll.
    """,
    "depends": [
        "base",
        "hr",
        "planning",
        "hr_work_entry",
        "hr_work_entry_contract_enterprise",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/hr_job.xml",
        "views/work_shifts.xml",
        "views/planning_slot_template.xml",
        "views/planning_slot.xml",
        "views/planning_role.xml",
        "views/hr_work_entry_type.xml",
    ],
    "installable": True,
    "auto_install": False,
    "license": "LGPL-3",
}
