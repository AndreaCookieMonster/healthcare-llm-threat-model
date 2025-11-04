---
layout: default
title: 'Threat Catalog'
permalink: /threats/
---

# Threat Catalog

Filter by tag: `?tag=<tag>`

<ul>
{% assign tag = page.url | split:'?tag=' | last %}
{% assign qtag = site.params.tag | default: '' %}
{% assign filter = qtag | default: '' %}
{% assign tag = '' %} {# no server-side query—docs note explains query param; simple listing here #}
{% for t in site.threats %}
  <li><a href="{{ t.url | relative_url }}">{{ t.id }} — {{ t.title }}</a> — {{ t.summary }}</li>
{% endfor %}
</ul>
