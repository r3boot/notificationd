
import sys
import subprocess

class BaseClass:
    def __init__(self, logger):
        self.__logger = logger

    def info(self, msg):
        self.__logger.info(msg)

    def debug(self, msg):
        self.__logger.debug(msg)

    def warning(self, msg):
        self.__logger.warning(msg)

    def error(self, msg):
        self.__logger.error(msg)
        sys.exit(1)

    def path_to_name(self, path=None):
        if not path:
            return

        if path == '/':
            return 'slash'
        elif path.startswith('/'):
            path = path[1:]
        return path.replace('/', '_')

    def run(self, cmdline):
        self.debug(' '.join(cmdline))
        proc = subprocess.Popen(cmdline, stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
        proc.wait()
        output = proc.stdout.readlines()
        if len(output) > 0:
            return ''.join(output)
