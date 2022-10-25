# -*- coding: utf-8 -*-

from odoo import fields, models,_
import ast

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    
    TipoDeComprobante = fields.Selection(
        selection=[('I', 'Ingreso'), 
                   ('E', 'Egreso'),
                   ('T', 'Traslado'),
                   ('P', 'Nómina'),],
        string=_('Tipo de Comprobante'),
    )
    
    forma_pago_id  =  fields.Many2one('catalogo.forma.pago', string='Forma de Pago')
    
    methodo_pago = fields.Selection(
        selection=[('PUE', _('Pago en una sola exhibición')),
                   ('PPD', _('Pago en parcialidades o diferido')),],
        string=_('Método de Pago'), 
    )
    
    uso_cfdi_id  =  fields.Many2one('catalogo.uso.cfdi', string='Uso CFDI')
    
    estatus_cfdi = fields.Selection(
        selection=[
            ('no_cargado', 'No Cargado'),
            ('por_validar', 'Pendiente de Validar'),
            ('no_encontrado', 'No Encontrado'),
            ('vigente', 'Vigente'),
            ('cancelado', 'Cancelado')
        ],
        string='Estatus del CFDI',
        default='no_cargado',
        copy=False)
        
    error_cfdi = fields.Char(string='Descripción del Error', copy=False)
    
    version_cfdi = fields.Char(string='Versión ')
    
    cfdi_uuid = fields.Char('Folio Fiscal SAT UUID', copy=False)
    
    serie = fields.Char(string='Serie')
    
    folio = fields.Char(string='Folio')
    
    rfc_emisor = fields.Char(string='RFC Emisor')
    rfc_receptor = fields.Char(string='RFC Receptor')
    fecha_de_emision = fields.Char(string='Fecha de Emisión')
    fecha_certificacion = fields.Char(string='Fecha y Hora de Certificación')
    fecha_cancelacion = fields.Char(string='Fecha de Cancelación')
    
    moneda = fields.Char(string='Moneda')
    tipocambio = fields.Char(string='Tipo de cambio')
    
    cfdi_relacionado = fields.Char(
        string='CFDI Relacionado',
        copy=False)
        
    tipo_relacion = fields.Selection(
        selection=[('01', 'Nota de crédito de los documentos relacionados'), 
                   ('02', 'Nota de débito de los documentos relacionados'), 
                   ('03', 'Devolución de mercancía sobre facturas o traslados previos'),
                   ('04', 'Sustitución de los CFDI previos'), 
                   ('05', 'Traslados de mercancías facturados previamente'),
                   ('06', 'Factura generada por los traslados previos'), 
                   ('07', 'CFDI por aplicación de anticipo'),],
        string='Tipo de Relación',
    )
        
    archivo_cfdi_id = fields.Many2one('ir.attachment', string='Archivo CFDI', copy=False)
    documento_cfdi = fields.Binary()
    
    # vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:         
