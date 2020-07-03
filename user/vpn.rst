VPN-Client Automation
=====================


Installing VPN Server and importing the VPN configuration
---------------------------------------------------------

We will be installing VPN Server using `this ansible role <https://github.com/Stouts/Stouts.openvpn>`_
and then import the VPN configuration into OpenWISP. If you have
already setup your VPN server or would like to install the VPN server
via some other way, you can skip to
`Step 4 <#importing-the-ca-and-the-server-ceritficate>`_

.. note::
    **This process is not auomated yet.**

1. Install Ansible and required Ansible roles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Install ansible (version 2.5 or higher) **on your local machine**
(not on the server!) if you haven't done already.

To **install ansible** we suggest you follow the official
`ansible installation guide <http://docs.ansible.com/ansible/latest/intro_installation.html>`_ .

After having installed ansible, **you need to install git**
(example for linux debian/ubuntu systems):

.. code-block:: bash

    sudo apt-get install git

After having ansible and git installed, install the required roles:

.. code-block:: bash

    ansible-galaxy install git+https://github.com/Stouts/Stouts.openvpn,3.0.0 nkakouros.easyrsa

2. Create hosts file and ansible playbook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create an ansible inventory file named ``hosts``
**on your local machine and not in the server** with the following
contents:

::

    [openvpn]
    your_server_domain_or_ip

For e.g. if your server ip is ``192.168.56.2``:

::

    [openvpn]
    192.168.56.2

In the same directory where you created the ``host`` file,
create a file named ``playbook.yml`` which contains the following:

.. code-block:: yaml

    - hosts: openvpn
      vars:
        # EasyRSA
        easyrsa_generate_dh: true
        easyrsa_servers:
          - name: server
        easyrsa_clients: []
        easyrsa_pki_dir: /etc/easyrsa/pki

        # OpenVPN
        openvpn_keydir: "{{ easyrsa_pki_dir }}"
        openvpn_clients: []
        openvpn_use_pam: false
      roles:
        - role: nkakouros.easyrsa
        - role: Stouts.openvpn


.. Hint::
    You can further customize the Configuration using the role variables.
    Get Info about other options in `EasyRSA <https://github.com/nkakouros-original/ansible-role-easyrsa>`_
    and `OpenVPN <https://github.com/Stouts/Stouts.openvpn>`_


3. Run the Playbook
~~~~~~~~~~~~~~~~~~~

Run the ansible playbok using:

.. code-block::  bash

    ansible-playbook -i hosts playbook.yml -b -k -K --become-method=su


4. Importing the CA and the Server Ceritficate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To import the CA and Server Ceritficate, you need to access your server
via ``ssh`` or any other method that suits you.

You need to change your directory to ``/etc/easyrsa/pki/``

.. note::
    If you face ``-bash: cd: /etc/easyrsa/pki: Permission denied``
    you may need to login as root user.

**Importing the CA**:

On your openwisp dashboard go to ``/admin/pki/ca/add/``

In **Operation Type** choose :guilabel:`Import Existing`

Get your CA Ceritficate from ``ca.crt`` file and Private Key from
``private/ca.key`` and then enter them in the respective fields.

**Importing the Server Certificate**:

On your openwisp dashboard go to ``/admin/pki/cert/add/``

In **Operation Type** choose :guilabel:`Import Existing` and in **CA**
choose the CA you just created.

Get your Server Ceritficate from ``issued/server.crt`` file and Server
Private Key from ``private/server.key`` and then enter them in the
respective fields.

4. Creating VPN Server
~~~~~~~~~~~~~~~~~~~~~~

On your openwisp dashboard go to ``/admin/config/vpn/add/``

In **Host** enter you Server IP, in **Certification Authority** select
the CA you created and in **X509 Certificate** select the certificate you
created.

Now under **Configuration**, open **Configuration Menu** and deselect
Property :guilabel:`Files`. For **VPN1** Change
:guilabel:`Server (Bridged)` to the Type of your VPN Server. The VPN
Server installed using the guide above is a Routed Server so change the
Type to :guilabel:`Server (Routed)`. The Process to setup a Bridged Server
is identical to that of Routed Server.

Change the rest of the Configuration of the VPN according to the
configuration in ``/etc/openvpn/server.conf``

.. Tip::
    You can check if your VPN Configuration is similar to the
    ``server.conf`` file using the **Preview Configuration** option
    at the Top.

Preparing the configuration template for VPN Clients
----------------------------------------------------

Create VPN Template
~~~~~~~~~~~~~~~~~~~

On your openwisp dashboard go to ``/admin/config/template/add/``.

Change **Type** to :guilabel:`VPN-client`.
For **VPN** select the VPN you created in the previous steps.

You can further toggle `Enabled by default <#default-templates>`_
and `Auto certificate <#auto-client-certificates>`_
options according to your needs.

Save the template. You can now tweak the Client VPN configuration.
Now can add the template to your devices.

Auto Client Certificates
~~~~~~~~~~~~~~~~~~~~~~~~

**Option**: ``Auto certificate``

**Default**: ``True``

Auto Client Certificates feature allows you to automatically generate
generate client certificates for your Device.

Default Templates
~~~~~~~~~~~~~~~~~

**Option**: ``Enabled by default``

**Default**: ``False``

Default templates are automatically added to newly created devices of
the organization of the template. If no organization is specified, the
template is added to all devices of all the organizations.
