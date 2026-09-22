frappe.ui.form.on("Sales Invoice", {
    refresh(frm) {
        update_patient_payable(frm);
    },

    grand_total(frm) {
        update_patient_payable(frm);
    },

    advances_add(frm) {
        update_patient_payable(frm);
    },

    advances_remove(frm) {
        update_patient_payable(frm);
    }
});

frappe.ui.form.on("Sales Invoice Advance", {
    allocated_amount(frm, cdt, cdn) {
        update_patient_payable(frm);
    }
});

function update_patient_payable(frm) {
    const patient_payable_total = flt(frm.doc.patient_payable_amount);

    (frm.doc.advances || []).forEach(row => {
        const allocated = flt(row.allocated_amount);

        const remaining = Math.max(
            0,
            patient_payable_total - allocated
        );

        frappe.model.set_value(
            row.doctype,
            row.name,
            "patient_payable_amount",
            remaining
        );
    });
}
