#HOWTO: Add a story to the website

## File structure

The website will automatically create and build a Story page for every config file it finds in `~/_interviews/`, which looks like this:

[screenshot]

Each of these files describes the settings for a Story. More below.

The website will look for the contents for each Story in `~/_assets/images/stories/`, which looks like this:

[screenshot]

Each directory here represents one Story.


## Config files

The config file for each Story, located in `~/_interviews` as described above, contains settings that tell the website what information to include in the page for that Story.

The structure is
```
parameter_name: parameter_value
```

One per line, with a semicolon, exactly like this^^.


### Config file example

Config files look like this:

```
---
layout: interview
interviewee: "NAME"
date: 2018-05-01
quotation: "Whatever words you want for the quotation, with capital letters and punctuation exactly as you want them"
video_youtube: "https://www.youtube.com/embed/s-OJoLnkEoA"
matrix_photo: /assets/images/interviews/FOLDER_NAME/matrix.png
main_photo: /assets/images/interviews/FOLDER_NAME/main.jpg
photos: 
 - /assets/images/interviews/FOLDER_NAME/FILE_NAME.png
 - /assets/images/interviews/FOLDER_NAME/DSC_8597.png
 - /assets/images/interviews/FOLDER_NAME/DSC_8609.png
 - /assets/images/interviews/FOLDER_NAME/DSC_8646.png
 - /assets/images/interviews/FOLDER_NAME/DSC_8659.png
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

### Config file parameters

 `layout` needs to be `interview, exactly as above, in order to tell the website what kind of page to create.

`interviewee` and `quotation` Will display  exactly as you enter, so is case sensitive

`date` format must be exactly like the above, so yyyy-mm-dd

`video_url` and `audio_url` need to be the full URL to where the file is on YouTube or SoundCloud

`matrix_photo` is the filepath to the main photo for that Story, the one you want to display in the thumbnails on the cards for each Story when these are given in a list, such as "Related Stories" or whatever

`photos` specifies a list of filepaths to the other photos you want to display for that Story. We can display these in a gallery, or however you like, but they should all be given here. Spaces and hyphens and quotation marks must be exactly as above.

`tags` specifies a list of the tags you want to appear for that Story. Spaces and hyphens and quotation marks must be exactly as above.


## Image files

Each file must be uploaded to GitHub, with its path given in the config file for that Story. For example, for Priscilla, the config file specifies the matrix photo to be:
```
matrix_photo: /assets/images/interviews/priscilla/matrix.png
```
And the corresponding file is uploaded to that directory, like this:

[screenshot]

## How to actually create or upload files on GitHub

To follow (sorry)