# -*- coding: utf-8 -*-
from odoo import http

# class DietFacts(http.Controller):
#     @http.route('/diet_facts/diet_facts/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/diet_facts/diet_facts/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('diet_facts.listing', {
#             'root': '/diet_facts/diet_facts',
#             'objects': http.request.env['diet_facts.diet_facts'].search([]),
#         })

#     @http.route('/diet_facts/diet_facts/objects/<model("diet_facts.diet_facts"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('diet_facts.object', {
#             'object': obj
#         })