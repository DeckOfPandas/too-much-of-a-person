---
title: "Interviews"
subtitle: "subtitle"
permalink: /interviews/
social_links: false
layout: default
---

<section id="generic-header-card" class="content_no_padding">
	<h2>{{ page.title }}</h2>    
</section>

<section class="content">
{% assign tag_list = site.interviews | map: 'tags' | uniq %}
{% for this_tag in tag_list %}
	<h1 style="width: 80%">{{ this_tag }}</h1>
	<div class="interview_list">
		<ul>
			{% for interview in site.interviews %}
				{% if interview.tags contains this_tag %}
					<li>
	        			<a href="{{ interview.url | relative_url }}"><img src="{{ interview.thumbnail | relative_url }}" /></a>
	        			<div class="name"><a href="{{ interview.url | relative_url }}">{{ interview.interviewee }}</a></div>
	        			<div class="tags" id="tags">
		                    {% for tag in interview.tags %}   
		                        <a href="" class="tag">{{ tag }}</a>
		                    {% endfor %}
	        			</div>
		            </li>
				{% endif %}
			{% endfor%}
		</ul>
	</div>
{% endfor%}	
</section>
