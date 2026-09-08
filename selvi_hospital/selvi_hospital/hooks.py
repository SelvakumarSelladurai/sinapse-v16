app_name = "selvi_hospital"
app_title = "Selvi Hospital Custom App"
app_publisher = "CubaAR"
app_description = "Customizations for Selvi Hospital"
app_email = "cubaar29@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "selvi_hospital",
# 		"logo": "/assets/selvi_hospital/logo.png",
# 		"title": "Selvi Hospital Custom App",
# 		"route": "/selvi_hospital",
# 		"has_permission": "selvi_hospital.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/selvi_hospital/css/selvi_hospital.css"
# app_include_js = "/assets/selvi_hospital/js/selvi_hospital.js"

# include js, css files in header of web template
# web_include_css = "/assets/selvi_hospital/css/selvi_hospital.css"
# web_include_js = "/assets/selvi_hospital/js/selvi_hospital.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "selvi_hospital/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "selvi_hospital/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "selvi_hospital.utils.jinja_methods",
# 	"filters": "selvi_hospital.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "selvi_hospital.install.before_install"
# after_install = "selvi_hospital.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "selvi_hospital.uninstall.before_uninstall"
# after_uninstall = "selvi_hospital.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "selvi_hospital.utils.before_app_install"
# after_app_install = "selvi_hospital.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "selvi_hospital.utils.before_app_uninstall"
# after_app_uninstall = "selvi_hospital.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "selvi_hospital.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "selvi_hospital.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"selvi_hospital.tasks.all"
# 	],
# 	"daily": [
# 		"selvi_hospital.tasks.daily"
# 	],
# 	"hourly": [
# 		"selvi_hospital.tasks.hourly"
# 	],
# 	"weekly": [
# 		"selvi_hospital.tasks.weekly"
# 	],
# 	"monthly": [
# 		"selvi_hospital.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "selvi_hospital.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "selvi_hospital.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "selvi_hospital.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "selvi_hospital.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["selvi_hospital.utils.before_request"]
# after_request = ["selvi_hospital.utils.after_request"]

# Job Events
# ----------
# before_job = ["selvi_hospital.utils.before_job"]
# after_job = ["selvi_hospital.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"selvi_hospital.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []



fixtures = [
    {
        "dt": "Workspace Sidebar",
        "filters": [
            ["name", "in", [
                "Reception",
                "Nurse",
                "Practitioner",
                "Lab",
                "Pharmacy",
                "Emergency"
            ]]
        ]
    }
]


# Recent Patient Encounter customizations
fixtures.append({
    "dt": "Property Setter",
    "filters": [
        ["name", "in", [
            "Patient Encounter-title-in_list_view",
            "Patient Encounter-practitioner_name-in_list_view",
            "Patient Encounter-encounter_date-in_list_view",
            "Patient Encounter-patient_name-in_list_view",
            "Patient Encounter-main-title_field"
        ]]
    ]
})

fixtures.append({
    "dt": "Property Setter",
    "filters": [
        ["name", "in", [
            "Patient Encounter-title-in_list_view",
            "Patient Encounter-practitioner_name-in_list_view",
            "Patient Encounter-encounter_date-in_list_view",
            "Patient Encounter-patient_name-in_list_view",
            "Patient Encounter-main-title_field",
            "Patient Appointment-title-in_list_view",
            "Patient Appointment-practitioner_name-in_list_view",
            "Patient Appointment-main-title_field"
        ]]
    ]
})

fixtures.append({
    "dt": "Custom Field",
    "filters": [
        ["name", "in", [
            "Patient Appointment-custom_patient_type"
        ]]
    ]
})
