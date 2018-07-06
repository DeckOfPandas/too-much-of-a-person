---
layout: page_no_header
title: "Scribbles"
subtitle: ""
permalink: /blog/
---

<section class="container-fullwidth blog_archive_page">
	<div class="container-fullwidth blog_header_img">
		<img class="img-fluid" src="{{site.baseurl}}assets/images/backgrounds/blog_archive_letterbox.jpg" />
	</div>		
	<div class="blog_archive_title">
		<h1>{{ page.title }}</h1>
		<span class="author">Updated every Thursday</span>
	</div>
	<div>
		{% assign sorted = site.blog | sort: 'date' | reverse %}
		{% for post in sorted %}
			<ul class="blog_archive_list"> 
			    <li>
			      <span><a href="{{ post.url | absolute_url }}">{{ post.title }}</a></span>
			      <br><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date_to_long_string }}</time><span class="author">{{ post.author }}</span>
			      <p>{{ post.content | truncatewords:50 | strip_html }}</p>
			    </li>
			</ul>
		{% endfor %}
	</div>
</section>
