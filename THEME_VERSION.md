# Theme provenance

The layout, include, Sass, and asset directories were imported from
[Academic Pages](https://github.com/academicpages/academicpages.github.io),
commit `9c8f68fd2582abba41365ea1ca459bbb222d5a92` on 2026-10-18.
Its MIT license is retained in `LICENSE`.

The upstream theme stylesheet is precompiled using Dart Sass 1.105.2 into
`assets/css/main.css`. Its source is `_sass/academic-main.scss`, with the default
light/dark theme imports resolved. Jekyll copies the compiled CSS unchanged;
there is no dependency on a locally installed Sass compiler for normal edits.
To regenerate it after changing the upstream theme Sass:

```text
npx --yes sass@1.105.2 --load-path=_sass _sass/academic-main.scss assets/css/main.css --style=compressed --no-source-map
```

Personal styling lives in `assets/css/personal.css`. The profile, navigation,
footer, head, and script includes have local overrides. No example posts,
example publications, or unrelated source documents were imported.

The Advanced Science record uses January 1 internally only as a sorting key:
the supplied CV establishes 2025 but does not specify an exact publication day.
Only the year is displayed. Its published status and DOI were verified in the
supplied article, not inferred from the date.
Publication records are data-only (`output: false`), so no invented exact date
is emitted in article metadata or detail pages. Lists link to the publishers.
