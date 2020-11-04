import shutil
import matplotlib
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode

package_path = Path(__file__).parents[0].resolve()
cjk_font_path = Path(f'{package_path}/fonts/').resolve()
mpl_font_path = Path(f'{matplotlib.get_data_path()}/fonts/ttf').resolve()

# fonts_info = {
#     # cwTeX Fonts
#     'cwTeX Q Ming': {'folder': 'cwtex', 'filename': 'cwTeXQMing.ttf'},
#     'cwTeX Q Kai': {'folder': 'cwtex', 'filename': 'cwTeXQKai.ttf'},
#     'cwTeX Q Yuan': {'folder': 'cwtex', 'filename': 'cwTeXQYuan.ttf'},
#     'cwTeX Q Fangsong': {'folder': 'cwtex', 'filename': 'cwTeXQFangsong.ttf'},
#     'cwTeX Q Hei': {'folder': 'cwtex', 'filename': 'cwTeXQHei.ttf', }
# }


class FontTool():

    def __init__(self) -> None:
        pass

    @staticmethod
    def set_font(font='Noto Serif CJK TC'):
        matplotlib.rcParams['font.sans-serif'] = [font] + matplotlib.rcParams['font.sans-serif']
        matplotlib.rcParams['axes.unicode_minus'] = False

    @staticmethod
    def install_font(folder='noto', method='link'):
        if method == 'link':
            for file in Path(f'{cjk_font_path}/{folder}'):
                matplotlib.font_manager.fontManager.addfont(file)
        elif method == 'copy':
            mpl_fonts = [file.name for file in mpl_font_path.glob('**/*')]
            cjk_fonts = [file.name for file in Path(f'{cjk_font_path}/{folder}')]

            for font in cjk_fonts:
                if font not in mpl_fonts:
                    shutil.copy(Path(f'{cjk_font_path}/{folder}/{font}'),
                                Path(f'{mpl_font_path}/{font}'))

    @staticmethod
    def show_font_setting():
        print("Family: " + str(matplotlib.rcParams['font.family']))
        print("Cursive: " + str(matplotlib.rcParams['font.cursive']))
        print("Fantasy: " + str(matplotlib.rcParams['font.fantasy']))
        print("Monospace: " + str(matplotlib.rcParams['font.monospace']))
        print("Sans-Serif: " + str(matplotlib.rcParams['font.sans-serif']))
        print("Serif: " + str(matplotlib.rcParams['font.serif']))
        print("Size: " + str(matplotlib.rcParams['font.size']))
