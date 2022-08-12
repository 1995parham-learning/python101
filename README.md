# Python 101

It's better to use `pyvenv` with your python code
if you want to have the latest version of python:

```bash
# Setup
pyvenv .
# Activate
. ./bin/activate
# Deactive
deactive
```

## [Bluetooth](bluetooth)

simple program for using bluetooth in python.
In order to use this code on linux you need to install `libbluetooth-dev`
package.

```bash
sudo apt-get install libbluetooth-dev
```

If you want to use BLE version of this library you need following dependencies:

```bash
sudo apt-get install libglib2.0-dev pkg-config libboost-dev libboost-python-dev libboost-thread-dev
git clone https://github.com/1995parham/pygattlib.git && cd pygattlib
sudo python3 setup.py install
```

If you want to access your low power bluetooth devices directly from linux shell
you can use HCI tools like this:

```bash
# First check HCI device is up and running
sudo hciconfig
# If you HCI device is down :(
sudo hciconfig hci0 up
# Let's start a scan for LE (Bluetooth LE or Bluetooth smart) devices
sudo hcitool lescan
```

## [Mastering Python](mastering-python)

Sample codes of Mastering Python book that is written by Rick van Hattem.

## [ReNamer](renamer)

Simple project for renaming your downloaded TV series or Wallpapers
to better naming structure.
It's far from complete project that can do these things in professional manner.

## [Thrift](thrift)

Let's learn this new animal in Python,
we use pure python edition of Thrift form
[here](https://github.com/Thriftpy/thriftpy2).
This example was written for having more fun in our trash life.

## [EMQx](emqtt)

First up and run your [EMQx](https://emqx.io) broker,
then use this example to have fun.
