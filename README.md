# too-much-of-a-person

## Introduction
This is the source code for the Too Much of a Person project website. The site uses jekyll, with CSS/Sass/Scss for styling.

## Licence
Source code is licensed under GPLv4. Website content is licensed under CC BY. All IP remains with Too Much of a Person.

## Live site 
* Built from this repository branch `master` via GitHub pages
* URL in the repo subtitle line  
* Give DNS details to whoever holds the domain name

## Deployment
* Travis CI picks up Pull Requests to branch `source`, runs tests, builds the site using gulp, then pushes the build to branch `master`
* TODO: staging build

## Build locally 
* `gulp serve` builds the site and serves it at `localhost:3000
* The gulpfile has other build options, including `gulp clean`

### Initial setup for first local build
* `git clone` repo
* `bundle install` to install list in Gemfile  
* `npm install` to install list in packages.json  
* TODO Quick description of how to get bundler etc 


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
* I have included `_config.local.yml` as well as `_config.yml` to cover this
