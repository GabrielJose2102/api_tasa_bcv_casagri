# -*- coding: utf-8 -*-
from odoo import models
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from bs4 import BeautifulSoup
import logging

_logger = logging.getLogger(__name__)


class ApiExchangeRate(models.Model):
    _name = "api.exchange.rate"
    _description = "Fetch BCV exchange rates"

    def requests_retry_session(self, retries=3, backoff_factor=0.3,
                               status_forcelist=(500, 502, 504), session=None):
        session = session or requests.Session()
        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        return session

    def get_bcv_rates(self):
        url = "https://bcv.org.ve"
        try:
            session = self.requests_retry_session()
            page = session.get(url, verify=False)

            if page.status_code != 200:
                return {"status": False, "error": page.reason}

            soup = BeautifulSoup(page.content, "html.parser")

            usd = float(soup.find(id="dolar")
                        .find_all(class_="col-sm-6 col-xs-6 centrado")[0]
                        .get_text().strip().replace(",", "."))

            eur = float(soup.find(id="euro")
                        .find_all(class_="col-sm-6 col-xs-6 centrado")[0]
                        .get_text().strip().replace(",", "."))

            return {"status": True, "usd": usd, "eur": eur}

        except Exception as e:
            _logger.exception("Error fetching BCV rate: %s", e)
            return {"status": False, "error": str(e)}
