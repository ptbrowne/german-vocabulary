# German vocabulary

## Context

This is a script to generate a Anki deck from a simple text file where I
add my German vocabulary.

It uses [genanki](https://github.com/kerrickstaley/genanki) to generate the deck.

## Installation

```bash
pip install -r requirements.txt
cp config.sample.json config.json # Edit the sample config (mostly for the deck title)
cp deck.sample.txt deck.txt # Edit the deck
```

## Usage

The update script will generate the deck and open Anki so that the deck is updated.
Then you can use Anki sync feature to sync it to the cloud, and then sync it on
your mobile.

```
./update.sh
```
