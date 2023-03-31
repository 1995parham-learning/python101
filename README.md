<h1 align="center"><a href="https://docs.python.org/3/">Python 101</a></h1>

## Introduction

It's better to use [pyenv](https://github.com/pyenv/pyenv) with your python code,
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
[poetry](https://github.com/python-poetry/poetry) or other newer dependency management tools
instead of old and messy virtual environment.

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

The example for counting lines of text files with python. It dates back to 2014.

## [Fibonacci](./fibonacci)

Dynamic programming implementation of Fibonacci.

## [A Pluggable Algorithm](./descriptor)

We need to have a Solution class that has a pluggable algorithm which can be changed during the runtime.
This example contains two ways of implementation for this problem.

## [Fun](./fun)

The fist time I met Python.

## [Soup](./soup)

Parse HTML in Python. This is a very useful example for scrapping sites.

## [Working with Audio Signals](./pyroy)

An introduction example to using python for audio processing (needs to know a little about signals and systems).

## [MongoDB](./mongodb)

Insert random data into a MongoDB server. It actually used for inserting random data into I1820 database for a B.Sc.
Project.

## [Metaclass](./metaclass)

Review on metaclass basis. Useful for refreshing the concepts in your mind before digging deeper about its awesome
usages.

## [Operator Package](./operator)

Python has built-in library named `operator`. This example is review on some of its functions.

## [Mode](./mode)

It returns the most common element in the array. The objective of this example is not about mode itself, actually it
discusses type hints.

## [Protocol](./protocol)

In Python, a protocol definition is written as a `typing.Protocol` subclass.
However, classes that implement a protocol don't need to inherit, register, or declare any relationship with the class
that defines protocol.
_Protocol_ in Python is similar to interfaces in Go.

## [Main Thread](./main-thread)

Do you know every python program has a thread named `MainThread`? You do now.

## [FastAPI](./fastapi)

[FastAPI](https://fastapi.tiangolo.com/) is one of famous HTTP frameworks in Python and here is an example to use it.

## [Single Dispatch](./singledispatch)

How we can have function overloading in python?

## [Memory View](./memory-view)

The built-in `memoryview` class is a shared-memory sequence type that lets you handle
slices of arrays without copying bytes. It was inspired by the NumPy library.

## [Format](./format)

The f-string, the `format()` built-in function, and the `str.format()` method delegate
the actual formatting to each type by calling their `.__format__(format_spec)`
method. The `format_spec` is a formatting specifier.
