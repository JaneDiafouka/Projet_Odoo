# -*- coding: utf-8 -*-

from odoo import models, fields

class Client(models.Model):
    _name = 'parc.automobile.client'
    _description = "Objet Client"
    
    
    name = fields.Char(string='Nom et Prénom', required=True)
    adresse = fields.Char(string='Adresse')
    telephone = fields.Char(string='Téléphone')
    email = fields.Char(string='E-mail')
    
    
    
    
    