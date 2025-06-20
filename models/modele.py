# -*- coding: utf-8 -*-

from odoo import models, fields

class Modele(models.Model):
    _name = 'parc.automobile.modele'
    _description = "Objet Modèle de voiture" 
    
    
    name = fields.Char(string='Nom', required=True)
    marque_id = fields.Many2one('parc.automobile.marque', string="Marque Associée", required=True)
    type_carrosserie  = fields.Selection(string='Type de Carrosserie', required=True,
        selection=[('berline', 'Berline'),
                   ('suv', 'SUV'),
                   ('44', '4x4')]
    )
    consomation = fields.Char(string='Consomation')
    puissance = fields.Char(string='Puissance')
    
    
    
    
    
    