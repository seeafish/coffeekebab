import argparse


def stickers(text):
    control_chars = list('facebook')
    required_stickers = 0

    filtered_text = [char for char in text if char in control_chars]
    if filtered_text:
        occurrences = [
            round(float(filtered_text.count(char)) / control_chars.count(char))
            for char in set(filtered_text)
        ]

        required_stickers = int(max(occurrences))
    return "You require %d stickers" % required_stickers

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Output number of stickers')
    parser.add_argument('text', help='text to parse')
    args = parser.parse_args()

    print stickers(args.text)
