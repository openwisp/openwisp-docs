======================
Main Technologies Used
======================

Python
------

`Python <https://www.python.org/>`_ it's the main programming language
used by the server side application (web admin, API, controller, workers).

In the past OpenWISP was built in Ruby On Rails, but we later switched
to Python because it's much more suited to networking and it has a wider
pool of potential contributors.

Django
------

`Django <https://www.djangoproject.com/>`_ is one of the most popular
web frameworks for Python language.

It is used extensively in our modules. Django allows rapid development
and has a very rich ecosystem.

OpenWRT
-------

`OpenWRT <https://openwrt.org/>`_ is an linux distribution designed for
embedded systems, routers and networking in general.

It has a very skilled community and it is used as a base by many
hardware vendors (Technicolor, Ubiquiti Networks, Linksys, Teltonika
and many others).

Node.js and React JS
--------------------

`NodeJS <https://nodejs.org/en/>`_ is javascript runtime to build
JS based applications.

In OpenWISP it's used as a base for frontend applications
along with `React <https://reactjs.org/>`_, like
`openwisp-wifi-login-pages <https://github.com/openwisp/openwisp-wifi-login-pages/>`_.

Ansible
-------

We use `Ansible <https://www.ansible.com/>`_ to provide an automated
procedure to `deploy OpenWISP <https://github.com/openwisp/ansible-openwisp2>`_
and to `compile custom OpenWRT images for different
organizations <https://github.com/openwisp/ansible-openwisp2-imagegenerator>`_.

Docker
------

We use docker in
`docker-openwisp <https://github.com/openwisp/docker-openwisp>`_,
which aims to ease the deployment of OpenWISP in a
containerized infrastructure.

NetJSON
-------

`NetJSON <http://netjson.org/>`_ is a data interchange format based on
`JSON <http://json.org/>`_ designed to ease the development of software
tools for computer networks.

Lua
---

`Lua <https://www.lua.org/>`_ is a lightweight, multi-paradigm programming
language designed primarily for embedded systems and clients.

Lua is cross-platform, since the interpreter is written in ANSI C,
and has a relatively simple C API.

It is the official scripting language of OpenWRT.
