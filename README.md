# HomeAssistant_Denon_RS232

This implementation was based off of the following:

https://github.com/home-assistant/home-assistant/blob/dev/homeassistant/components/media_player/denon.py
https://github.com/joopert/nad_receiver/blob/master/nad_receiver/__init__.py 

Setup:
1) Place media_player.py under Home Assistant Config folder under the following directory path:
/custom_components/denon232/

2) Place __init__.py under Home Assistant Config folder under the following directory path:
/deps/lib/python3.8/site-packages/denon232_receiver

When the minimum version of python increases the folder "python3.8" needs to be changed to that updated version.

3) Add configuration.yaml details:

```
media_player:
  - platform: denon232
    serial_port: /dev/ttyUSB0
    name: Receiver
```

The serial_port device referenced should be changed to match what is being used in your setup.  In this setup a USB to serial converter was used through /dev/ttyUSB0.  If USB is being used ensure Home Assistant has access to USB.
