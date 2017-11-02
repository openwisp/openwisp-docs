Setup for users
===============

The only community supported method of installing OpenWISP2 is using the Ansible role.
This will take care of installing the latest release, it's dependencies, a database,
a webserver, an email server, running migrations.

To begin we need *ansible* installed on our **local machine**

.. code-block:: bash

   sudo pip install ansible

.. note::

   The minimum version of ansible supported by the community is ansible 2.2, please make sure
   to have a recent version of ansible installed

Once we have ansible installed it's time to get our hands on the OpenWISP2 *role*.

.. glossary::

   role
       A role is a bundle of files that Ansible can make sense of to do
       some automated work. You put those files into a directory and call
       it a role. Very fine people upload these bundles to ansible-galaxy
       so that others can use them.

.. code-block:: bash

   # this will install the openwisp role on your local
   # machine to be used during the setup
   ansible-galaxy install openwisp.openwisp2

Now we have to create or *playbook* to instruct ansible to do the work

.. glossary::

   playbook
      A file containing a list of tasks to do and where to do them

Create a directory called `my_openwisp` and move inside it.

.. code-block:: bash

   mkdir my_openwisp
   cd my_openwisp

Before continuing we have to decide where to place the controller.
Once you have chosen an available domain name we can continue.

From now on I want the controller to be avaialable at `my.controller.domain.com`
so I will use it where you will have to use your domain name.

Create a file `controller.yaml` and fill it with this

.. code-block:: yaml

   - hosts: controller # <- the name of the remote machine
     become: "{{ become | default('yes') }}" # <- add this if you will not be logging in as root
   - roles: # <- we want to use the openwisp2 role on the remote machine
     - openwisp.openwisp2

Now that we have the list of tasks and where to work we have to
specify who is the `controller`

Create a file `hosts` and put this in there

.. code-block:: ini

   [controller]
   my.controller.domain.com

Substitute the `my.controller.domain.com` with your **remote** machine domain.

.. warning::

   Usin a domain name instead of an IP is vital because postfix, the mail server,
   will not be able to work with just an ip

At the end you will have a new directory looking like this.

.. code-block:: bash

    .
    ├── controller.yaml
    └── hosts
 
Now it's finally time to let Ansible do some work for us!

.. code-block:: bash

   ansible-playbook -i hosts controller.yaml -u remote_user -k --ask-sudo-pass

Obviously substitute the **remote_user** with the your user on the **remote** machine.

Once ansible has finished correctly to do the work you can log in your controller using the
url `https://my.controller.domain.com/admin` using the credentials

    username: admin

    password: admin

.. warning::

   Change the password for the admin account as soon as possible from the
   address `https://my.controller.domain.com/admin/password_change/`
