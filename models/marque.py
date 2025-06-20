# -*- coding: utf-8 -*-

from odoo import models, fields

class Marque(models.Model):
    _name = 'parc.automobile.marque'
    _description = "Objet Marque"
    
    
    name = fields.Char(string='Nom', required=True)
    pays_id = fields.Many2one('res.country', string="Pays d'origine", required=True)
    date_creation = fields.Date(string="Année de fondation")
    modele_ids = fields.One2many('parc.automobile.modele', 'marque_id', string='Liste des modèles')
    
    
    
    
    
    