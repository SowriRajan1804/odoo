# -*- coding: utf-8 -*-

from odoo import models, fields, api


class category(models.Model):
    _name = 'category.category'
    _description = 'category.category'

    name = fields.Char()

class ticket(models.Model):
    _inherit = 'movies.movies'

    count = fields.Integer(string="Ticket_Count")
    price = fields.Float(string="Ticket_Price")
    total = fields.Float(compute="total_price",store=True)

    @api.depends('count','price')
    def total_price(self):
        for record in self:
            record.total = float(record.count) * float(record.price)
