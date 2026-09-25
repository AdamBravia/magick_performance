# Deploying Magick Performance to a baked-image cluster (testerp / prod)

The app has no controllers: all behaviour lives in fixtures under `magick_performance/fixtures/` and is
applied by `bench --site <site> migrate` (fixture sync + the `after_migrate` hook in `install.py`).

## Never at runtime

Do not run `bench get-app` or `install-app --force` inside a running pod of the trial or production
cluster. Bake the new commit into the image, roll the deployment, then migrate once.

## Release 2026-09-17 (branch `fix/qa-2026-09-17`)

What changes on the site after `bench migrate`:

| Area | Change |
|---|---|
| Performance Settings | readable by roles Employee and Line Manager (Custom DocPerm); Permission Query Server Script is role/company based instead of a hard-coded e-mail allow-list |
| Performance Evaluation | permissions rebuilt: Employee create/read/write/submit on own records only (no delete/cancel/amend); Line Manager read/write/submit; HR User read/write/create/cancel; HR Manager and System Manager full. `after_migrate` removes stale permission rows that are not in the fixture |
| KRA and Goal Setup | Line Manager loses create/delete/amend; new KRA defaults the Employee to the logged-in user |
| Scoring | Before Save Server Script computes total goal / self / manager score, final score (0–5) and `performance_band` on every save; Client Script no longer parses locale-formatted strings (root cause of the 100× scores under locale `id`) |
| Auto-populate | New evaluation fills goal, self-review and manager-review rows in the browser (company/cycle taken from the KRA), no "Performance Settings undefined-…" warning |
| Blast e-mail API | only HR Manager / System Manager may trigger the cycle e-mail; no per-row commit |
| Appraisee | Property Setter `ignore_user_permissions = 1` on `Appraisee.employee` so employees can read their company's Performance Settings although it lists other employees |
| Employee links | stricter Employee link-title formatter on the two forms (Reports To no longer shows the employee's own name) |

## Steps

1. Build the image from this commit (the app folder replaces the previous one in `apps/magick_performance`).
2. Roll out; wait until all pods run the new image.
3. Once: `bench --site <site> migrate`. Watch for the line
   `magick_performance: removed N stale Custom DocPerm row(s)` — N > 0 is expected on a site that had
   the old permissions.
4. `bench --site <site> clear-cache`.
5. Smoke test as an Employee (not System Manager): open Performance → KRA and Goal Setup → New; the
   Employee is pre-filled and no "Insufficient Permission for Performance Settings" appears. Open an
   existing Performance Evaluation and Save: scores are on a 0–5 scale and the band is filled.

## Rollback

Deploy the previous image and run `bench migrate` again; the previous fixtures re-import. Scores computed
by the new Server Script stay as stored values (harmless).
