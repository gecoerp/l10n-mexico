# -*- coding: utf-8 -*-
# Copyright (C) 2022 GECOERP (http://www.gecoerp.com/)
# @author: Manuel Cabañas <manuel.cabanas@gecoerp.com>
# License OPL-1 Open Content License, versión 1.0 (https://www.gnu.org/licenses/license-list.html#OpenContentL).

{
    'name': 'Catálogos para Facturación Electrónica CFDI 4.0 (Mexico)',
    'description': ''' Catálogos para Factura Electrónica CFDI 4.0 (Mexico)
    ''',
    'category': 'Localisation',
    'license': 'OPL-1',  
    'author': 'Manuel Cabañas, GECOERP',
    'website': 'https://www.gecoerp.com',  
    'version': '16.0.1',
    'maintainers': ["gecoerp"],  
    'depends': [
        'sale','account','purchase'
    ],
    'data': [  
    ],
    'pre_init_hook': 'pre_init_hook',
    'post_init_hook': 'post_init_hook',
    'application': False,
    'installable': True,
    'price':0.0,
    'currency':'USD',
}
