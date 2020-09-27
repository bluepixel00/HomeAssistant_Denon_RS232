"""
Denon  RS232 interface to control the receiver.

Based off:
https://github.com/home-assistant/home-assistant/blob/dev/homeassistant/components/media_player/denon.py#L228
https://github.com/joopert/nad_receiver/blob/master/nad_receiver/__init__.py 

Not all receivers have all functions.
Functions can be found on in the xls file within this repository
"""

import codecs
import socket
from time import sleep
import serial
import telnetlib
import threading
import logging

DEFAULT_TIMEOUT = 1
DEFAULT_WRITE_TIMEOUT = 1

_LOGGER = logging.getLogger(__name__)

class Denon232Receiver(object):
    """Denon232 receiver."""


    def __init__(self, serial_port, timeout=DEFAULT_TIMEOUT,
                 write_timeout=DEFAULT_WRITE_TIMEOUT):
        """Create RS232 connection."""
        self.ser = serial.Serial(serial_port, baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=timeout, write_timeout=write_timeout)
        self.lock = threading.Lock()

    def serial_command(self, cmd, response=False, all_lines=False):
        _LOGGER.debug('Command: %s ', cmd)
        if not self.ser.is_open:
            self.ser.open()
        
        try:
            self.lock.acquire()
            
            # Denon uses the suffix \r, so add those to the above cmd.
            final_command = ''.join([cmd, '\r']).encode('utf-8')
            #_LOGGER.debug('Final Command (encoded): %s ', final_command)
            #Write data to serial port
            #self.ser.reset_output_buffer()
            self.ser.write(final_command)
            #Read data from serial port
            if response:
                lines = []
                while True:
                    line = self.ser.read_until(bytes('\r'.encode('utf-8')))
                    if not line:
                        break
                    #_LOGGER.debug('Received (encoded): %s ', line)
                    lines.append(line.decode().strip())
                    _LOGGER.debug("Received: %s", line.decode().strip())
                if all_lines:
                    return lines
                return lines[0] if lines else ''
            else:
                return None
        finally:
            self.lock.release()