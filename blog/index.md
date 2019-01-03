---
layout: page_no_header-fullwidth
title: "Scribbles"
subtitle: "Updated every Thursday"
permalink: /blog/
---

<section class="container blog_archive_page">
	<div class="archive_page_title">
		<h1>{{ page.title }}</h1>
		<div class="section_subtitle_centered">
			<span>Updated every Thursday</span>
		</div>
	</div>
	<div>
		{% include blog_list.html %}
		{% include dotdotdot.html %}
	</div>
</section>


