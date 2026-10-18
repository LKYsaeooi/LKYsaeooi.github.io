# Kaiyuan Li — academic website

A personalized Academic Pages / Jekyll website prepared for GitHub Pages.

## Edit the content

- `_config.yml`: name, email, academic profiles, website address.
- `_data/profile.yml`: education, skills, broad interests, selected honors.
- `_data/patents.yml`: verified patent grant details, shared by publications and CV.
- `_data/software.yml`: software introductions; private entries have no URL.
- `index.md`: short biography and home page.
- `_publications/`: one Markdown record per published article.
- `_pages/`: publications, software, public CV, contact, and 404 page.
- `_data/navigation.yml`: navigation destinations.
- `assets/css/personal.css`: all custom design overrides.
- `images/monogram.svg`: initials used in place of an unverified portrait.

Publication lists share one include, and the CV shares structured education and
skills data. Navigation, reading, and contact links work without JavaScript.
The CV page has a print / save-as-PDF button and a dedicated print stylesheet.

## Preview and check

With Ruby 3.3 and Bundler installed, run from this folder:

```powershell
bundle install
bundle exec jekyll build
python scripts/check_site.py
bundle exec jekyll serve --host 127.0.0.1
```

Open `http://127.0.0.1:4000/`. `_site/` contains the real generated website.
The theme CSS is already compiled. Regular content and styling edits do not
require a separate Sass installation; see `THEME_VERSION.md` for regeneration.

For a preview without installing anything, open `.preview/index.html`, or unzip
`Kaiyuan-Li-website-preview.zip` and open `index.html`. This preview includes
working file-based navigation. Regenerate both delivery archives after a build:

```powershell
python scripts/package_site.py
```

## Publish on GitHub Pages

1. Use the GitHub account `LKYsaeooi` and create an empty repository named
   `LKYsaeooi.github.io`. If that repository already exists, review it first.
2. Put **only the contents of this website folder** in that repository.
   Do not upload the parent PhD folder or application documents.
3. Use the `main` branch. In repository **Settings → Pages → Build and deployment**,
   choose **GitHub Actions** as the source.
4. The included workflow builds Jekyll, checks the generated output, and deploys.
   When it succeeds, the intended address is `https://lkysaeooi.github.io/`.

For a repository with another name, update `_config.yml` (`repository`, `url`,
and `baseurl`) before publishing. The prepared configuration targets the account
root site. A successful deployment in GitHub Actions confirms publication.

## Content scope

The site contains education, broad interests, published articles, a granted
invention patent, scientific software, skills, selected honors, and academic contact links. It excludes
specific doctoral project proposals, unpublished manuscripts, the full private
application CV, phone / WeChat details, referee details, identity documents,
transcripts, recommendation letters, and research statements.
Private software is described briefly without repository links or specific
research methods or results.

Private editorial provenance is retained locally and excluded from the public
repository. See `THEME_VERSION.md` for the pinned theme revision; it is excluded
from the generated website.

Official references: [Academic Pages](https://academicpages.github.io/) and
[GitHub Pages setup](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site).
