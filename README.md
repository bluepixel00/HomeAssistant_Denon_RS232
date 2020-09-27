# HomeAssistant_Denon_RS232

This implementation was based off of the following:

https://github.com/home-assistant/home-assistant/blob/dev/homeassistant/components/media_player/denon.py
https://github.com/joopert/nad_receiver/blob/master/nad_receiver/__init__.py 

1) Place media_player.py under Home Assistant Config folder:
/custom_components/denon232

2) Place __init__.py under Home Assistant Config folder:
/deps/lib/python3.8/site-packages/denon232_receiver

When the minimum version of python increases the above python3.8 needs to be changed to that updated version.

The serial_port device below should be changed to match what is being used in your setup.  In this setup I was using a USB to serial converter.  If this is what is being used ensure Home Assistant has access to USB.

3) Add configuration.yaml details:

```
media_player:
  - platform: denon232
    serial_port: /dev/ttyUSB0
    name: Receiver
```
