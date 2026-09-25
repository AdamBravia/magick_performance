"""Install / migrate hooks for Magick Performance.

The app ships its behaviour as fixtures (Client Scripts, Server Scripts, Custom DocPerm rows,
Property Setters, Workflows). `bench migrate` imports fixtures by record name, which ADDS rows but never
removes rows that exist on the site under a different name. For Custom DocPerm that matters: a site that
still holds the pre-2026-09-17 permission rows (e.g. Employee with delete/cancel/amend on Performance
Evaluation) would keep them next to the new ones, and Frappe unions permissions per role.

`after_migrate` therefore deletes Custom DocPerm rows for this app's doctypes that are not part of the
shipped fixture file, so every site ends up with exactly the permission set in
`fixtures/custom_docperm.json`.
"""
import json
import os

import frappe

APP_DOCTYPES = ("KRA and Goal Setup", "Performance Evaluation")


def _fixture_rows():
	path = os.path.join(os.path.dirname(__file__), "fixtures", "custom_docperm.json")
	if not os.path.exists(path):
		return None
	with open(path, encoding="utf-8") as f:
		return json.load(f)


def reconcile_custom_docperms():
	rows = _fixture_rows()
	if rows is None:
		return
	shipped = {r["name"] for r in rows if r.get("parent") in APP_DOCTYPES}
	if not shipped:
		return
	stale = frappe.get_all(
		"Custom DocPerm",
		filters={"parent": ["in", APP_DOCTYPES], "name": ["not in", list(shipped)]},
		pluck="name",
	)
	for name in stale:
		frappe.delete_doc("Custom DocPerm", name, ignore_permissions=True, force=True)
	if stale:
		for dt in APP_DOCTYPES:
			frappe.clear_cache(doctype=dt)
		print(f"magick_performance: removed {len(stale)} stale Custom DocPerm row(s) not in fixtures")


def after_migrate():
	reconcile_custom_docperms()
