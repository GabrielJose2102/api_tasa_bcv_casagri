# -*- coding: utf-8 -*-
from odoo import models, fields, api

# ============================================================
# OLD CODE (Odoo 17) — COMENTADO PARA AUDITORÍA
# ============================================================
"""
from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    exchange_rate_round_method = fields.Selection([
        ('round', 'Redondear'),
        ('truncate', 'Truncar')
    ], string='Método de gestión del tipo de cambio', default='round', help='Method to round or truncate the exchange rate')

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('account.exchange_rate_round_method', self.exchange_rate_round_method)

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            exchange_rate_round_method=self.env['ir.config_parameter'].sudo().get_param('account.exchange_rate_round_method', default='round')
        )
        return res
"""

# ============================================================
# NEW CODE (Odoo 18) — SIN CAMBIOS FUNCIONALES
# ============================================================

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    exchange_rate_round_method = fields.Selection(
        [
            ("round", "Redondear"),
            ("truncate", "Truncar"),
        ],
        string="Método de gestión del tipo de cambio",
        default="round",
        help="Método para redondear o truncar la tasa de cambio obtenida del BCV.",
    )

    def set_values(self):
        super().set_values()
        self.env["ir.config_parameter"].sudo().set_param(
            "account.exchange_rate_round_method",
            self.exchange_rate_round_method,
        )

    @api.model
    def get_values(self):
        res = super().get_values()
        icp = self.env["ir.config_parameter"].sudo()
        res.update(
            exchange_rate_round_method=icp.get_param(
                "account.exchange_rate_round_method",
                default="round",
            )
        )
        return res
