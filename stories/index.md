---
layout: page_no_header
title: "Stories"
subtitle: "subtitle if wanted"
permalink: /stories/
---

<section class="container-fullwidth blog_archive_page">
	<div class="container-fullwidth blog_header_img">
		<img class="img-fluid" src="{{site.baseurl}}assets/images/backgrounds/blog_archive_letterbox.jpg" />
	</div>		
	<div class="blog_archive_title">
		<h1>{{ page.title }}</h1>
		<span class="author">{{ page.subtitle }}</span>
	</div>
	<div>
		{% include story_list.html %}
		{% include dotdotdot.html %}
	</div>
</section>
