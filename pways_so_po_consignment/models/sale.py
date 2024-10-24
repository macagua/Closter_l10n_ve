from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"  # pylint: disable=consider-merging-classes-inherited

    is_consignments = fields.Boolean(
        string="Consignment", help="Consignments", copy=False
    )
    is_consignments_purchase = fields.Boolean(
        string="Purchase Consignments", help="Consignments", copy=False
    )
    analytic_id = fields.Many2one(
        "account.analytic.account", string="Consignment Account", copy=False
    )

    def action_confirm(self):
        res = super(__class__, self).action_confirm()
        consignments_data = []
        if self.is_consignments and self.analytic_id:
            for line in self.order_line:
                d_vals = {
                    "product_id": line.product_id.id,
                    "description": line.product_id.name,
                    "consignment_type": "income",
                    "qty": line.product_uom_qty,
                    "uom_id": line.product_id.uom_id.id,
                    "unit_price": line.price_unit,
                    "sales": line.price_unit,
                    "sale_id": self.id,
                    "purchase_order_line_id": line.purchase_order_line_id.id,
                }
                consignments_data.append((0, 0, d_vals))
            self.analytic_id.consignment_ids = consignments_data
        return res

    @api.constrains("order_line")
    def _check_product_line(self):
        analytic_id = self.analytic_id
        if analytic_id:
            for record in self.order_line:
                if (
                    record.product_id.id
                    not in analytic_id.purchase_order_id.order_line.mapped(
                        "product_id"
                    ).ids
                ):
                    raise ValidationError(
                        _(
                            "Product %s not found in this consignment purchase order"
                            % (record.product_id.name)
                        )
                    )
                else:
                    purchase_line_ids = (
                        analytic_id.purchase_order_id.order_line.filtered(
                            lambda x: x.product_id.id == record.product_id.id
                        )
                    )
                    qty = sum(purchase_line_ids.mapped("product_qty"))
                    if record.product_uom_qty > qty:
                        raise ValidationError(
                            _(
                                "Order qty of product %s is more "
                                "then consignment purchase order"
                                % (record.product_id.name)
                            )
                        )
