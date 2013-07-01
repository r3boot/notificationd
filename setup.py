#!/usr/bin/env python

from distutils.core import setup

setup(
    name='notificationd',
    version='1.0',
    description='Desktop Notifications with a D-Bus backend',
    author='Lex van Roon',
    author_email='r3boot@r3blog.nl',
    url='https://r3blog.nl/',
    scripts=['scripts/notificationd', 'scripts/notify'],
    data_files=[
        ('/etc/dbus/system.d', ['dbus/net.as65342.notifications.conf']),
    ]
)
