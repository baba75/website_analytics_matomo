# Copyright 2015 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Matomo analytics",
    "version": "14.0",
    "author": "Therp BV,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "category": "Website",
    "summary": "Track website users using Matomo",
    "depends": ["website"],
    "data": [
        "views/website_config_settings.xml",
        "views/website.xml",
        "views/templates.xml",
    ],
    "installable": True,
}
