---
title: "Stories"
subtitle: "subtitle"
permalink: /stories/
social_links: false
layout: default
---

<section class="content" id="story_list">
	<div class="story_list_container">
		{% for story in site.stories %}
		<div class="row story_list_result_container">
			<div class="container box col-sm-12">
				<div class="box">
					<img src="{{ story.matrix_photo | relative_url }}" class="story_matrix_photo img-fluid" />
				</div>
			</div>
			<div>
				<div class="container box col-sm-12 bottom_section">
					<span class="name">
						<a href="{{ story.url | relative_url }}">{{ story.storyee }}</a>
					</span>
			    	<span class="quotation">
				    	<i class="fa fa-quote-left"></i>
					    {{ story.quotation }}
						<i class="fa fa-quote-right"></i>
				    </span>
				    <p class="tag_list">
				    	{% for tag in story.tags %}
				    		<a href="#">{{ tag }}</a>
			    		{% endfor %}
			    	</p>
			    </div>
			</div>
		</div>
		{% endfor%}
	</div>
</section>