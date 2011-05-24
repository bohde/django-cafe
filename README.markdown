# Django Cafe

Django cafe is a way to integrate [Coffeescript](http://jashkenas.github.com/coffee-script/) within your Django application. 

## Simple Example
    
    {% load coffee %}
    <script src="{% coffee spam.coffee %}"/>

## Multiple Files

    <script src="{% coffee foo.coffee bar.coffee %}"/>

## Install
  
    `pip install https://github.com/joshbohde/django-cafe/tarball/master`

## Setup

Make sure cafe is in your installed app, like so. You'll also need to have a working installation of Coffeescript.

    INSTALLED_APPS = (
      ...
      "cafe", 
      ...      
    ) 

## Settings

### CAFE_ROOT

Default: `MEDIA_ROOT`

The location of the .coffee files. 

### CAFE_OUTPUT_DIR

Default: `compiled`

The location within the `CAFE_ROOT` to store the compiled .js files. 

### COFFEE_BIN

Default: `"coffee"`

The Coffeescript executable.

### COFFEE_PARAMS

Default: `"--print"`

The parameters sent to the Coffeescript compiler. 
