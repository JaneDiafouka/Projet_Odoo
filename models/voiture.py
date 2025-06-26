# -*- coding: utf-8 -*-

from odoo import models, fields

class Voiture(models.Model):
    _name = 'parc.automobile.voiture'
    _description = "Objet Voiture"
    
    
    name = fields.Char(string='Nom', required=True)
    photo = fields.Binary(string='Photo')
    immatriculation = fields.Char(string='Immatriculation')
    couleur = fields.Selection(string='Couleur', required=True,
        selection=[('white', 'Blanche'),
                   ('black', 'Noire'),
                   ('yellow', 'Jaune'),
                   ('red', 'Rouge'),
                   ('blue', 'Bleu')],
        default='white'
    )
    date_service = fields.Date(string="Date de mise en service")
    kilometrage = fields.Char(string='Kilometrage')
    etat = fields.Selection(string='Etat', required=True,
        selection=[('neuf', 'Neuf'),
                   ('service', 'En Service'),
                   ('hs', 'Hors Service'),],
        default='service'
    )
    type_vehicule = fields.Selection([
        ('voiture', 'Voiture'),
        ('utilitaire', 'Utilitaire'),
        ('moto', 'Moto'),
        ('camion', 'Camion'),
    ], string="Type de véhicule", required=True)

    statut = fields.Selection([
        ('en_service', 'En service'),
        ('hors_service', 'Hors service'),
        ('maintenance', 'En maintenance'),
        ('vendu', 'Vendu'),
    ], string="Statut", required=True, default='en_service')


    devise = fields.Selection([
        ('FCFA', 'FCFA'),
        ('EURO', 'EURO(s)'),
        ('DOLLAR', 'DOLLAR(s)')
    ], string="devise", required=True, default='FCFA')

    date_dernier_entretien = fields.Date(string='Dernier Entretien',default=fields.Date.today)
    prochaine_visite_technique = fields.Date(string='Prochaine Visite')
    documets_ids = fields.Many2many('ir.attachment', 'attachement_100', 'attachment_id', string="Papiers de Douane")
    modele_id = fields.Many2one('parc.automobile.modele', string="Modèle Associé", required=False)
    carte_grise_id = fields.Many2one('parc.automobile.carte.grise', string="Carte Grise Associée", required=False)
    assurance_id = fields.Many2one('parc.automobile.assurance', string="Assurance", required=False)
    montant_location = fields.Integer(string="Prix de location")
    description = fields.Text(string='Description')
    centre_id = fields.Many2one('parc.automobile.centre', string="Centre/Service associé")
    document_ids = fields.One2many('parc.automobile.document', 'voiture_id', string='Liste des Documents')
    
    
    
    
    