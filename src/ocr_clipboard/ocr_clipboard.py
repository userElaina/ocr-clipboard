import time
import keyboard
import numpy as np
from PIL import ImageGrab


ALL_API = list()

try:
    import easyocr
    reader = easyocr.Reader(['en', 'ch_sim'])

    def _ocr_easyocr(img: np.ndarray) -> str:
        return reader.readtext(img)

    ALL_API.append(_ocr_easyocr)
except ImportError:
    pass


# from .ocr_api import ALL_API

if not ALL_API:
    raise ImportError(
        'No OCR API available. Please install `easyocr` or other supported OCR libraries, or provide your own OCR implementation.'
    )
_ocr = ALL_API[0]

ZH_PATTERN = r'[\u4e00-\u9fa5]+'


def ocr_0(f=_ocr) -> list:
    for _ in range(50):
        img = ImageGrab.grabclipboard()
        if img is not None:
            break
        time.sleep(0.1)
    if img is None:
        return None
    data = np.array(img)
    return [s for idx, s, acc in f(data)]


def ocr_1(f=_ocr) -> list:
    # print('[get img...]')
    l = ocr_0(f)
    if l is None:
        print('No image found in clipboard.')
        return

    # print('[ocr:]')
    if not l:
        print('No text found in image.')
        return
    print('\n'.join(l))


def ocr_cycle(f=_ocr) -> None:
    print('[ocr clipboard cycle]')
    while True:
        if keyboard.is_pressed('ctrl+c'):
            return
        if not keyboard.is_pressed('windows+shift+s'):
            try:
                time.sleep(0.1)
            except KeyboardInterrupt:
                return
            continue

        print('[Meta Shift S]')
        time.sleep(5)
        ocr_1(f)
        print('[done; waiting for next...]')


if __name__ == '__main__':
    print(ocr_1())
    ocr_cycle()
