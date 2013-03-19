===============
vagrant_openerp
===============

------------------------------------------------------------------
Vagrant and Fabric files for creating an OpenERP 7 virtual machine
------------------------------------------------------------------

`vagrant_openerp <https://github.com/arthru/vagrant_openerp>`_ is a tool for installing automatically `OpenERP 7 <https://www.openerp.com>`_ on a `Vagrant <http://www.vagrantup.com/>`_ VM. You can also use the recipe to install it on a physical server.

It is made for debian based system but it has only been tested with `Ubuntu 12.04 Precise Pangolin <http://releases.ubuntu.com/precise/>`_.

Prerequisites
=============

You must install `vagrant <http://rubygems.org/gems/vagrant/versions/1.0.7>`_ (version 1.0.x, **may** work with 1.1) and `fabtools <https://pypi.python.org/pypi/fabtools>`_ (only tested with 0.13.0).  For example, if you don't want to use your system package manager :

.. code-block:: sh
    pip install fabtools
    gem install vagrant

You should also add a box to vagrant :

.. code-block:: sh
    vagrant box add precise32 http://files.vagrantup.com/precise32.box

Quickstart
==========

Clone vagrant_openerp from github :

.. code-block:: sh
    git clone https://github.com/arthru/vagrant_openerp.git

Go to the new directory and set up the vagrant VMs :

.. code-block:: sh
    cd vagrant_openerp 
    vagrant up

Launch fab in order to provision the vm for OpenERP :

.. code-block:: sh
    fab vagrant openerp

And here it is ! Simply browse to `http://localhost:8069/ <http://localhost:8069/>`_ to log in your freshly installed OpenERP instance (with admin login and admin password).

