
# Group Chats Capture

A little implementation of capturing WeChat messages, focusing on group chats.
Powered by [ItChat](https://github.com/littlecodersh/itchat).

## Environment

Works and tested on python3.8.

## Messages Generation Steps

### Install dependency

`pip install itchat`

### Start generating messages

python start_generation.py # Hit `Ctrl + C` to stop it

## Data Description

All of messages from one single group chat in one day will be stored in a txt
file, which has the same name of it. And all of files located in a path named
by format `%b-%d-%Y`(e.g. Apr-23-2021).
