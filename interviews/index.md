---
title: "Interviews"
subtitle: "subtitle"
permalink: /interviews/
social_links: false
layout: default
---

<section class="content" id="interview_list">
	<div class="interview_list_container">
		{% for interview in site.interviews %}
				<div class="interview_list_result_container col-xs-12">
					<span>
						<a href="{{ interview.url | relative_url }}"><img src="{{ interview.matrix_photo | relative_url }}" class="img-fluid" /></a>
					</span>
					<span class="name">
						<a href="{{ interview.url | relative_url }}">{{ interview.interviewee }}</a>
					</span>
			    	<span class="quotation">
				    	<i class="fa fa-quote-left"></i>
					    {{ interview.quotation }}
						<i class="fa fa-quote-right"></i>
				    </span>
				</div>
		{% endfor%}
	</div>
</section>