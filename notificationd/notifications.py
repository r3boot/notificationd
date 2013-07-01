
import pynotify

from notificationd import BaseClass

class Notifications(BaseClass):
    def __init__(self, logger):
       # BaseClass.__init__(self, logger)
        pynotify.init('notificationd')

    def _message(self, urgency, title, msg):
        if urgency not in ['low', 'normal', 'critical']:
            self.error('Unknown urgency: %s' % urgency)
            return

        msg = pynotify.Notification(title, msg)
        msg.set_urgency(urgency)
        msg.show()

    def low(self, title, msg=None):
        self._message('low', title, msg)

    def normal(self, title, msg=None):
        self._message('normal', title, msg)

    def critical(self, title, msg=None):
        self._message('critical', title, msg)
