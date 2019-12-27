"""我们使用import语句导入csv模块，然后用dir()函数看看它里面有什么东西："""
# 请直接运行并体验代码

import csv

# dir()函数会得到一个列表，用for循环一行行打印列表比较直观
for i in dir(csv):
    print(i)

"""
Dialect
DictReader
DictWriter
Error
OrderedDict
QUOTE_ALL
QUOTE_MINIMAL
QUOTE_NONE
QUOTE_NONNUMERIC
Sniffer
StringIO
_Dialect
__all__
__builtins__
__cached__
__doc__
__file__
__loader__
__name__
__package__
__spec__
__version__
excel
excel_tab
field_size_limit
get_dialect
list_dialects
re
reader
register_dialect
unix_dialect
unregister_dialect
writer

"""
