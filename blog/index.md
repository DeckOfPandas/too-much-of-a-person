---
layout: page_no_header
title: "Scribbles"
subtitle: ""
permalink: /blog/
---

<section class="container-fullwidth blog_archive_page" style="margin-top:-30px">
	<div class="container-fullwidth blog_header_img">
		<img class="img-fluid" src="{{site.baseurl}}assets/images/backgrounds/blog_archive_letterbox.jpg" />
	</div>		
	<div class="blog_archive_title">
		<h1>{{ page.title }}</h1>
		<span class="author">Updated every Thursday</span>
	</div>
	<div>
		{% include blog_list.html %}
		{% include dotdotdot.html %}
	</div>
</section>
