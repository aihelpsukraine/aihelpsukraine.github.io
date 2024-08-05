---
layout: page-floatbutton
title: Team
permalink: /team
---

# Organizers
The Harms and Risks of AI in the Military workshop is organized by volunteer students and academics. These are the organizers (in random order):

{% assign people = site.data.team | sample: site.data.team.size %}
{% for person in people %}
  {% assign side = forloop.index0 | modulo: 2 %}
    {% if side == 0 %}
      {% include team-card.html %}
    {% else %}
      {% include team-card.html %}
    {% endif %}
{% endfor %}

# Advisory Committee Members
{% assign advisors = site.data.advisors %}
{% for advisor in advisors %}
  {% include advisors-card.html %}
{% endfor %}
