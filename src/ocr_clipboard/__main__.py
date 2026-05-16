import argparse

from .ocr_clipboard import ocr_1, ocr_cycle

parser = argparse.ArgumentParser(
    'ocr-clipboard',
    'ocr_clipboard [options] ...',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

parser.add_argument(
    '-c', '--cycle',
    action='store_true',
    help='cycle mode'
)


def main():
    args = parser.parse_args()
    if args.cycle:
        ocr_cycle()
    else:
        ocr_1()


if __name__ == '__main__':
    main()
