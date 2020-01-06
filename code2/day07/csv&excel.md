## csv&excel 🥧爬到的数据存哪里

### 1.存储数据的方式

其实，常用的存储数据的方式有两种——存储成csv格式文件、存储成Excel文件（不是复制黏贴的那种）。

我猜想，此时你会想问“csv”是什么，和Excel文件有什么区别？

前面，我有讲到json是特殊的字符串。其实，csv也是一种字符串文件的格式，它组织数据的语法就是在字符串之间加分隔符——行与行之间是加换行符，同行字符之间是加逗号分隔。

它可以用任意的文本编辑器打开（如记事本），也可以用Excel打开，还可以通过Excel把文件另存为csv格式（因为Excel支持csv格式文件）。

现了吗？csv文件里的逗号可以充当分隔同行字符串的作用。

为什么要加分隔符？因为不加的话，数据都堆在一起，会显得杂乱无章，也不方便我们之后提取和查找。这也是一种让数据变得有规律的组织方式。

另外，用csv格式存储数据，读写比较方便，易于实现，文件也会比Excel文件小。但csv文件缺少Excel文件本身的很多功能，比如不能嵌入图像和图表，不能生成公式。

至于Excel文件，不用我多说你也知道就是电子表格。它有专门保存文件的格式，即xls和xlsx（Excel2003版本的文件格式是xls，Excel2007及之后的版本的文件格式就是xlsx）。

好啦，csv和Excel文件你都清楚了，我们可以继续学习存储数据的基础知识——如何写入与读取csv格式文件和Excel文件的数据。

### 2.存储数据与的基础知识

存储成csv格式文件和存储成Excel文件，这两种不同的存储方式需要引用的模块也是不同的。操作csv文件我们需要借助csv模块；操作Excel文件则需要借助openpyxl模块。

放心，两个模块都并不复杂。本节的实操环节我们会用到Excel，先来一起学习一下。

- 基础知识:Excel写入与读取

一个Excel文档也称为一个工作薄（workbook），每个工作薄里可以有多个工作表（worksheet），当前打开的工作表又叫活动表。

每个工作表里有行和列，特定的行与列相交的方格称为单元格（cell）。比如上图第A列和第1行相交的方格我们可以直接表示为A1单元格。

清楚了Excel的基础概念，我们可以来说下`openpyxl`模块是怎么操作Excel文件的了。照例先说写入后说读取。

提醒：我们得先提前安装好openpyxl模块。课程的终端是已经安装好了，如果你想要在本地操作的话，就需要在本地上安装。（安装方法：window电脑：在终端输入命令：`pip install openpyxl`，按下enter键；mac电脑：在终端输入命令：`pip3 install openpyxl`，按下enter键）

装好openpyxl模块后，首先要引用它，然后通过`openpyxl.Workbook()`函数就可以创建新的工作薄，代码如下：
```python
# 引用openpyxl     
import openpyxl 

# 利用openpyxl.Workbook()函数创建新的workbook（工作薄）对象，就是创建新的空的Excel文件。
wb = openpyxl.Workbook()
```
创建完新的工作薄后，还得获取工作表。不然程序会无所适从，不知道要把内容写入哪张工作表里。
```python
# wb.active就是获取这个工作薄的活动表，通常就是第一个工作表。
sheet = wb.active

# 可以用.title给工作表重命名。现在第一个工作表的名称就会由原来默认的“sheet1”改为"new title"。
sheet.title = 'new title'
```
添加完工作表，我们就能来操作单元格，往单元格里写入内容。
```python
# 把'漫威宇宙'赋值给第一个工作表的A1单元格，就是往A1的单元格中写入了'漫威宇宙'。
sheet['A1'] = '漫威宇宙' 
```
往单元格里写入内容只要定位到具体的单元格，如A1（根据Excel的坐标，A1代表第一列第一行相交的单元格），然后给这个单元格赋值即可。

如果我们想往工作表里写入一行内容的话，就得用到`append`函数。
```python
# 把我们想写入的一行内容写成列表，赋值给row。
row = ['美国队长','钢铁侠','蜘蛛侠']

# 用sheet.append()就能往表格里添加这一行文字。
sheet.append(row)
```
如果我们想要一次性写入的不止一行，而是多行内容，又该怎么办？请你花10s思考一下这个问题。

想出结果了吗？（提示：用for循环，再点击会出现答案）
```python
# 先把要写入的多行内容写成列表，再放进大列表里，赋值给rows。
rows = [['美国队长','钢铁侠','蜘蛛侠'],['是','漫威','宇宙', '经典','人物']]

# 遍历rows，同时把遍历的内容添加到表格里，这样就实现了多行写入。
for i in rows:
    sheet.append(i)

# 打印rows
print(rows)
```
成功写入后，我们千万要记得保存这个Excel文件，不然就白写啦！
```python
# 保存新建的Excel文件，并命名为“Marvel.xlsx”
wb.save('Marvel.xlsx')
```

写入文件代码参考 `demo02.py`
读取文件代码参考 `demo04.py`

