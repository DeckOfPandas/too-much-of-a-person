# HOWTO: Add a story to the website

## Overview

To add a Story to the website, you need to do three things:
 1. Decide on a unique slug for that Story -- more below
 1. Create a new markdown file on our GitHub repo -- template and details below
 1. Upload at least the main photo and thumbnail images for that Story to our GitHub repo, with optional extra photos to display in the gallery

In the writing below, I use the symbol `~` to denote the root folder of our repository, meaning the directory you see when you go to our repo's URL in your browser: https://github.com/DeckOfPandas/too-much-of-a-person . So if I write `~/_stories`, I mean the folder named "_stories" contained in the main folder, and `~/_assets/images` means the folder "images" which is inside the folder "_assets" contained in the main folder.

## Adding a Story step by step
### Step 1: Identifying stories -- decide on the slug

Each Story is identified by a "slug", which is a unique string that will appear in the permanent URL for that Story when it appears online. The slug will also form the name of the directory where you upload the images for that Story.

For example, the slug for a Story from Helen Jackson might be `helen-j`, so the permanent URL for the published story will be `https://toomuchofaperson.com/stories/helen-j`, and you will upload Helen's images into a directory named `helen-j`.

The idea of using a consistent slug helps keep things organised and clear from both ends, but is also super great for SEO and search engine crawling, as URL stability is ranked very highly. Lastly, and most importantly imo, it is polite to our Story participants to ensure that the URL shared publicly has something sensible in it!

### Step 2: Add the information for the Story to a new Markdown file

Markdown is a particular kind of plain text file that is used widely on the interwebs. Markdown files have file extension .md.

The markdown file containing the config for each Story should be created in or uploaded to `~/_stories`, for example `~/_stories/helen-j.md`. You can make the file on your own computer then upload it to GitHub by clicking "Upload file", or you can create it directly on GitHub by clicking "Create new file". It is worth noting that you can upload multiple files at the same time. Note: you must be inside the directory in which you want to create or upload the new file(s).

The website will automatically create and build a Story page for every .md file it finds in `~/_stories/`, if the parameter `published` is set to `true` (the very first setting in the file).

A template markdown file with details of what goes inside it is below.

### Step 3: Add the image files

All images used in the website are in the directory `~/_assets/images/`, with those for Stories then in the subfolder `stories`, and those for a particular Story in a subfolder from there named with the slug you decided on for that Story.

For the example above, the images for the Story should be uploaded to `~/_assets/images/stories/helen-j/`. 

You need to upload at least two images: one for the main photo used on the Story page, and one to use as the thumbnail in the Story cards we display on the site. Please name these "main" and "thumbnail" -- file extension doesn't matter, but the interwebs prefer .png in general in case it's equivocal to you.

Any other images with file extensions .png or .jpg you upload to this same directory will be displayed in the photo gallery/slideshow on the Story page. You don't need to write down anywhere what these images are called -- all images other than main and thumbnail will appear in the gallery automatically.


## More about the markdown file

### Overview

The markdown file for each Story, which you create in or upload to `~/_stories/`, contains all the information you want to display on the web page.

The file must start and end with `---` each on its own line, in order to be recognised by the website as an instruction to create a new page.

The structure for giving the details is:
```
parameter_name: parameter_value
```
One per line, with a semicolon, exactly like this^^. 

### Full template markdown file 

```
---
published: true
layout: story
firstname: "Helenj"
surname: "Jackson"
slug: priscilla-s
year: "2018"
quotation: "If this is justice, then I am a banana"
video_url: "https://www.youtube.com/embed/s-OJoLnkEoA"
audio_url: "https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/484902516%3Fsecret_token%3Ds-dVKjW&color=%23fe0000&inverse=false&auto_play=false&show_user=false"
tags:
  - "#toomuchofaperson"
  - "#ADHD"
  - "#tooloud"
  - "#toomuch"
  - "#twenties"
  - "#toointense"
  - "#toohyper"
  - "#relationships"
  - "#emotionallyintelligent"
  - "#sensitive"
  - "#london" 
  - "#tooexcitable"
  - "#poet"
  - "#creativity" 
  - "#musician"
---
```

You can copy and paste this template into each new file you make, then change the parameter values appropriately.

### Explanation of markdown file contents

* `published`  must be either `true` or `false`, depending on if you want this Story to appear on the site yet or not

* `layout` must be `story`, in order to tell the website what kind of page to create.

* `firstname` `surname` and `quotation` must be inside quote marks, and will display exactly the text you enter, so are case sensitive and will include any punctuation you use. We don't actually display surname anywhere yet, but you have it in your spredsheet for now so we may as well make use of it here.

* `slug` is the unique identifier you decide on for each Story, and must be inside quotation marks. This is also the name of the directory you must upload image files to for this Story.

*`year` must be a number inside quotation marks.

* `video_url` and `audio_url` must be the full URL of the media file (on YouTube or SoundCloud) inside quotation marks

* `tags` specifies a list of the tags you want to appear for that Story. Each tag must appear on its own line, with the spacing and hyphen exactly as above, and the word itself inside quotation marks.


