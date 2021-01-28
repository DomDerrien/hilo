"""Hilo HA integration"""
DOMAIN = 'hilo'
import logging

from .hiloapi import *
import voluptuous as vol
from datetime import timedelta

import homeassistant.helpers.config_validation as cv

from homeassistant.const import CONF_PASSWORD, CONF_USERNAME

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Required(CONF_USERNAME): cv.string,
        vol.Required(CONF_PASSWORD): cv.string
    }),
}, extra=vol.ALLOW_EXTRA)

def setup(hass, config):
    """Your controller/hub specific code."""
    
    # Data that you want to share with your platforms
    username = config[DOMAIN].get(CONF_USERNAME, "no username")
    password = config[DOMAIN].get(CONF_PASSWORD, "no password")

    h = Hilo(username, password)
    
    hass.data[DOMAIN] = h

    hass.helpers.discovery.load_platform('climate', DOMAIN, {}, config)
    hass.helpers.discovery.load_platform('sensor', DOMAIN, {}, config)

    return True