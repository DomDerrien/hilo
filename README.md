[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)

# Hilo
Hilo integration for Home Assistant

# What This Is:
This is a custom component to allow control of Hilo devices from Home Assistant.

# What It Does:
- Get current temperature of thermostat
- Update target temperature of thermostat
- Get power of energy meter
- Get power of each devices
- Support for switches
- Binary sensor for Hilo Event

# To Do:
- Add functionnalities for other devices

# How To Setup:
Copy the custom_components/hilo directory from the latest release to your customer_components directory.

After copying all files from the hilo directory, your configuration should look like:
```
hilo:
  username: YourHiloUsername
  password: YourHiloPassword
```
