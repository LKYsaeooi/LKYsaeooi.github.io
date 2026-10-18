---
title: Scientific software
permalink: /software/
excerpt: "Open-source electromagnetic simulation and scientific programming by Kaiyuan Li."
---

<p class="page-lead">Reusable tools for numerical optics and scientific workflows.</p>

<div class="software-feature">
<p class="eyebrow">OPEN-SOURCE CONTRIBUTION</p>
<h2>pyMESTI</h2>
<p class="software-subtitle">Electromagnetic scattering, in Python.</p>
<p>I contribute to a native Python port of MESTI.jl for frequency-domain electromagnetic scattering simulations. My work includes scalar and vectorial solvers, scattering-matrix computation, field reconstruction, and numerical verification.</p>
<ul>
<li>2D scalar/TM and 3D vectorial finite-difference frequency-domain methods</li>
<li>CPU and GPU sparse-solver backends</li>
<li>Regression checks and comparisons with the Julia implementation</li>
</ul>
<a class="primary-link" href="https://github.com/LKYsaeooi/pyMESTI">View repository <span aria-hidden="true">↗</span></a>
</div>

## Tools I work with

<dl class="skills-list">
{% for skill in site.data.profile.skills %}
<dt>{{ skill.title }}</dt><dd>{{ skill.items }}</dd>
{% endfor %}
</dl>

<p>More code and contributions are available on <a href="https://github.com/{{ site.author.github }}">GitHub</a>.</p>
