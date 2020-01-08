import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "my title"
sheet['A1'] = "西游记"
rows = [["唐僧", "孙悟空", "猪八戒", "沙僧"], ["是", "西游记", "里面", "的经典人物"]]
for i in rows:
    sheet.append(i)
print(sheet)
wb.save("xiyouji.xlsx")
