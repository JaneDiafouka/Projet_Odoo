# -*- coding: utf-8 -*-

from odoo import models, fields

class Assurance(models.Model):
    _name = 'parc.automobile.assurance'
    _description = "Objet Compagnie d'assurance"
    
    
    name = fields.Char(string="Compagnie d'assurance", required=True)
    type_assurance = fields.Selection(string="Type d'assurance", required=True,
        selection=[('tiers', 'Au tiers'),
                   ('intermediaire', 'Intermédiaire'),
                   ('tout_risque', 'Tout Risque')],
        default='tiers'
    )
    date_debut = fields.Date(string="Date de début")
    date_fin = fields.Date(string="Date de fin")
    montant_annuel = fields.Integer(string='Montant Prime Annuelle')
    voiture_ids = fields.One2many('parc.automobile.voiture', 'assurance_id', string='Liste des voitures')
    
    
    
    
    