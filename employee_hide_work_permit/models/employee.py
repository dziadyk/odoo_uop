from odoo import _, api, exceptions, fields, models


class Employee(models.Model):
    _inherit = 'hr.employee'
