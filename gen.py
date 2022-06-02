import uuid
import genanki
import os.path as osp
import json

class WordNote(genanki.Note):
  @property
  def guid(self):
    """Only front is used to identify a note"""
    return genanki.guid_for(self.fields[0])


def prepare_config(config_filename):
    if osp.exists(config_filename):
      with open(config_filename) as f:
        return json.load(f)
    else:
      config = {
        'deckId': uuid.uuid1(),
        'modelId': uuid.uuid1(),
        'deckTitle': "Deck title"
      }
      with open(config_filename) as f:
        json.dump(f, config)
      return config


def generate_deck(config, input_filename, output_filename):
    deck = genanki.Deck(
      config['deckId'],
      config['deckTitle']
    )
    word_model = genanki.Model(
      config['modelId'],
      'Word model',
      fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
      ],
      templates=[
        {
          'name': 'Card 1',
          'qfmt': '{{Question}}',
          'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
      ]
    )
  
    with open(input_filename) as f:
        lines = list(f.readlines())
        groups = []
        current_group = None
        for line in lines:
            if line.startswith('# '):
                if current_group:
                    groups.append(current_group)
                current_group = {"name": line[2:].strip(), "children": [] }
            elif len(line.strip()) > 0:
                current_group["children"].append(line.strip())
        
        for group in groups:
            for line in group["children"]:
                try:
                    front, back = line.split(':', 2)
                    note = WordNote(
                        model=word_model,
                        fields=[front, back]
                    )
                    deck.add_note(note)
                    genanki.Package(deck).write_to_file(output_filename)
                except Exception:
                    print(f'Ignored {line}')


def main():

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Text file')
    parser.add_argument('output', help='APKG file')
    args = parser.parse_args()

    config = prepare_config('./config.json')

    generate_deck(
      config=config,
      input_filename=args.input,
      output_filename=args.output
    )


if __name__ == '__main__':
    main()