
# Group Chats Capture

A little implementation of capturing WeChat messages, focusing on group chats.
Powered by [ItChat](https://github.com/littlecodersh/itchat).

## Environment

Requires python3.8.

## Messages Generation Steps

### Install dependency

```bash
pip install itchat
```

### Start generating messages

```bash
python start_generation.py # Hit `Ctrl + C` to stop it
```

## Data Description

All of messages from one single group chat will be stored in some txt files,
which has the same name of them. And all of files located in a path named by
the date format `%b-%d-%Y`(e.g. Apr-23-2021).

## Get Results

Results will be several lists, every list contains key-value informations of
user name as key, and the number of messages sent as value. The time scope is
defined as a 24 hours duration start from yesterday's "stop time" to today's

### Start getting results

```bash
python get_results.py
```
