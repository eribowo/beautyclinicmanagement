# -*- coding: utf-8 -*-
# from odoo import http


# class /home/eribowo/beautyclinicmanagement/beautyClinicCore(http.Controller):
#     @http.route('//home/eribowo/beautyclinicmanagement/beauty_clinic_core//home/eribowo/beautyclinicmanagement/beauty_clinic_core', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//home/eribowo/beautyclinicmanagement/beauty_clinic_core//home/eribowo/beautyclinicmanagement/beauty_clinic_core/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('/home/eribowo/beautyclinicmanagement/beauty_clinic_core.listing', {
#             'root': '//home/eribowo/beautyclinicmanagement/beauty_clinic_core//home/eribowo/beautyclinicmanagement/beauty_clinic_core',
#             'objects': http.request.env['/home/eribowo/beautyclinicmanagement/beauty_clinic_core./home/eribowo/beautyclinicmanagement/beauty_clinic_core'].search([]),
#         })

#     @http.route('//home/eribowo/beautyclinicmanagement/beauty_clinic_core//home/eribowo/beautyclinicmanagement/beauty_clinic_core/objects/<model("/home/eribowo/beautyclinicmanagement/beauty_clinic_core./home/eribowo/beautyclinicmanagement/beauty_clinic_core"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/home/eribowo/beautyclinicmanagement/beauty_clinic_core.object', {
#             'object': obj
#         })

