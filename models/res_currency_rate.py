# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import date
import logging

_logger = logging.getLogger(__name__)


class CurrencyRateCreator(models.Model):
    _inherit = "res.currency.rate"

    @api.model
    def actualizar_tasa_bcv_ves(self):
        """Consulta BCV desde api.exchange.rate y crea las líneas aquí."""

        api_model = self.env["api.exchange.rate"]
        resp = api_model.get_bcv_rates()

        if not resp.get("status"):
            _logger.error("Error consultando BCV: %s", resp.get("error"))
            return

        usd_rate = resp["usd"]
        eur_rate = resp["eur"]
        today = date.today()

        ves_currency = self.env["res.currency"].search([("name", "=", "VES")], limit=1)
        eur_currency = self.env.ref("base.EUR")

        if not ves_currency:
            _logger.error("VES currency not found")
            return

        company_id = self.env.ref("base.main_company").id

        # Crear línea VES
        self.create({
            "name": today,
            "company_rate": usd_rate,
            "currency_id": ves_currency.id,
            "company_id": company_id,
        })

        # Crear línea EUR
        self.create({
            "name": today,
            "company_rate": usd_rate / eur_rate,
            "currency_id": eur_currency.id,
            "company_id": company_id,
        })

        _logger.info("Tasas creadas correctamente para %s", today)
