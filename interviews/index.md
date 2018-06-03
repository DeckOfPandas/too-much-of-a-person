---
title: "Interviews"
subtitle: "subtitle"
permalink: /interviews/
social_links: false
layout: default
---

<section class="content" id="interview_list">
	{% assign tag_list = site.interviews | map: 'tags' | uniq %}
	{% for this_tag in tag_list %}
	<div class="interview_list_container">
		<div class="col-md-12 ">
			<h1>{{ this_tag }}</h1>
		</div>
		{% for interview in site.interviews %}
			{% if interview.tags contains this_tag %}
				<div class="interview_list_result_container col-md-3 col-sm-6 col-xs-8 col-xs-offset-2">
					<span>
						<a href="{{ interview.url | relative_url }}"><img src="{{ interview.thumbnail | relative_url }}" class="img-fluid" /></a>
					</span>
					<span class="name">
						<a href="{{ interview.url | relative_url }}">{{ interview.interviewee }}</a>
					</span>
					<span id="tags">
		                {% for tag in interview.tags %}   
		                    <a href="">{{ tag }}</a>
		                {% endfor %}
		            </span>
				</div>
			{% endif %}
		{% endfor%}
	</div>
	{% endfor%}	
</section>