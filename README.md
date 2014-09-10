Easy Search
改自 Google Search[https://github.com/nwjlyons/google-search]
适用于Sublime Text 2/3.
我不熟悉版权问题，我不宣称有版权(276887367@qq.com)
##Install

If your using the [Sublime Package Manger][2] hold down Ctrl+Shift+P and type
`Package Control: Install Package`. Then search for `easy-search` and hit return.

If your not using the package manager then go to your Sublime packages directory(Sublime Text/Packages) Then run this command `git clone https://github.com/justintung/easy-search.git`.

Or you can download the package as a zip file [https://github.com/justintung/easy-search/archive/master.zip][3] then copy it into your Sublime packages directory.
## 配置
```json
{
    "suffix": "", // 查询关键字前缀
    "prefix": "", // 查询关键字后缀
    "searchbase": "http://www.baidu.com/s?wd=" // 搜索基地址
}
```
## 快捷键
1.选择要搜索的词，然后按 `Ctrl+Shift+G`.
2.按 `Ctrl+Alt+G`,然后输入要搜索的关键字

## 使用方法

1.使用百度翻译
```json
{
    "suffix": "",
    "prefix": "",
    "searchbase": "http://fanyi.baidu.com/#en/zh/"
}
```
2.使用百度搜索
```json
{
    "suffix": "",
    "prefix": "",
    "searchbase": "http://www.baidu.com/s?wd="
}
```
3.使用百度词典
```json
{
    "suffix": "",
    "prefix": "",
    "searchbase": "http://dict.baidu.com/s?wd="
}
```
4.搜索 php.net document
```json
{
    "suffix": "",
    "prefix": "",
    "searchbase": "http://cn2.php.net/manual-lookup.php?pattern="
}
```