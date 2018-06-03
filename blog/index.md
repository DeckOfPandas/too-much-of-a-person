---
layout: default
title: "Blog"
subtitle: "Subtitle"
permalink: /blog/
---

<div class="blog">
	<ol class="blog-posts">
	{% assign sorted = site.blog | sort: 'date' | reverse %}
	{% for post in sorted %}
	    <li>
	      <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date_to_long_string }}</time>
	      <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
	      <h4>{{ post.subtitle }}</h4>
	      <p>{{ post.content | truncatewords:50 | strip_html }}</p>
	    </li>
	{% endfor %}
	</ol>
</div>