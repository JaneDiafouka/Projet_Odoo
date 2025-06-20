# -*- coding: utf-8 -*-

from odoo import models, fields

class Entretien(models.Model):
    _name = 'parc.automobile.entretien'
    _description = "Objet Entretien"
    
    
    name = fields.Char(string="Numéro d'entretien", required=True)
    voiture_id = fields.Many2one('parc.automobile.voiture', string="Liste des voitures")
    type_entretien = fields.Selection(string="Type d'entretien", required=True,
        selection=[('vidange', 'Vidange'),
                   ('change', 'Changement des pièces'),
                   ('revision', 'Révision')],
        default='vidange'
    )
    date_entretien = fields.Date(string="Date d'entretien")
    cout = fields.Integer(string='Côut')
    date_prochain_entretien = fields.Date(string="Prochain Entretien")
    description_entretien = fields.Text(string="Description")
    
    
    
    
    
    