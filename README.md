# Python 101

It's better to use [pyvenv](https://github.com/pyenv/pyenv) with your python code
if you want to have the latest version of python:

```bash
# Setup
pyvenv .
# Activate
. ./bin/activate
# Deactive
deactive
```

Also, you can use [pipenv](https://github.com/pypa/pipenv),
[poetry](https://github.com/python-poetry/poetry) or other newer dependency management tools.

## [Mastering Python](mastering-python)

Sample codes of Mastering Python book that is written by Rick van Hattem.

## [ReNamer](renamer)

Simple project for renaming your downloaded TV series or Wallpapers
to better naming structure.
It's far from complete project that can do these things in professional manner.

## [Thrift](thrift)

Let's learn this new beast in Python,
we use pure python edition of Thrift form
[here](https://github.com/Thriftpy/thriftpy2).
This example was written for having more fun in our trash life.

## [EMQx](emqtt)

First up and run your [EMQx](https://emqx.io) broker,
then use this example to have fun.

## [Initial Values](./initial-values/)

Sometimes you want to have a default value for a function parameter:

```python
def f(a = 10):
  pass
```

You cannot use mutable values as a default value, but why?

## [Dataclasses](./dataclasses)

Example of working with dataclasses in python. They are introduced in 3.7.

## [Tuples and their immutability](./tuples-immutability/)

Tuples are immutable but let dig deeper and see what is happened when their items are not immutable.

## [Hashing](./hashing)

Since first time that I used python one of my challenges is how hashing works.

## [Fun with UTF-8](./fun-with-utf8)

Python has better support for UTF-8 than Golang, so let's use it.

## [Finalize](./finalize)

Learn about using finalizers in Python and also seeing `weakref` for the first time.

## [The Calculator](./calc-with-tokenizer/)

An implementation for a calculator that also has a tokenizer, so you can write:

```
1 + 2 * (3 + 4)
```

## [Count Lines](./count-lines/)

The example for counting lines of text file with python. It dates back to 2014.

## [Fibonacci](./fibonacci)

Dynamic programming implementation of Fibonacci.

## [A Pluggable Algorithm](./descriptor)

We need to have a Solution class that has a pluggable algorithm which can be changed during the runtime.
This example contains two ways of implementation for this problem.

## [Fun](./fun)

The fist time I saw Python.

## [Soup](./soup)

Parse HTML in Python. This is a very useful example for scrapping sites.

## [Working with Audio Signals](./pyroy)

An introduction example to using python for audio processing (needs to know a little about signals and systems).

## [MongoDB](./mongodb)

Insert random data into a MongoDB server. It actually used for inserting random data into I1820 database for a B.Sc.
Project.
