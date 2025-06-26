# -*- coding: utf-8 -*-
# Ce sa présence est obligatoire pour un module Odoo
{
    'name' : 'Parc Automobile',
    'version' : '1.3',
    'summary': "Ce module a été réalisé lors du TP final du cours ERP M2GL ISI",
    'sequence': -200,
    'description': """
        Ce module a été réalisé lors du TP final du cours ERP M2GL ISI avec Monsieur LAM.
        Les fonctionnalités de ce modules sont la gestion d'un ou des : 
        1. Voiture
        2. Marque
        3. Modèle
        4. Client
        5. Employé
        6. Assurance
        7. Carte Grise
        8. Contrat de Location
        9. Entretien

    """,
    'category': 'tp',
    'website': 'https://www.groupeisi.com/',
    'depends' : ['base'],
    'data': [
        'security/parc_automobile_security.xml',
        'security/ir.model.access.csv',
        'views/client.xml',
        'views/marque.xml',
        'views/modele.xml',
        'views/voiture.xml',
        'views/assurance.xml',
        'views/carte_grise.xml',
        'views/contrat_location.xml',
        'views/employe.xml',
        'views/entretien.xml',
        # 'data/cron.xml',
        'views/sequence.xml',
        'views/service.xml',
        'views/affectation.xml',
        'views/document.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'author': "Youssoupha LAM",
    'auto_install': False,
}
