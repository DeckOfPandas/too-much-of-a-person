---
layout: base
title: "Stories"
subtitle: "Never too many people, opinions, stories..."
permalink: /stories/
---

<section class="container blog_archive_page">
	<div class="archive_page_title">
		<h1>{{ page.title }}</h1>
		<div class="section_subtitle_centered">
			<span>{{ page.subtitle }}</span>
		</div>
	</div>
	{% if site.show_stories %}
	<div class="container-fullwidth" style="margin-top: 2em;">	
		<div class="small">
			<div class="list_to_hide_or_not_hide" data-limit='999' style="visibility:hidden">
				{% include list_stories.html %}
			</div>
		</div>
	{% else %}
	<div class="container-fullwidth" style="margin-top: 2em;padding:20px 40px;background-color:rgba(255,255,255,0.6);">	
		<p>Coming soon in 2019...</p>
		<p>We are currently editing the interviews and portraits of 100 womxn and non-binary people. They’re raw and articulate and beautiful and well worth the wait. Watch this space.</p>
	{% endif %}
	</div>		
</section>
