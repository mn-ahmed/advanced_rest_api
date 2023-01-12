# -*- coding: utf-8 -*-

from odoo import fields, models

class Users(models.Model):
    _inherit = "res.users"
    token_ids = fields.One2many("api.access.token", "user_id", string="Access Tokens")
