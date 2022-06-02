#!/bin/bash

python gen.py deck.txt deck.apkg
/Applications/Anki.app/Contents/MacOS/AnkiMac deck.apkg
