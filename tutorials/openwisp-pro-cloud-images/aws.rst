Deploying OpenWISP Pro on AWS
=============================

**OpenWISP Pro** is a cloud image that you can launch from AWS
Marketplace. This tutorial walks you through subscribing to the image,
launching an Amazon EC2 instance, and configuring network access so that
you can connect to the server using SSH.

.. important::

    OpenWISP Pro Images is in private beta. To try it, submit your
    interest through the `OpenWISP Pro Images form
    <https://form.jotform.com/260416646535055>`_.

.. contents:: **Table of Contents**:
    :depth: 2
    :local:

Launch OpenWISP Pro Standard from AWS Marketplace
-------------------------------------------------

To begin, sign in to the `AWS Management Console
<https://console.aws.amazon.com/>`_. If you do not have an AWS account,
`create one <https://aws.amazon.com/>`_ before continuing.

Open `AWS Marketplace <https://aws.amazon.com/marketplace/>`_, enter
``OpenWISP Pro Standard`` in the search field, and select the listing.
Review the product information, usage instructions, and pricing before
subscribing.

Choose **Continue to Subscribe**, review the terms and conditions, and
choose **Accept Terms**. Once the subscription has been processed, choose
**Continue to Configuration** to prepare the image for launch.

Configure and launch the instance
---------------------------------

On the configuration page, select the software version you want to deploy
and the AWS **Region** where the instance will run. Choose **Continue to
Launch**, then use **Launch from Website** to configure the instance:

1. For **EC2 Instance Type**, choose ``t3.medium`` or larger. This is the
   recommended starting size; choose a larger instance if your deployment
   requires more resources.
2. For **VPC Settings**, select the Virtual Private Cloud (VPC) in which
   OpenWISP will run. A VPC is the network that contains your AWS
   resources.
3. For **Subnet Settings**, select a public subnet so that users and VPN
   clients can reach the server over the internet. The subnet must have a
   route to an internet gateway, and the instance must have a public IPv4
   address. See `enable internet access using an internet gateway
   <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html>`_
   if you need to prepare your VPC first.
4. For **Security Group Settings**, configure the inbound rules described
   below before launching the instance.
5. For **Key Pair Settings**, select an existing key pair in the chosen
   Region, or choose **Create a key pair in EC2**. Keep the private key on
   your computer: you will need it to authenticate your SSH connection.
6. Review the configuration and choose **Launch**.

Open the `Amazon EC2 console <https://console.aws.amazon.com/ec2/>`_ in
the same Region and select **Instances** to find your new server. Wait for
its state to become **Running** and for its status checks to pass before
connecting.

Configure the security group
----------------------------

A security group acts as a firewall for the instance. Its inbound rules
determine which connections can reach OpenWISP.

In **Security Group Settings**, choose **Create New Based on Seller
Settings**, enter a name and description, and review the proposed rules.
For example, use ``openwisp-pro`` as the name and ``Web, SSH, and VPN
access to OpenWISP Pro`` as the description. If you select an existing
security group instead, check that it permits the same traffic.

Configure the following inbound rules:

.. list-table::
    :header-rows: 1
    :widths: 20 15 15 25 25

    - - Type
      - Protocol
      - Port
      - Source
      - Purpose
    - - HTTP
      - TCP
      - 80
      - ``0.0.0.0/0``
      - HTTP connections
    - - HTTPS
      - TCP
      - 443
      - ``0.0.0.0/0``
      - HTTPS connections
    - - SSH
      - TCP
      - 22
      - Your trusted public IP address or network
      - Server administration
    - - Custom TCP
      - TCP
      - 1194
      - ``0.0.0.0/0``
      - VPN connections

Ports 80 and 443 allow web traffic to reach the server. Port 1194 allows
remote VPN clients to establish a connection. For this image, the VPN rule
uses **TCP**, so select **Custom TCP** and enter ``1194`` as the port.

The source ``0.0.0.0/0`` allows connections from any IPv4 address. This
lets users and devices reach the web and VPN services from different
networks. For SSH, restrict the source to addresses you trust. For
example, a single administrator address can be entered as
``203.0.113.10/32``; replace this example with your own public IP address.
Use a trusted network's CIDR range if several administrators need access.

Save the security group and select it for the instance. If your public IP
address changes later, update the SSH rule before trying to connect again.

Associate an Elastic IP address
-------------------------------

Once the instance is running, consider associating an Elastic IP address
with it. An Elastic IP is a static public IPv4 address that you can keep
associated with the server or move to a replacement instance.

A stable address is useful for both web access and VPN connections: users,
devices, and DNS records can continue to use the same endpoint. An
automatically assigned public IPv4 address can change when an EC2 instance
is stopped and started.

For instructions, see the AWS guide to `associate an Elastic IP address
with an instance
<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-eips.html>`_.

Connect to the instance using SSH
---------------------------------

When the instance has passed its status checks, connect to it using SSH.
You will need the private key for the key pair selected at launch, the
instance's public address, and its login username.

In the EC2 console, select the instance, choose **Connect**, and open the
**SSH client** tab to view the connection instructions. Use the username
provided for the image. Follow the AWS guide to `connect to your Linux
instance using SSH
<https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-linux-instance.html>`_.

If the connection times out, check that the instance has a public address,
its subnet has internet access, and the security group allows TCP port 22
from your current public IP address. If authentication fails, check the
username and that you are using the private key corresponding to the key
pair selected at launch.

Configure OpenWISP Pro
----------------------

In your SSH session, run the following command to start the configuration
wizard:

.. code-block:: shell

    sudo openwisp-ctl configure

The wizard asks a series of questions to set up your OpenWISP instance.
Pay particular attention to these settings:

- **Dashboard domain**: The domain where you will access the OpenWISP
  administration interface, for example, ``openwisp.example.com``.
- **API domain**: The domain your devices will use to communicate with
  OpenWISP, for example, ``api.example.com``.
- **VPN domain**: The domain used by OpenVPN clients to connect to the
  server. It defaults to the dashboard domain; you can keep this default
  unless you need a separate VPN domain.
- **SSL certificates**: Choose whether the wizard should provision
  certificates using Let's Encrypt. Before enabling this option, update
  the DNS records for the domains that need certificates to point to the
  instance's public IP address. Make sure the records resolve to this
  address before continuing.
- **Site Manager Email**: Enter the email address to use when creating
  your user account.
- **Logo**: Optionally add a logo for your instance.

Once you have completed the wizard, choose **Save and Apply**. The wizard
closes, and the terminal asks whether you want to continue. Press ``Y`` to
apply the configuration and start OpenWISP.

When setup finishes, the command displays your login credentials. Open the
dashboard domain you configured and sign in using those credentials.
