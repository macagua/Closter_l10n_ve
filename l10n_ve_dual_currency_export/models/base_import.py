from odoo import models


class Import(models.TransientModel):
    _inherit = "base_import.import"

    def execute_import(self, fields, columns, options, dryrun=False):
        self = self.with_context(convert_date_to_utc=True)
        return super(__class__, self).execute_import(fields, columns, options, dryrun)
