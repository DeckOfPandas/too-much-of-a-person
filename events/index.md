---
layout: default
title: "Events"
subtitle: "subtitle"
permalink: /events/
header_image: about_img.jpg
social_links: true
---

{% include upcoming_events.html %}

<h2>Previous Events:</h2>
<ol class="past-events" reversed="reversed">
{% assign current_time = site.time | date: "%s" | to_integer%}
{% assign sorted = site.events | sort: 'date' | reverse %}
{% for post in sorted %}
    {% assign start = post.date | date: "%s" | plus: 86400 | to_integer %}
    {% unless start >= current_time %}
        <li>
          <h3><a href="{{ post.url }}">{{ post.title }}</a><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%-d %B %Y" }}</time></h3>
          <h4>Held at {{ post.venue }}, {{ post.city }} and organised by {{ post.organiser | join: ' and ' }}</h4>
        </li>
    {% endunless %}
{% endfor %}
</ol>