如果你对openpyxl模块感兴趣，想要有更深入的了解的话，推荐阅读openpyxl模块的官方文档：

https://openpyxl.readthedocs.io/en/stable/



- 基础知识:csv写入与读取

首先，我们要引用csv模块。因为Python自带了csv模块，所以我们不需要安装就能引用它。

```python
# 引用csv模块。
import csv

# 创建csv文件，我们要先调用open()函数，传入参数：文件名“demo.csv”、写入模式“w”、newline=''、encoding='utf-8'。
csv_file = open('demo.csv','w',newline='',encoding='utf-8')
```

然后，我们得创建一个新的csv文件，命名为“demo.csv”。

“w”就是write，即文件写入模式，它会以覆盖原内容的形式写入新添加的内容。

友情附上一张文件读写模式表。你不需要背下来，之后不知道用什么模式时查查表就可以了。


加`newline=' '`参数的原因是，可以避免csv文件出现两倍的行距（就是能避免表格的行与行之间出现空白行）。加`encoding='utf-8'`，可以避免编码问题导致的报错或乱码。

创建完csv文件后，我们要借助csv.writer()函数来建立一个writer对象。
```python
# 引用csv模块。
import csv

# 调用open()函数打开csv文件，传入参数：文件名“demo.csv”、写入模式“w”、newline=''、encoding='utf-8'。
csv_file = open('demo.csv','w',newline='',encoding='utf-8')
# 用csv.writer()函数创建一个writer对象。
writer = csv.writer(csv_file)
```
那怎么往csv文件里写入新的内容呢？答案是——调用writer对象的writerow()方法。
```python
# 借助writerow()函数可以在csv文件里写入一行文字 "电影"和“豆瓣评分”。
writer.writerow(['电影','豆瓣评分'])
```
我们试着再写入两部电影的名字和其对应的豆瓣评分，最后关闭文件，就完成csv文件的写入了。
```python
# 引用csv模块。
import csv

# 调用open()函数打开csv文件，传入参数：文件名“demo.csv”、写入模式“w”、newline=''、encoding='utf-8'。
csv_file = open('demo.csv','w',newline='',encoding='utf-8')
# 用csv.writer()函数创建一个writer对象。
writer = csv.writer(csv_file)
# 调用writer对象的writerow()方法，可以在csv文件里写入一行文字 “电影”和“豆瓣评分”。
writer.writerow(['电影','豆瓣评分'])
# 在csv文件里写入一行文字 “银河护卫队”和“8.0”。
writer.writerow(['银河护卫队','8.0'])
# 在csv文件里写入一行文字 “复仇者联盟”和“8.1”。
writer.writerow(['复仇者联盟','8.1'])
# 写入完成后，关闭文件就大功告成啦！
csv_file.close()
```
现在，我们一行行来看刚刚读取“demo.csv”文件的代码，注释要认真阅读。
```python
import csv
csv_file = open('demo.csv','r',newline='',encoding='utf-8')
reader = csv.reader(csv_file)
for row in reader:
    print(row)
csv_file.close()
# 第1、2行代码：导入csv模块。用open()打开“demo.csv”文件，'r'是read读取模式，newline=''是避免出现两倍行距。encoding='utf-8'能避免编码问题导致的报错或乱码。
# 第3行代码：用csv.reader()函数创建一个reader对象。
# 第4、5行代码：用for循环遍历reader对象的每一行。打印row，就能读取出“demo.csv”文件里的内容。
```

真棒，csv格式文件的写入和读取都被我们搞定了！

补充一点：csv模块本身还有很多函数和方法，附上csv模块官方文档链接：

https://yiyibooks.cn/xx/python_352/library/csv.html#module-csv

这些函数和方法我们不需要全部都记下来，只要在需要用到的时候，学会查询就行。


- 项目:存储与周杰伦的歌曲信息

接下来是简单的复习（刚才选择跳过csv模块的同学，也可以看看csv模块的复习内容，毕竟温故而知新）
```python
# csv写入的代码：

import csv
csv_file = open('demo.csv','w',newline='')
writer = csv.writer(csv_file)
writer.writerow(['电影','豆瓣评分'])
csv_file.close()
```
```python
# csv读取的代码：

import csv
csv_file = open('demo.csv','r',newline='')
reader=csv.reader(csv_file)
for row in reader:
    print(row)
```
```python
# Excel写入的代码：

import openpyxl 
wb = openpyxl.Workbook() 
sheet = wb.active
sheet.title ='new title'
sheet['A1'] = '漫威宇宙'
rows = [['美国队长','钢铁侠','蜘蛛侠','雷神'],['是','漫威','宇宙', '经典','人物']]
for i in rows:
    sheet.append(i)
print(rows)
wb.save('Marvel.xlsx')
```
```python
# Excel读取的代码：

import openpyxl
wb = openpyxl.load_workbook('Marvel.xlsx')
sheet = wb['new title']
sheetname = wb.sheetnames
print(sheetname)
A1_value = sheet['A1'].value
print(A1_value)
```