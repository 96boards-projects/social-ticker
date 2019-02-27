---
# Front Matter
# Title of your project used for the breadcrumb title and meta title.
title:  Project Title

# Permalink your project will reside under on the 96boards.org website.
# separate your title's words with dashes for SEO purposes.
permalink: /projects/template-project/
author: 96Boards

# Add a description of your project
#description: Description of your project

# Add the names of your images which are stored in the sub folders here.
# The first image is always used in the table at /projects/
# This section is used to add a social media share image to your project.
# Place the image you'd like to use when sharing on social media in the /assets/images/projects/
# folder and adjust the following YAML accordingly.
# High Res 1920 x 1080
# regenerated on site build
#image: 
#    path: /assets/images/projects/share_image.png
#    list:
#        - thumb.png
#        - share.png
#social:
#  name: 96Boards
#  links:
#    - https://twitter.com/96boards
#    - https://www.facebook.com/96Boards/
#    - https://www.linkedin.com/company/96boards/
#    - https://plus.google.com/+96Boards
3    - https://github.com/96boards
project:
    # Difficulty level for your project <Beginner, Intermediate, Experienced>
    #difficulty_level:
    #- Intermediate
    # Boards that you have used in this project. For a full list of boards see 
    # this file in the 96boards/website repo - _data/boards.yml
    boards_used: 
        - dragonboard410c
    # Verticals are catagories that your project belongs to. For a full list of verticals see 
    # this file in the 96boards/website repo - _data/verticles.yml
    verticals:
        - Maker
#Optional tags for your projects: meta-key words
tags:
- dragonboard410c
---
# Social Media Ticker

# Table of Contents

- [1) Hardware](#1-hardware)
   - [1.1) Hardware Requirements](#11-hardware-requirements)
   - [1.2) Hardware Setup](#12-hardware-setup)
- [2) Software](#2-software)
   - [2.1) Install Dependencies](#21-install-dependencies)
   - [2.2) Add tokens](#22-add-tokens)
   - [2.3) Running the Bot](#23-running-the-bot)

# 1) Hardware

## 1.1) Hardware Requirements

- [Any 96Boards CE](https://www.96boards.org/products/ce/)
- [SeeedStudio Sensors Mezzanine](https://www.96boards.org/product/sensors-mezzanine/)
- 5x [MAX7219 LED Matrix Modules](https://www.amazon.com/MAX7219-Microcontroller-Compatible-Atomic-Market/dp/B00TNNDH0A/ref=sr_1_13?ie=UTF8&qid=1541425999&sr=8-13&keywords=max7219)
- [SSD1306 OLED 128x64](https://www.adafruit.com/product/326)
## 1.2) Hardware Setup
- Connect all the LED matrix Modules in a daisy-chain configuration
- Connect the Sensor Mezzanine to the first LED Matrix Module as follow:

| Sensor Mezzanine | MAX7219 LED Matrix |
|:----------------:|:------------------:|
| 5v               | VCC                |
| GND              | GND                |
| 11               | DI (MOSI)          |
| 10               | CS                 |
| 13               | CLK                |

- Connect the OLED Module as follow:

| Sensor Mezzanine | SSD1306 OLED |
|:----------------:|:------------:|
| 5v               | VCC          |
| GND              | GND          |
| SDA              | SDA          |
| SCL              | SCL          |

- I used ICSP to program the SeeedStudio Mezzanine. You can follow [this guide](https://www.96boards.org/blog/arduino-ide-sensor-mezzanine/).

# 2) Software

**This guide assumes that [Debian OS is running on a Dragonboard410c](https://www.96boards.org/documentation/consumer/dragonboard410c/downloads/debian.md.html) on all 4 nodes. How ever the instructions hold true for other 96Boards CE Boards running Debian.**

> This project is compatible with other Linux based OS, but they might have to be tweaked accordingly.

## 2.1) Install Dependencies

```shell
$ sudo apt install python-setuptools python-dev python-pip
$ sudo pip install wheel tweepy requests serial
```

## 2.2) Add tokens

- **Twitter**
  - Create a developer account at: [https://developer.twitter.com/en/apply/user](https://developer.twitter.com/en/apply/user)
  - Get access token: [https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html)
  - Set <twconsumer_key> in ```ticker.py``` with your Twitter Consumer Key.
  - Set <twconsumer_secret> in ```ticker.py``` with your Twitter Consumer Secret Key.
  - Set <twaccess_token> in ```ticker.py``` with your Twitter access token.
  - Set <twaccess_token_secret> in ```ticker.py``` with your Twitter access token secret key.

- **YouTube**
  - Follow Google's [official guide](https://developers.google.com/youtube/v3/getting-started) to generate API key.
  - Set <ytapikey> in ```ticker.py``` with your YouTube API Key.


## 2.3) Running the Ticker

- Flash the Sensors Mezzanine with ```ticker.ino```

**Test Run**

You can run it simply as
  ```shell
  $ python ticker.py
  ```
**Deploy**

From Shell
  ```shell
  $ python ticker.py &
  ```
