---
title: "Light, computation<br>& imaging."
permalink: /
excerpt: "Kaiyuan Li is a master's student in Optical Engineering at Shenzhen University, with interests in photonics, optical computing, computational imaging, and scientific software."
---

<p class="eyebrow">PHOTONICS · COMPUTING · SCIENTIFIC SOFTWARE</p>

<p class="intro">I’m Kaiyuan Li <span class="chinese-name" lang="zh-Hans">（李开元）</span>, a master’s student in Optical Engineering at Shenzhen University.</p>

My interests lie at the intersection of **photonics, computation, and imaging**. I combine experimental optics, numerical simulation, and machine learning to study optical systems and develop scientific tools.

I received my B.S. in Optoelectronic Information Science and Engineering from Shenzhen University in 2024. Alongside my academic work, I enjoy building reusable software for optical experiments and electromagnetic simulation.

<div class="action-links">
  <a class="primary-link" href="{{ '/publications/' | relative_url }}">Explore publications <span aria-hidden="true">↗</span></a>
  <a href="{{ '/cv/' | relative_url }}">View CV <span aria-hidden="true">→</span></a>
</div>

## Research interests

<div class="interest-list">
{% for interest in site.data.profile.interests %}
  <div class="interest-row"><h3>{{ interest.title }}</h3><p>{{ interest.description }}</p></div>
{% endfor %}
</div>

<div class="section-heading"><h2>Selected publications</h2><a href="{{ '/publications/' | relative_url }}">All publications <span aria-hidden="true">→</span></a></div>

{% include publication-list.html limit=2 %}

<div class="closing-note"><span class="eyebrow">OPEN SCIENCE</span><p>Good scientific tools should be understandable, testable, and useful beyond a single experiment.</p><a href="{{ '/software/' | relative_url }}">Explore software <span aria-hidden="true">→</span></a></div>
