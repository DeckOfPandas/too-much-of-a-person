import csv

with open('participants-newsheet-2019-03-07-0127-only_seven.csv', mode='r') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	line_count = 1
	for row in csv_reader:
		
		# Generate slug
		slug = "%s-%s" % (row["firstname"].lower().strip(), row["surname"][0].lower()) # NB: Re-used below in output to file contents
		print(f'Line {line_count}, slug {slug}')
		output_filename = "%s.md" % slug
		# print(f'output_filename: {output_filename}')
		
		# Create file for output
		f = open(output_filename, "w") # NB: overwrites entire file every time

		# Print standard header for config file
		f.write('---\n')

		# Print parameters we don't vary
		f.write('published: true\n')
		f.write('layout: story\n')

		# First name
		try:
			f.write(f'firstname: {row["firstname"]}\n')
		except:
			f.write(f'firstname: FIRSTNAME\n')

		# Slug -- as per above
		f.write(f'slug: %s\n' % slug)

		# Surname
		try:
			f.write(f'surname: {row["surname"].strip()}\n')
		except:
			f.write(f'surname: SURNAME\n')

		# Year
		try:
			f.write(f'year: {row["year"].strip()}\n')
		except:
			f.write(f'year:\n')

		# Quotation
		quotation_clean_ends = row["quotation"].strip('\"')
		quotation_clean_whole = quotation_clean_ends.replace('\"','\'')
		try:
			f.write(f'quotation: "%s"\n' % quotation_clean_whole)
		except:
			f.write(f'quotation:\n')

		# Short quotation
		short_quotation_clean_ends = row["short_quotation"].strip('\"')
		short_quotation_clean_whole = short_quotation_clean_ends.replace('\"','\'')
		try:
			f.write(f'short_quotation: "%s"\n' % short_quotation_clean_whole)
		except:
			f.write(f'short_quotation:\n')

		# Audio URL
		try:
			f.write(f'audio_url: {row["audio_url"]}\n')
		except:
			f.write(f'audio_url:\n')

		# Video URL
		try:
			f.write(f'video_url: {row["video_url"]}\n')
		except:
			f.write(f'video_url:\n')	

		# Tags		
		try:
			tags_string = "tags: %s" % (row["tags"].replace('#','\n  - '))
			f.write(f'%s' % tags_string)
		except:
			f.write(f'tags:\n')
		f.write(f'\n')

		# Print standard footer for config file
		f.write('---')

		line_count += 1
	print(f'Processed {line_count} lines, including header row.')
