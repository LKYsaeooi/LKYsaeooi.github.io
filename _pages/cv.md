---
title: Curriculum vitae
permalink: /cv/
excerpt: "Kaiyuan Li — education, published articles, patent, scientific software, skills, and selected honors."
---

<p class="page-lead">Kaiyuan Li <span lang="zh-Hans">· 李开元</span></p>
<p>Optical Engineering · Shenzhen University · Shenzhen, China<br><a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a></p>

<button class="print-button" type="button" onclick="window.print()">Print / save as PDF <span aria-hidden="true">↗</span></button>

## Education

{% include education.html %}

## Research interests

Complex photonics; optical computing; AI for optics; computational imaging; scientific software development.

## Published articles

{% include publication-list.html %}

## Patent

{% include patent-list.html %}

## Open-source contributions

**[pyMESTI](https://github.com/LKYsaeooi/pyMESTI)** — native Python electromagnetic-scattering simulation software. Contributions include frequency-domain solvers, scattering matrices, field reconstruction, sparse-solver backends, and numerical verification.

## Technical skills

<dl class="skills-list">
{% for skill in site.data.profile.skills %}
<dt>{{ skill.title }}</dt><dd>{{ skill.items }}</dd>
{% endfor %}
</dl>

## Selected honors

{% for award in site.data.profile.awards %}
- {{ award }}
{% endfor %}

## Languages

English and Simplified Chinese.
