# History

Retrieves your [Meetup](http://meetup.com) group's past events and generates a database.

## Motivation

We are building this so we can retrieve data reagrding past events' attendance and members.

The ultimate use of this is to feed our machine learning models to, hopefully, generate some interesting
predictions for the organizers of newer events.

## Set up

> Requires Python 3.6

### Dependencies

We use [Bjoern](https://github.com/jonashaag/bjoern) to serve our WSGI application (built with Hug framework).

As such, `libev` is required, [as an external dependency](https://github.com/jonashaag/bjoern/wiki/Installation#libev).

```shell
$ FUTSALTOKYO_ENV=dev && pip install -r requirements/$FUTSALTOKYO_ENV.txt
```

TODO

