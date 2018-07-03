# too-much-of-a-person

## Introduction
This is the source code for the Too Much of a Person project website. The site uses jekyll, with CSS/Sass/Scss for styling.

## Licence
Source code is licensed under GPLv3. Website content is licensed under CC BY. All IP remains with Too Much of a Person.

## Overview
* RAW repo https://github.com/DeckOfPandas/too-much-of-a-person 
* LIVE repo: https://github.com/too-much-of-a-person/com.toomuchofaperson
* branch `source` of RAW --> Travis CI, built site pushed back to branch `master` of RAW
* branch `master` of RAW is served as a GitHub Pages site for staging
* branch `master` of LIVE is served as a GitHub Pages site for final site

## Raw source code
RAW repo: https://github.com/DeckOfPandas/too-much-of-a-person branch `source`
* Branch `current` to be maintained as identical to current release
* PR into branch `source` to trigger Travis CI

## Deployment to staging site (and automated optimisation and testing)
* Travis CI picks up Pull Requests to https://github.com/DeckOfPandas/too-much-of-a-person
 branch `source`, runs tests, builds the site using gulp, then pushes the build to branch `master`
* Staging URL: https://deckofpandas.github.io/too-much-of-a-person/

## Deployment to live site
* Clone https://github.com/DeckOfPandas/too-much-of-a-person branch `master` locally, then push to LIVE repo
* Live URL: 

# Building locally 
### Initial setup for first local build
* `git clone` repo
* `bundle install` to install list in Gemfile  
* `npm install` to install list in packages.json  
* TODO Quick description of how to get bundler etc 

### Then
* `gulp serve` builds the site and serves it at `localhost:3000
* (The gulpfile has other build options, including `gulp clean`)
* Browser automaticlly refreshes with changes etc\

## Notes 
* Make sure `baseurl` and `url` are set up correctly for the main build:
```
baseurl: "/too-much-of-a-person"
url: "https://deckofpandas.github.io"
```
* Locally these settings will be something like:
```
baseurl: "/"
url: "http://localhost:3000/"
```
* I have included `_config.dev.yml` as well as `_config.yml` to cover this
