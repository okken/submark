# submark
Subset of Markdown

This project started as an example project to describe migrating from a script to a package, utilizing flit, tox, coverage, and pytest. 

See http://testandcode.com/80 for the story.

## Features

* Convert headings 
    * `# heading`  -> `<h1> heading </h1>`
    * `## heading`  -> `<h2> heading </h2>`
    * `### heading`  -> `<h3> heading </h3>`
    * `#### heading`  -> `<h4> heading </h4>`
    * `##### heading`  -> `<h5> heading </h5>`

* Convert strong
    * `**strong**` -> `<strong>strong</strong>`
    * `__strong__`-> `<strong>strong</strong>`


* Convert em
    * `**something**` -> `<em>something</em>`
    * `__something__`-> `<em>something</em>`


## Usage

Use it like this:
~~~
$ submark something.md > something.html
~~~

or:
~~~
$ cat something.md | submark > something.html
~~~

or:
~~~
$ echo '**hi**' | submark
<strong>hi</strong>
~~~


## Testing

Test in a virtual environment with the usual incantations.

~~~
$ git clone https://github.com/okken/submark.git
$ cd submark
$ python3 -m venv venv --prompt submark
$ source venv/bin/activate
(submark) $ pip install -U pip
~~~

Then install `tox`.

~~~
(submark) $ pip install tox
~~~

Now run tests.

~~~
(submark) $ tox
~~~

## Building a wheel

Make sure everything is committed before running `flit`.

~~~
(submark) $ pip install flit
(submark) $ flit build
~~~

Yep. That's it. 
There should be a wheel now sitting in a `dist` folder.

~~~
(submark) $ ls dist
submark-0.5-py2.py3-none-any.whl
submark-0.5.tar.gz
~~~

## Deploying

Flit does that too.

~~~
(submark) $ flit publish
~~~

But don't do that unless:

* You are Brian Okken

or:

* You are pointing to something other than pypi
* see https://flit.readthedocs.io/en/latest/upload.html



## History

* 0.1 Initial script and tests
* 0.2 build wheel with flit
* 0.3 build and test with tox
* 0.4 move source module into a package directory
* 0.5 move tests into tests directory
* 0.6 hook up readme in toml file
