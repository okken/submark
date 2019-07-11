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

* links
    * `[message](http://some.link.html "my title")`  
      -> `<a href="http://some.link.html" title="my title">message</a>`
    * `[message](http://some.link.html)`  
      -> `<a href="http://some.link.html">message</a>`

* images
    * `![alt](/some/image.png "title")'`  
       -> `'<img src="/some/image.png" title="title"/>`
       
* inline code
    * ``this is `some code` ``  
       -> `this is <code>some code</code> `
       
* line breaks with two spaces at end of text
* horizontal rules, 3 or more dashes
    * `---` -> `<hr>`

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

## Dev & Test virtual environment

Testing and development should be done with a virtual environment.

~~~
$ git clone https://github.com/okken/submark.git
$ cd submark
$ python3 -m venv venv --prompt submark
$ source venv/bin/activate
(submark) $ pip install -U pip
~~~


### Testing

Testing is done with `tox`.

~~~
(submark) $ pip install tox
(submark) $ tox
~~~

### Development

Development requires a few tools. 
Install submark locally and install dev tools with flit.

~~~
(submark) $ pip install flit
(submark) $ flit install --pth-file
~~~

Then you can test any changes locally with pytest.

~~~
(submark) $ pytest --cov=submark 
~~~

And when ready to test everything as an installed package:

~~~
(submark) $ tox
~~~



### Building a wheel

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
* 0.7 
    * flit for development with requires-extra,
    * support for links, images, inline code, line breaks, horizontal rules

