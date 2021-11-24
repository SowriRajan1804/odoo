# -*- coding: utf-8 -*-
import datetime

from odoo import models, fields, api


class pubg(models.Model):
    _name = 'pubg.pubg'
    _description = 'pubg.pubg'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    in_game_name = fields.Char()
    bday = fields.Date(default=datetime.datetime.now())
    age = fields.Integer(compute="age_calc",store=True)
    most_game_played = fields.Selection([
        ('erangle','ERANGLE'),('sanhok','SANHOK'),('miramer','MIRAMER'),('vikendi','VIKENDI')
    ])
    acc_number = fields.Integer ()
    kd_ratio = fields.Float()
    real_name = fields.Char()
    clan = fields.Char()
    tier = fields.Char(compute="_set_tier",store=True)
    top_10 = fields.Integer()
    wins = fields.Integer()
    rp = fields.Integer(default = "1")
    popularity = fields.Char()
    mode = fields.Many2one("res.partner",string="modes")
    achievements = fields.Integer()
    player_level = fields.Integer()
    evo_level = fields.Integer()
    looking_for = fields.Selection([('teamates', 'TEAMATES'), ('crew', 'CREW')])
    role_1 = fields.Selection([
        ('camper', 'CAMPER'), ('gunslinger', 'GUNSLINGER'), ('sniper', 'SNIPER'), ('shotgun_lover', 'SHOTGUN_LOVER'),
        ('lazy_burn', 'LAZY_BURN'),('tactician', 'TACTICIAN')])
    role_2 = fields.Selection([
        ('camper', 'CAMPER'), ('gunslinger', 'GUNSLINGER'), ('sniper', 'SNIPER'), ('shotgun_lover', 'SHOTGUN_LOVER'),
        ('lazy_burn', 'LAZY_BURN'), ('tactician', 'TACTICIAN')])
    online_days = fields.Selection([('weekdays', 'WEEKDAYS'), ('weekend', 'WEEKEND'), ('everyday', 'EVERYDAY')])
    online_time = fields.Selection([
        ('morning', 'MORNING'), ('afternoon', 'AFTERNOON'), ('evening', 'EVENING'), ('allday', 'ALLDAY')
    ])



    # def submit(self):
    #      for record in self:
    #          print(record)
    #          # test2=record.env['mobilelegends.mobilelegends'].search([
    #          #     ('name','=','siva')
    #          # ])
    #          # print(test2)
    #          test2 = record.env['mobilelegends.mobilelegends'].browse([4, 5])
    #          # test2.write(
    #          #     {'name': 'siva','value':100}
    #          #
    #          # )
    #          print(test2)
    #          # test = record.create([
    #          #     {'in_game_name':'lokesh','clan':'asdf'}
    #          #
    #          # ])
    #          # test = record.browse([2])
    #          # test2 = test.copy()
    #          # print(test2)


    @api.depends('bday')
    def age_calc(self):
        for record in self:
            age = datetime.datetime.now().year - record.bday.year
            record.age=age
            # print(age)
            # print("gyjgjkgyjhfthytujktuyjnyh")

    @api.depends('top_10')
    def _set_tier(self):
        tir = {0:'Silver', 1:'Gold',2:'Platinum', 3:'Diamond', 4:'Crown', 5:'Ace', 6:'Conqueror'}
        #     if record.top_10 < 100:
        #         record.tier = 'silver'
        #     elif record.top_10 < 200:
        #         record.tier = 'gold'
        #     elif record.top_10 < 300:
        #         record.tier = 'platinum'
        #     elif record.top_10 < 400:
        #         record.tier = 'diamond'
        #     elif record.top_10 < 500:
        #         record.tier = 'crown'
        #     elif record.top_10 < 600:
        #         record.tier = 'ace'
        #     elif record.top_10 < 700:
        #         record.tier = 'conqueror'
        #     else:
        #         record.tier = 'MASTER'


        for record in self:
            record.tier = tir.get(int(record.top_10/100), 'MASTER')

class viznu(models.Model):
    _inherit = "account.move"

    checking = fields.Many2one("sale.order",string="checkmate")

