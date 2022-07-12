from __future__ import unicode_literals

import frappe

def on_submit(doc, method):
    if doc.items:
        sales_order = None
        for item in doc.items:
            if item.get("against_sales_order"):
                sales_order = item.get("against_sales_order")
                break
        if sales_order and (doc.get("shipment_id") or doc.get("carrier")):
            frappe.db.set_value('Sales Order', sales_order, dict({'shipment_id':doc.get("shipment_id"),"carrier":doc.get("carrier")}))
            frappe.db.commit()

