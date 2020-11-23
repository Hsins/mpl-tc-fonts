<div align="right">

  [![](https://img.shields.io/pypi/v/mpl-tc-fonts?style=flat-square)](https://pypi.org/project/mpl-tc-fonts/)
  [![](https://img.shields.io/github/license/Hsins/mpl-tc-fonts.svg?style=flat-square)](./LICENSE)

</div>

<div align="center">

<img src="https://i.imgur.com/21O7uhj.png" alt="mpl-tc-fonts" height="150px">

# mpl-tc-fonts

🇹🇼 _一款用來處理 `matplotlib` 繪圖時無法正常顯示繁體中文標籤或內容，導致產生如同 [豆腐（tofu）](https://en.wikipedia.org/wiki/Specials_(Unicode_block)) 形狀空白字元 `□` 的套件_

[![Open in Colab](https://img.shields.io/badge/DEMO-Open%20in%20Colab-DB8E34.svg?logo=jupyter&style=flat-square)](https://colab.research.google.com/github/hsins/mpl-tc-fonts/blob/main/examples/examples.ipynb)
[![README in English](https://img.shields.io/badge/README-English-8CA1AF.svg?logo=read-the-docs&style=flat-square)](./README.md)

</div>

<details><summary><b>Other CJK Characters Version</b></summary>
<p>

<div align="center">

[🇨🇳 簡體中文](https://github.com/Hsins/mpl-sc-fonts) ・ [🇯🇵 日語](https://github.com/Hsins/mpl-jp-fonts) ・ [🇰🇷 韓文](https://github.com/Hsins/mpl-kr-fonts)

</div>

<p>
</details>

## 安裝

透過 `pip` 套件管理工具安裝 `mpl-tc-fonts` 套件:

```bash
# Install from GitHub Repository for latest commit
$ pip install git+https://github.com/Hsins/mpl-tc-fonts.git
```

The package installer `pip` will install this package from the [
mpl-tc-fonts](https://github.com/Hsins/mpl-tc-fonts) repository to your local python environment. Please see the [FAQ](#faq) section for more information and troubleshooting.

## 使用說明

### 快速入門

The easiest way to use this package is just `import` the package after installation. It links the fonts inside package folder to the `matplotlib` font manager and the Traditional Chinese characters will be properly displayed in your plots.

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

> **[NOTE]** The default font would set to be **思源宋體（Noto Serif CJK TC）**.

### 更多特性

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

## 常見問答

<details><summary><b>[ 問 ] 在 <code>load_font()</code> 方法中的 <code>copy</code> 和 <code>link</code> 選項有什麼區別？</b></summary>
<p>

> TBD

<p>
</details>

## 授權許可

Licensed under the GPL-3.0 License, Copyright © 2020-present Hsins.