# resm

Simple web server to get and release resources

## Install

> $ python setup.py build

> $ python setup.py test

> \# python setup.py install

## Running in console

After install you can run the service jump write "resm" in console.

#### Params

- --port (default 5000)
- --count Count of resources (default 5)
- --name Name of resource (default r)
- --debug Debbuging

#### Example

> resm -p 8000 -c 10 -n resource --debug

## Daemon

Setup creates /etc/init.d/resm
Configuration file is located /etc/resm.conf
Format of config file is exactly the same as console params, ie

> --port 8000 --count 6 -n res
