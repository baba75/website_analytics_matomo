# Copyright 2015 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    has_Matomo_analytics = fields.Boolean(
        "Matomo Analytics", related="website_id.has_Matomo_analytics", readonly=False
    )
    Matomo_analytics_id = fields.Integer(
        related="website_id.Matomo_analytics_id", readonly=False
    )
    Matomo_analytics_host = fields.Char(
        related="website_id.Matomo_analytics_host", readonly=False
    )
