




<div align="center">
  <img src="/data/icons/com.mattjakeman.ExtensionManager.svg" width="64">
  <h1 align="center">Extension Manager (Unofficial Fedora Build)</h1>
  <p align="center">A native tool for browsing, installing, and managing GNOME Shell Extensions</p>

  <blockquote>
    <p><strong>⚠️ NOTICE: THIS IS A FORK</strong></p>
    <p>
      This is a modified version of the original <a href="https://github.com/mjakeman/extension-manager">Extension Manager</a>.
      The purpose of this repo is to create a native .rpm file for Fedora.
      Please <strong>do not</strong> report bugs encountered in this version to the original maintainers.
      Report issues via the "Issues" tab in this repository.
    </p>
  </blockquote>

  [![License (GPL-3.0)](https://img.shields.io/github/license/mjakeman/extension-manager)](http://www.gnu.org/licenses/gpl-3.0)
  [![Copr build status](https://copr.fedorainfracloud.org/coprs/vaniiiiii/extension-manager/package/extension-manager/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/vaniiiiii/extension-manager/package/extension-manager/)
  
  <sup>Original project written with GTK 4 and libadwaita</sup>

  ![Screenshot of the main GUI (light mode)](data/screenshot-installed-light.png#gh-light-mode-only)
  ![Screenshot of the main GUI (dark mode)](data/screenshot-browse-dark.png#gh-dark-mode-only)
</div>

## About This Fork
This repository is a fork of the excellent **Extension Manager** originally created by **Matthew Jakeman**.

**Changes in this version:**
*  Bundled libbacktrace support(as it is not available in fedora)


## Features
The core tool supports:
 - Browsing and searching extensions from `extensions.gnome.org`
 - Installation and Removal
 - Enabling and Disabling
 - Updating in-app ([GNOME 43+](https://github.com/mjakeman/extension-manager/wiki/Known-Issue:-Updates))
 - Screenshots & Images
 - Ratings & Comments
 - Translations

## 💻 Installing

### Installing this Fork
[Provide instructions for your specific fork here, for example:]

**Via COPR (Fedora):**
```shell
sudo dnf copr enable vaniiiiii/extension-manager
sudo dnf install extension-manager

```

### Installing the Original (Upstream)

If you are looking for the **official** stable release supported by the original developer, Flatpak is the recommended method.

<a href='https://flathub.org/apps/com.mattjakeman.ExtensionManager'>
<img width='240' alt='Get it on Flathub' src='https://flathub.org/api/badge?locale=en'/>
</a>

## 💬 Community (Upstream)

The original project has a Matrix room. If you are discussing general Extension Manager topics, you may join below. **Please clarify that you are using a fork if you ask for help.**

Join and say hello! https://matrix.to/#/#extension-manager:matrix.org

## 🌐 Translations

The original Extension Manager is translated into more than 30 languages via [Weblate](https://weblate.org/en/).

If you wish to contribute translations, please contribute to the **upstream project** so that all versions of Extension Manager benefit from your work:
[Contribute to Upstream Translations](https://hosted.weblate.org/engage/extension-manager/)

## ⚠️ Known Issues

### Extensions are not being updated

Updates do not work out of the box on GNOME 40 and certain older versions of GNOME
41 and 42 **unless the official GNOME Extensions app is also installed**. See here
for details and a simple workaround: [Wiki Page](https://github.com/mjakeman/extension-manager/wiki/Known-Issue:-Updates)

## ⏰ Using Unsupported Extensions

GNOME Shell will not load extensions that were not designed for your current
version. You can override this behaviour by manually disabling GNOME Shell's
version check. Extension Manager will respect this preference and allow you
to use unsupported extensions fully.

> [!CAUTION]
> Unsupported extensions will likely not work as intended and
> may introduce instability to your system. Disable the version check at your own risk.

Turn off the version check and allow unsupported extensions:

```
gsettings set org.gnome.shell disable-extension-version-validation true

```

## 🔨 Building

### Dependencies

Extension Manager depends on the following libraries:

* gettext
* gtk4
* libadwaita
* libjson-glib
* libsoup
* libxml2
* [blueprint](https://gitlab.gnome.org/jwestman/blueprint-compiler)
* **libbacktrace** (Specific to this fork)

On Debian-based distributions, the required dependencies can be installed with the following command:

```shell
sudo apt install blueprint-compiler gettext libadwaita-1-dev libgtk-4-dev libjson-glib-dev libsoup-3.0-dev libxml2-dev meson

```

### Building From Source

```shell
meson setup _build
meson compile -C _build
meson install -C _build

```

## 👫 Code of Conduct

This project follows the [GNOME Code of Conduct](https://conduct.gnome.org/). Please
adhere to it in all project spaces and interactions.

## 📜 Credits

* **Original Author:** [Matthew Jakeman](https://github.com/mjakeman)
* All contributors to the upstream repository.
