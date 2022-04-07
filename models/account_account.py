import logging
from odoo import api, fields, models

_logger = logging.getLogger(__name__)

class AccountAccount(models.Model):
    _inherit = "account.account"

    external_use = fields.Boolean(string='Externally used', index=True, default=False, tracking=True)