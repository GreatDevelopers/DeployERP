# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE

import frappe
import frappe.www.list
from frappe import _

no_cache = 1
startRecord = 0;
pageLength = 25;

def get_context(context):
        context.current_user = frappe.get_doc("User", frappe.session.user)
        context.show_sidebar = False
        context.Rai = frappe.get_all('Program',
                filters={'department': ['like', '%eachin%']},
                fields=['name'],
                order_by='name asc',
                start=startRecord,
                page_length=pageLength,
                as_list=True)
