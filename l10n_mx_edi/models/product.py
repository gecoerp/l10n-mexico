# -*- coding: utf-8 -*-

from odoo import fields, models, api,_

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    unidad_medida_id = fields.Many2one('unidad.medida', string='Unidad SAT')
    clave_producto_id = fields.Many2one('producto.servicio', string='Clave Producto/Servicio SAT')
    objetoimp = fields.Selection(
        selection=[('01', 'No objeto de impuesto'), 
                   ('02', 'Sí objeto de impuesto'), 
                   ('03', 'Sí objeto del impuesto y no obligado al desglose'),],
        string='Objeto Impuesto', default = '02',
    )
