---
title: Scientific software
permalink: /software/
excerpt: "Public and private scientific software by Kaiyuan Li, spanning electromagnetic simulation, microscopy, and optical instrument control."
---

<p class="page-lead">Reusable tools for numerical optics and scientific workflows.</p>

{% include software-list.html %}

## Tools I work with

<dl class="skills-list">
{% for skill in site.data.profile.skills %}
<dt>{{ skill.title }}</dt><dd>{{ skill.items }}</dd>
{% endfor %}
</dl>

<p>More code and contributions are available on <a href="https://github.com/{{ site.author.github }}">GitHub</a>.</p>
