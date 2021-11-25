# -*- coding: utf-8 -*-

from odoo import models, fields, api


class movies(models.Model):
    _name = 'movies.movies'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'movies.movies'

    name = fields.Char(string="Movie Name",required=1)
    actor = fields.Char(string="Actor")
    actress = fields.Char(string="Actress")
    date = fields.Date(string="Release Date")
    time = fields.Integer(string="Duration in Minutes",required=1)
    abouts = fields.Text(string="Storyline")
    part = fields.Selection([('one','1'),('two','2'),('three','3'),('four','4'),('five','5')])
    ticket = fields.Selection([('silver','Silver'),('gold','Gold'),('diamond','Diamond'),('platinum','Platinum')],string="Ticket_Type")
    budget = fields.Char(string="Budget")
    director = fields.Char(string="Director")
    category = fields.Many2many("category.category", string="Category")

    def action_confirm(self):
        for rec in self:
            listofmovies = self.env['movies.movies'].search([])
            print("movies..", listofmovies)

    def confirm(self):
        pass
