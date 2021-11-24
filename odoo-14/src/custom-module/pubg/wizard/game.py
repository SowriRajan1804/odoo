# -*- coding: utf-8 -*-

from odoo import models, fields, api


class game(models.TransientModel):
    _name = 'game'
    _description = 'game_game'


    name = fields.Char(string="Name")