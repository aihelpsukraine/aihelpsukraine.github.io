---
layout: page-floatbutton
title: Team
permalink: /team
---
Harms and Risks of AI in the Military Workshop is organized by volunteer students and academics. These are the organisers (in random order):

{% assign people = site.data.team | sample: site.data.team.size %}
{% for person in people %}
  {% assign side = forloop.index0 | modulo: 2 %}
    {% if side == 0 %}
      {% include team-card.html %}
    {% else %}
      {% include team-card.html %}
    {% endif %}
{% endfor %}
