---
title: "Action - Plugin (Experimental)"
source: https://automagic4android.com/action_plugin_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: action
---

# Action - Plugin (Experimental)

The action **Plugin (Experimental)** executes the action defined in a plugin. Most plugins don't offer a way to let Automagic wait for the plugin to finish. You can use an action **Sleep** to wait a short amount of time.

Warning: This function is experimental and might not work with all existing plugins available in Google Play. We can not provide support for plugins.

Note: Plugins can be defined using the interface description available from the app Locale: [Locale developer documentation](http://www.twofortyfouram.com/developer) and Tasker: [Tasker plugin extensions](http://tasker.dinglisch.net/plugins.html).

### Settings

#### Plugin

List of all available plugins found on the device.

#### replace variables/modify configuration

Script to dynamically replace variables and to modify the configuration passed to the plugin.

#### Synchronous with Timeout

Whether the plugin should be invoked synchronously and Automagic should wait for the plugin to return a result or not.
Only a few new plugins support this mechanism, this mechanism should usually not be used when the plugin does not request to be executed this way. This option will automatically be enabled when the plugin is configured and the plugin supports synchronous execution.

A variable is a container for a value that can be used in many actions and conditions to dynamically define a part of a text.
[See action Script for a description.](action_script.md#string-inline-expressions)

### Supplied Variables

- `Tasker variables` — takes over the local Tasker variables returned by the plugin (without leading %-character)

---

[← Indeks Action](README.md) · [Katalog komponen](../README.md) · [Semua komponen](../all-components.md)
