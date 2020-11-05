<div align="right">

  [![](https://flat.badgen.net/pypi/v/mpl-tc-fonts)](https://pypi.org/project/mpl-tc-fonts/)
  [![](https://flat.badgen.net/github/license/Hsins/mpl-tc-fonts)](./LICENSE)

</div>

<div align="center">

<img src="https://i.imgur.com/21O7uhj.png" alt="mpl-tc-fonts" height="150px">

# mpl-tc-fonts

🇹🇼 _A package to solve the problem of ["Tofu"](https://en.wikipedia.org/wiki/Specials_(Unicode_block)) in your `matplotlib` plots whenever you're trying to use Traditional Chinese characters in labels or texts._

[![Open In Colab](https://flat.badgen.net/badge/Demo/Open%20in%20Colab/DB8E34?icon=https://simpleicons.now.sh/jupyter/fff)](https://colab.research.google.com/github/hsins/mpl-tc-fonts/blob/main/examples/examples.ipynb)

</div>

## Installation

Install `mpl-tc-fonts` with `pip`:

```bash
# Install from GitHub Repository for latest commit
$ pip install git+https://github.com/Hsins/mpl-tc-fonts.git
```

The package installer `pip` will install this package from the [
mpl-tc-fonts](https://github.com/Hsins/mpl-tc-fonts) to your python environment. Please see the [FAQ](#faq) section for more information and troubleshooting.

## Usage

### Quick Start

The easiest way to use is just `import` the packages after installation and the Traditional Chinese characters are properly displayed in your plots.

```python
import matplotlib.pyplot as plt
import mpl_tc_fonts

names = ['分類 A', '分類 B', '分類 C']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('分類資料圖')
plt.show()
```

<p align="center">
  <img src="https://i.imgur.com/cwp1Qz4.png">
</p>

The default font is **思源宋體（Noto Serif CJK TC）**.

### More Features

```python
import mpl_tc_fonts

# Copy the cwTeX fonts into matplotlib folder
font_tool.load_font('cwtex', 'copy')

# Set "cwTeX Q Kai" to be the display font
font_tool.set_font('cwTeX Q Kai')

# Print out current font in use
font_tool.show_font_setting()

# Print out the list of the avaiable font-family name
print(font_tool.scan_font('國'))
```

There are some functions to help users qucik setup the fonts:

- `mpl_tc_fonts.load_font(folder, method)` would install the given fonts.
  - `folder` can be `noto` (default) or `cwtex`
  - `method` can be `link` (default) or `copy`
- `mpl_tc_fonts.set_font(font)` would set the given `font` to display the texts. There are 7 different fonts in this package.
  - `Noto Sans CJK TC`: 思源黑體
  - `Noto Serif CJK TC`: 思源宋體
  - `cwTeX Q Ming`: cwTeX 中明體
  - `cwTeX Q Kai`: cwTeX 中楷體
  - `cwTeX Q Yuan`: cwTeX 中圓體
  - `cwTeX Q Fangsong`: cwTeX 仿宋體
  - `cwTeX Q Hei`: cwTeX 粗黑體
- `mpl_tc_fonts.scan_font(char)` return the `list` of avaiable fonts in the FontList of `matlibplot`. The given `char` is used to check whether glyph could be found in that font or not.
- `mpl_tc_fonts.show_font_setting()` print out current font in use.

## FAQ

## License

Licensed under the GPL-3.0 License, Copyright © 2020-present Hsins.