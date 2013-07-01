#!/usr/bin/env python2

import dbus

from notificationd import BaseClass

class NotificationDBusServer(BaseClass, dbus.service.Object):
    def __init__(self, logger):
        BaseClass.__init__(self, logger)

        self.__logger = logger

        bus_name = dbus.service.BusName('net.as65342.notifications', bus=dbus.SystemBus())
        dbus.service.Object.__init__(self, bus_name, '/net/as65342/notifications')

    @dbus.service.method('net.as65342.notifications')
    def ifup(self, ifname):
        self.debug('DispatcherDBusServer.ifup received')
        return True

    @dbus.service.method('net.as65342.notifications')
    def ifdown(self, ifname):
        self.debug('DispatcherDBusServer.ifdown received')
        return True
