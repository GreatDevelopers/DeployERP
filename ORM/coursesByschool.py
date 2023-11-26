# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE
# Put files in folder: /home/cc/erp_gndec/frappe-bench/apps/noticeboard/noticeboard/www
import frappe
import frappe.www.list
from frappe import _

no_cache = 1

def get_context(context):
    # Get the variable from the URL
    nickNameSchool = frappe.request.args.get('nickNS', 'GNDEC')

    # Pass the variable to the context
    context.nickName = nickNameSchool

    context.List = frappe.get_all('Program',
            filters={'department': ['like', '%' + nickNameSchool]},
            fields=['name'],
            order_by='name asc',
            as_list=True)
