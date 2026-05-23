# -*- coding: utf-8 -*-
from odoo import api, models, fields

# ============================================================
# OLD CODE (Odoo 17) — COMENTADO PARA AUDITORÍA
# ============================================================
"""
from odoo import api, models, fields

class Holiday(models.Model):
    _name = 'res.holiday'
    _description = 'Días Feriados'

    holiday_date = fields.Date(string='Fecha Feriado', required=True)
    name = fields.Char(string='Descripción', required=True)
    year = fields.Integer(string='Año', compute='_compute_year', store=True)

    @api.depends('holiday_date')
    def _compute_year(self):
        for holiday in self:
            if holiday.holiday_date:
                holiday.year = holiday.holiday_date.year
"""

# ============================================================
# NEW CODE (Odoo 18) — SIN CAMBIOS FUNCIONALES
# ============================================================

class Holiday(models.Model):
    _name = "res.holiday"
    _description = "Días Feriados"

    holiday_date = fields.Date(
        string="Fecha Feriado",
        required=True,
    )
    name = fields.Char(
        string="Descripción",
        required=True,
    )
    year = fields.Integer(
        string="Año",
        compute="_compute_year",
        store=True,
    )

    @api.depends("holiday_date")
    def _compute_year(self):
        for holiday in self:
            holiday.year = holiday.holiday_date.year if holiday.holiday_date else False
