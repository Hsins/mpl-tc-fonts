import shutil
import matplotlib
from pathlib import Path
from fontTools.ttLib import TTFont

PACKAGE_PATH = Path(__file__).parents[0].resolve()
CJK_FONT_PATH = Path(f'{PACKAGE_PATH}/fonts/').resolve()
MPL_FONT_PATH = Path(f'{matplotlib.get_data_path()}/fonts/ttf').resolve()


# helper functions
def __has_glyph(font_path: str, glyph) -> bool:
    font = TTFont(font_path, fontNumber=0)
    for table in font['cmap'].tables:
        if ord(glyph) in table.cmap.keys():
            return True
    return False


def set_font(font='Noto Serif CJK TC') -> None:
    matplotlib.rcParams['font.sans-serif'] = [font, 'sans-serif']
    matplotlib.rcParams['axes.unicode_minus'] = False


def load_font(folder='noto', method='link') -> None:
    if method == 'link':
        for file in Path(f'{CJK_FONT_PATH}/{folder}').glob('**/*.*'):
            matplotlib.font_manager.fontManager.addfont(f'{file.resolve()}')

    elif method == 'copy':
        mpl_fonts = [file.name for file in MPL_FONT_PATH.glob('**/*')]
        cjk_fonts = [file.name for file in Path(f'{CJK_FONT_PATH}/{folder}').glob('**/*')]

        for font in cjk_fonts:
            if font not in mpl_fonts:
                source = Path(f'{CJK_FONT_PATH}/{folder}/{font}').resolve()
                target = Path(f'{MPL_FONT_PATH}/{font}').resolve()
                shutil.copy(source, target)
                matplotlib.font_manager.fontManager.addfont(f'{target}')


def scan_font(char='灣') -> list:
    result = []
    for font in matplotlib.font_manager.fontManager.ttflist:
        if font.name not in result and __has_glyph(f'{Path(font.fname).resolve()}', char):
            result.append(font.name)

    return result


def show_font_setting() -> None:
    print("Current Font: " + str(matplotlib.rcParams['font.sans-serif']))
