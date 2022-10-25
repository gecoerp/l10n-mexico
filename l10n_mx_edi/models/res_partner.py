# -*- coding: utf-8 -*-

from odoo import fields, models, _, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    nombre_fiscal  = fields.Char(string='Nombre Fiscal SAT')
    residencia_fiscal = fields.Char(string='Residencia Fiscal')
    registro_tributario = fields.Char(string='Registro Tributario')
    uso_cfdi_id  =  fields.Many2one('catalogo.uso.cfdi', string='Uso CFDI')
    regimen_fiscal_id  =  fields.Many2one('catalogo.regimen.fiscal', string='Régimen Fiscal')
