# Django Cafe

Django cafe is a way to integrate [Coffeescript](http://jashkenas.github.com/coffee-script/) within your Django application. 

## Simple Example
    
    {% load cafe %}
    <script src="{% coffee spam.coffee %}"/>

## Multiple Files

    <script src="{% coffee foo.coffee bar.coffee %}"/>

## Setup

Make sure cafe is in your installed app, like so. You'll also need to have a working installation of Coffeescript.

  INSTALLED_APPS = (
    ...
    "cafe", 
    ...      
  ) 

## Settings

### CAFE_MEDIA_DIRECTORY

Default: `MEDIA_DIRECTORY`

The location of the .coffee files. 

### COFFEE_BIN

Default: `"coffee"`

The Coffeescript executable.

### COFFEE_PARAMS

Default: `"-cj"`

The parameters sent to the Coffeescript compiler. 
