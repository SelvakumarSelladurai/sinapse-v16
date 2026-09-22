frappe.ui.form.on("Discharge Summary", {
    setup(frm) {
        // Remove the standard status filter
        frm.set_query("inpatient_record", function () {
            return {};
        });
    },

    refresh(frm) {
        // Make Inpatient Record non-mandatory
        frm.set_df_property("inpatient_record", "reqd", 0);
        frm.refresh_field("inpatient_record");
    }
});
