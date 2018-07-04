---
layout: page_no_header
title: "Scribbles"
subtitle: ""
permalink: /blog/
---
<section class="blog_page">

<div class="container">
	{% for post in site.blog %}
		<ul class="blog-posts"> 
		    <li>
		      <span><a href="{{ post.url | relative_url }}">{{ post.title }}</a></span>
		      <br><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date_to_long_string }}</time><span class="author">{{ post.author }}</span>
		      <p>{{ post.content | truncatewords:30 | strip_html }}</p>
		    </li>
		</ul>
	{% endfor %}
</div>


</section>