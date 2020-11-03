import matplotlib
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode

package_path = Path(__file__).parents[0].resolve()
fonts_info = {
    # cwTeX Fonts
    'cwTeX Q Ming': {'folder': 'cwtex', 'filename': 'cwTeXQMing.ttf'},
    'cwTeX Q Kai': {'folder': 'cwtex', 'filename': 'cwTeXQKai.ttf'},
    'cwTeX Q Yuan': {'folder': 'cwtex', 'filename': 'cwTeXQYuan.ttf'},
    'cwTeX Q Fangsong': {'folder': 'cwtex', 'filename': 'cwTeXQFangsong.ttf'},
    'cwTeX Q Hei': {'folder': 'cwtex', 'filename': 'cwTeXQHei.ttf', }
}


class FontTool():

    def __init__(self) -> None:
        pass

    @staticmethod
    def load(font='cwTeX Q Yuan'):
        folder, filename = fonts_info[font]['folder'], fonts_info[font]['filename']
        font_path = Path(f'{package_path}/fonts/{folder}/{filename}').resolve()

        matplotlib.font_manager.fontManager.addfont(f'{font_path}')

        # 設定預設字體（須注意座標軸負號顯示）
        # : 中文字體中，襯線體（serif）通常設置為明體或楷體
        # : 中文字體中，非襯線體（sans-serif）通常設置為黑體或圓體
        # matplotlib.rcParams['font.family'] = [
        #     font] + matplotlib.rcParams['font.family']
        matplotlib.rcParams['font.serif'] = [
            font] + matplotlib.rcParams['font.serif']
        matplotlib.rcParams['font.sans-serif'] = [font] + \
            matplotlib.rcParams['font.sans-serif']
        matplotlib.rcParams['axes.unicode_minus'] = False

    @staticmethod
    def show_font_setting():
        print("Family: " + str(matplotlib.rcParams['font.family']))
        print("Cursive: " + str(matplotlib.rcParams['font.cursive']))
        print("Fantasy: " + str(matplotlib.rcParams['font.fantasy']))
        print("Monospace: " + str(matplotlib.rcParams['font.monospace']))
        print("Sans-Serif: " + str(matplotlib.rcParams['font.sans-serif']))
        print("Serif: " + str(matplotlib.rcParams['font.serif']))
        print("Size: " + str(matplotlib.rcParams['font.size']))
