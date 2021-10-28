# -*- coding: utf-8 -*-
# from odoo import http


# class Tmalv(http.Controller):
#     @http.route('/tmalv/tmalv/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tmalv/tmalv/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tmalv.listing', {
#             'root': '/tmalv/tmalv',
#             'objects': http.request.env['tmalv.tmalv'].search([]),
#         })

#     @http.route('/tmalv/tmalv/objects/<model("tmalv.tmalv"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tmalv.object', {
#             'object': obj
#         })
