![Code Quality](https://github.com/m-ildefons/goshort/workflows/Code%20Quality/badge.svg?branch=master)

GoShort -- Tiny Url Shortener
=============================

Goshort is a tiny URL shortener with minimal requirements. It features:

  - Custom short names
  - API for shortening URLs
  - Frontpage showing custom shortlinks
  - Easy Docker deployment

Setup
-----

Set the URL of your goshort deployment in: `goshort/config.py`.
Alternatively, set the environment variable `GOSHORT_URL`.

To run initialize the database and run goshort from the commandline, execute:

```
$ ./run.sh init
[...]
$ ./run.sh
Serving on http://0.0.0.0:8080
```

Goshort will then be served on `localhost:8080`.

### Docker

Docker images are available here: https://hub.docker.com/r/ildefons/goshort

```
$ docker run -v <storage-dir>:/instance --rm -it ildefons/goshort init
$ docker run -p 8080:8080 -v <storage-dir>:/instance --rm -it ildefons/goshort
Serving on http://0.0.0.0:8080
```

In case of a Kubernetes deployment, use an init-container for the
initialization step.

Usage
-----

To shorted a url, enter it into the url field an press the `goshort` button.

You can save a URL to the frontpage of goshort with a custom name by visiting
the path `http://<your-goshort-host>/<custom-name>` and shortening the url as
usual.

Goshort also serves an API, which can be used to save links like so:

```
$ curl -F url=http://example.com http://<your-goshort-host>
http://<your-goshort-host>/jzqscblq
```

Contributing
------------

Please feel free to contribute code, documentation and ideas via the issue
tracker: https://github.com/m-ildefons/goshort/issues
