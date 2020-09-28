# HomeAssistant_Denon_RS232

This is a Denon AVR / Receiver Custom Component for Home Assistant.  This custom component should support any Denon receiver with a serial port.  This implementation was based off of the following:

https://github.com/home-assistant/home-assistant/blob/dev/homeassistant/components/media_player/denon.py
https://github.com/joopert/nad_receiver/blob/master/nad_receiver/__init__.py 

Setup:
1) If not present create the custom component folder structure under your Home Assistant config directory.
example: config/custom_components/denon232/

2) Place ``__init__.py``, media_player.py and denon232_receiver.py in the denon232 folder under custom components folder.

3) Add configuration.yaml details:

```
media_player:
  - platform: denon232
    serial_port: /dev/ttyUSB0
    name: Receiver
```

The serial_port device referenced should be changed to match what is being used in your setup.  In this setup a USB to serial converter was used through /dev/ttyUSB0.  If USB is being used ensure Home Assistant has access to USB.
