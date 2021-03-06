import csv

with open('input-all.csv', mode='r') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	line_count = 1
	for row in csv_reader:

		# Set names of columns
		# First name
		firstname_raw = row["interviewee"].lower()
		firstname = firstname_raw.strip()
		firstname_nospaces = firstname_raw.split(' ')
		firstname_nohyphens = firstname_raw.split('-')

		if len(firstname_nospaces) > 1:
			print "MULTIPLE FIRST NAMES"
  			firstname = "%s%s" % (firstname_nospaces[0], firstname_nospaces[1])	

		if len(firstname_nohyphens) > 1:
			print "HYPHEN IN FIRST NAME"
  			firstname = "%s%s" % (firstname_nohyphens[0], firstname_nohyphens[1])
			
		print "firstname '%s'" % firstname_raw

		# Surname
		if row["Surname"] != "":
			if row["Surname"] != "?":
				surname = row["Surname"][0].lower().strip()
			else:
				surname = ""
		else:
			surname = ""
		
		# Slug
		if "ecca" in firstname:
			slug = "rebecca-n"
			print "\n\n\n\nEXCEPTION\nRebecca N slug '%s' \n\n\n\n" % slug
		else:
			slug = "%s-%s" % (firstname, surname) # NB: Re-used below in output to file contents
		

		# Year
		year = row["date"].strip()	
		
		# Quotation
		quotation_clean_ends = row["quotation"].strip('\"')
		quotation_clean_whole = quotation_clean_ends.replace('\"','\'')
		quotation = quotation_clean_whole
		
		# Short quotation
		short_quotation_clean_ends = row["Short quote for thumb"].strip('\"')
		short_quotation_clean_whole = short_quotation_clean_ends.replace('\"','\'')
		short_quotation = short_quotation_clean_whole

		# Audio URL
		audio_raw = row["Souncloud link"]
		audio_url_prepend = "https://w.soundcloud.com/player/?url="
		audio_url_append = "&color=%23fe0000&inverse=false&auto_play=false&show_user=true"
		audio_url = "%s%s%s" % (audio_url_prepend, audio_raw, audio_url_append)

		# Video URL
		video_url = row["Embed Link"]

		# Tags
		tags_string = row["tags"].replace('#','\n  - ')
		tags = tags_string
		

		# PRINT TO CONSOLE
		print('Line %d, slug %s' % (line_count, slug))
		output_filename = "output_files//%s.md" % slug
		print('output_filename: %s' % output_filename )


		# PRINT TO FILE

		# Create output file
		f = open(output_filename, "w") # NB: overwrites entire file every time

		# Print standard header for config file
		f.write('---\n')

		# Print parameters we don't vary
		f.write('published: true\n')
		f.write('layout: story\n')

		# First name
		if firstname == "john": # Special handling for this person's name, see Issue 462
			firstname = "John Dior"
			print "\n\n\n\nEXCEPTION\nJohn Dior firstname '%s'" % firstname

		try:
			f.write('firstname: %s\n' % firstname_raw)
		except:
			f.write('firstname: FIRSTNAME\n')

		# Surname
		try:
			f.write('surname: %s\n' % surname)
		except:
			f.write('surname: SURNAME\n')

		# Slug -- as per above
		try:
			f.write('slug: %s\n' % slug)
		except:
			f.write('slug: SLUG\n')

		# Year
		try:
			f.write('year: %s\n' % row["date"].strip())
		except:
			f.write('year: YEAR\n')

		# Quotation
		try:
			f.write('quotation: "%s"\n' % quotation)
		except:
			f.write('quotation: QUOTATION\n')

		# Short quotation
		try:
			f.write('short_quotation: "%s"\n' % short_quotation)
		except:
			f.write('short_quotation: SHORT QUOTATION\n')

		# Audio URL
		try:
			f.write('audio_url: %s\n' % audio_url)
		except:
			f.write('audio_url: AUDIO URL\n')

		# Video URL
		try:
			f.write('video_url: %s\n' % video_url)
		except:
			f.write('video_url: VIDEO URL\n')	

		# Tags		
		try:
			f.write('tags: %s' % tags)
		except:
			f.write('tags: TAGS\n')

		# Print standard footer for config file
		f.write('\n---')

		line_count = line_count + 1
		print ""