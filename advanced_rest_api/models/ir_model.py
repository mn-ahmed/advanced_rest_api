# -*- coding: utf-8 -*-

from odoo import fields, models


class IrModel(models.Model):
    """Enable all models to be available for API request."""

    _inherit = "ir.model"

    rest_api = fields.Boolean("REST API", default=True, help="Allow this model to be fetched through REST API")
