# History

:date: Retrieves your [Meetup](http://meetup.com) group's past events and generates a database.

## Motivation

We are building this so we can retrieve data reagrding past events' attendance and members.

The ultimate use of this is to feed our machine learning models to, hopefully, generate some interesting
predictions for the organizers of newer events.

## Set up

> Requires Python 3.6

### Dependencies

We use [Bjoern](https://github.com/jonashaag/bjoern) to serve our WSGI application (built with [Hug framework]()).

As such, `libev` is required, [as an external dependency](https://github.com/jonashaag/bjoern/wiki/Installation#libev).

However, if you are intending to use this for development purpose, Hug has a built-in development server, batteries included.

For persistence, we assume you would be using a PostgreSQL backend as well.


```shell
$ FUTSALTOKYO_ENV=dev && pip install -r requirements/$FUTSALTOKYO_ENV.txt
```

### Environment Variables

Required environment variables:

| name | remarks |
| --- | --- |
| `MEETUP_API_KEY` | your Meetup API key |
| `MEETUP_GROUP_NAME` | your Meetup group name, `Futsal-Tokyo` for example |
| `DB_NAME` | your database name, defaults to `history` |
| `DB_HOST` | your database host, defaults to `127.0.0.1` |
| `DB_PORT` | your database password, defaults to `5432` |
| `DB_USER` | your database username |
| `DB_PASSWORD` | your database password, if any |


TODO

