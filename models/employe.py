# -*- coding: utf-8 -*-

from odoo import models, fields

class Employe(models.Model):
    _name = 'parc.automobile.employe'
    _description = "Objet Employé"
    
    
    name = fields.Char(string='Nom et Prénom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    nom = fields.Char(string='Nom de famille', required=True)
    adresse = fields.Char(string='Adresse')
    telephone = fields.Char(string='Téléphone')
    email = fields.Char(string='E-mail')
    poste = fields.Char(string='Poste')
    departement = fields.Char(string='Département')
    date_embauche = fields.Date(string="Date d'embauche", required=True)
    voiture_id = fields.Many2one('parc.automobile.voiture', string="Voiture affectée")
    