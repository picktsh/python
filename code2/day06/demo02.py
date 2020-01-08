# 引用openpyxl
import openpyxl

# 利用openpyxl.Workbook()函数创建新的workbook（工作薄）对象，就是创建新的空的Excel文件。
wb = openpyxl.Workbook()
# wb.active就是获取这个工作薄的活动表，通常就是第一个工作表。
sheet = wb.active
# 可以用.title给工作表重命名。现在第一个工作表的名称就会由原来默认的“sheet1”改为"new title"。
sheet.title = 'new title'
# 把'漫威宇宙'赋值给第一个工作表的A1单元格，就是往A1的单元格中写入了'漫威宇宙'。
sheet['A1'] = '漫威宇宙'
# 先把要写入的多行内容写成列表，再放进大列表里，赋值给rows。
rows = [['美国队长', '钢铁侠', '蜘蛛侠'], ['是', '漫威', '宇宙', '经典', '人物']]
# 遍历rows，同时把遍历的内容添加到表格里，这样就实现了多行写入。
for i in rows:
    # 用sheet.append()就能往表格里添加这一行文字。
    sheet.append(i)
# 打印rows
print(rows)
# 保存新建的Excel文件，并命名为“Marvel.xlsx”
wb.save('Marvel.xlsx')
