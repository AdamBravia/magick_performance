app_name = "magick_performance"
app_title = "Magick Performance"
app_publisher = "Adam Bravia Suksma"
app_description = "Custom Performance Evaluation Module made for GMI"
app_email = "adam@globalmagicko.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "magick_performance",
# 		"logo": "/assets/magick_performance/logo.png",
# 		"title": "Magick Performance",
# 		"route": "/magick_performance",
# 		"has_permission": "magick_performance.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/magick_performance/css/magick_performance.css"
# app_include_js = "/assets/magick_performance/js/magick_performance.js"

# include js, css files in header of web template
# web_include_css = "/assets/magick_performance/css/magick_performance.css"
# web_include_js = "/assets/magick_performance/js/magick_performance.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "magick_performance/public/scss/website"

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
# app_include_icons = "magick_performance/public/icons.svg"

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
# 	"methods": "magick_performance.utils.jinja_methods",
# 	"filters": "magick_performance.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "magick_performance.install.before_install"
# after_install = "magick_performance.install.after_install"
after_migrate = "magick_performance.install.after_migrate"

# Uninstallation
# ------------

# before_uninstall = "magick_performance.uninstall.before_uninstall"
# after_uninstall = "magick_performance.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "magick_performance.utils.before_app_install"
# after_app_install = "magick_performance.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "magick_performance.utils.before_app_uninstall"
# after_app_uninstall = "magick_performance.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "magick_performance.notifications.get_notification_config"

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
# 		"magick_performance.tasks.all"
# 	],
# 	"daily": [
# 		"magick_performance.tasks.daily"
# 	],
# 	"hourly": [
# 		"magick_performance.tasks.hourly"
# 	],
# 	"weekly": [
# 		"magick_performance.tasks.weekly"
# 	],
# 	"monthly": [
# 		"magick_performance.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "magick_performance.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "magick_performance.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "magick_performance.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "magick_performance.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["magick_performance.utils.before_request"]
# after_request = ["magick_performance.utils.after_request"]

# Job Events
# ----------
# before_job = ["magick_performance.utils.before_job"]
# after_job = ["magick_performance.utils.after_job"]

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
# 	"magick_performance.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


fixtures = [
    {"dt": "Custom Field", "filters": [["name", "in", ["Employee-custom_nickname"]]]},
    {"dt": "Role", "filters": [["name", "in", ["Line Manager"]]]},
    {"dt": "Module Def", "filters": [["module_name", "in", ["Magick Performance"]]]},
    {"dt": "DocType", "filters": [["module", "in", ["Magick Performance"]]]},
    {"dt": "Client Script", "filters": [["module", "in", ["Magick Performance"]]]},
    {"dt": "Server Script", "filters": [["module", "in", ["Magick Performance"]]]},
    {"dt": "Workflow", "filters": [["document_type", "in", ["Performance Evaluation", "KRA and Goal Setup"]]]},
    {"dt": "Workflow State", "filters": [["workflow_state_name", "in", ["Draft", "Submitted by Employee", "Pending Manager Approval", "Approved", "Rejected", "Manager Reviewed", "Finalized", "Communicated", "Revision Requested"]]]},
    {"dt": "Workflow Action Master", "filters": [["workflow_action_name", "in", ["Submit Self Review", "Submit to HR", "Approve", "Reject", "Finalize", "Communicate to Employee", "Request Revision", "Revise", "Submit for Approval", "Approve Revision", "Reject Revision"]]]},
    {"dt": "Notification", "filters": [["document_type", "in", ["Performance Evaluation", "KRA and Goal Setup"]]]},
    {"dt": "Property Setter", "filters": [["doc_type", "in", ["KRA and Goal Setup", "Performance Evaluation", "Appraisee"]]]},
    {"dt": "Custom DocPerm", "filters": [["parent", "in", ["KRA and Goal Setup", "Performance Evaluation"]]]},
]
