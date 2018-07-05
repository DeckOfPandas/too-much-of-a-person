# toomuchofaperson.com

## Introduction
The repos described here contain the source code for the Too Much of a Person project website. The site uses jekyll, with CSS/Sass/Scss for styling, Travis CI to optimise assets, add scripts, and build the site, and all versions of the site are hosted on github pages.

## Licence
Source code is licensed under GPLv3. Website content is licensed under CC BY. All IP remains with Too Much of a Person.

## Overview
### Repositories
* RAW repo https://github.com/DeckOfPandas/too-much-of-a-person 
* STAGING PARKED repo https://github.com/too-much-of-a-person/com.toomuchofaperson.test 
* LIVE repo https://github.com/too-much-of-a-person/com.toomuchofaperson

### Builds
* STAGING BUILD matching the base of the current release https://deckofpandas.github.io/too-much-of-a-person/
* STAGING PARKED BUILD for content we're not deploying now/soon https://too-much-of-a-person.github.io/com.toomuchofaperson.test/ (arbitrarily more of these can be made)
* LIVE DEPLOYMENT build https://toomuchofaperson.com

### Wiring
* branch `source` of RAW has PRs picked up by Travis CI --> built site pushed back to branch `master`
* branch `master` of RAW is served as a GitHub Pages site at the STAGING BUILD url above
* Any built jekyll site can be served from branch `master` of the STAGING PARKED BUILD repo at the STAGING PARKED BUILD url above (or indeed any github repo ofc)
* branch `master` of LIVE is served as a GitHub Pages site from the LIVE DEPLOYMENT url above
* Build locally (NB: check build paths in `_config.yaml`) then `git push --force [your_staging_remote_name] master` to push to any github pages site in an emergency... (Note: this is unlikely to be an emergency)

###
Summary:
* Make PRs to RAW branch `source`
* RAW `master` is served at STAGING BUILD url
* STAGING PARKED `master` is served at STAGING PARKED BUILD url
* LIVE `master` is served at LIVE DEPLOYMENT url

...got that?


## Raw source code
RAW repo: https://github.com/DeckOfPandas/too-much-of-a-person branch `source`
* Branch `current` to be maintained as identical to current release
* PR into branch `source` triggers Travis

## Deployment to staging site (and automated optimisation and testing)
* Travis picks up Pull Requests to RAW repo branch `source`, runs tests, compresses shiz, builds the site using gulp, then pushes the contents of the resulting built `_site` folder back to branch `master`

## Deployment to live site
* Clone https://github.com/DeckOfPandas/too-much-of-a-person branch `master` locally, build (check uild path in config...), then push to LIVE repo (probably not to `master`, though)


# Building locally 
### Initial setup for first local build
* `git clone` repo
* `bundle install` to install list of gems in Gemfile  
* `npm install` to install list of node packages in packages.json  
* TODO Quick description of how to get bundler etc 

### Then
* `gulp serve` builds the site and serves it at `localhost:3000
* (The gulpfile has other build options, including `gulp clean`)
* Browser automaticlly refreshes with changes etc

## Notes 
* Make sure `baseurl` and `url` are set up correctly for the main build:
* For staging site, these settings will be something like:
```
baseurl: "/too-much-of-a-person"
url: "https://deckofpandas.github.io"
```
* Locally, use something like:
```
baseurl: "/"
url: "http://localhost:3000/"
```
* Live site 
```
baseurl: "/"
url: "http://toomuchofaperson.com"
```
