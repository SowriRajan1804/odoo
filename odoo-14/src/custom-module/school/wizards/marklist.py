
from odoo import models, fields, api






class mark_edit(models.TransientModel):
    _name = 'school.wizards'


    name = fields.Char( default=lambda self: self.env['school.student'].browse([self.id]).name)

