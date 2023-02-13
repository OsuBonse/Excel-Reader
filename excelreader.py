from openpyxl import *
wb = load_workbook(r'...')
sheet_ranges = wb['...']
for row in sheet_ranges.iter_rows(min_col=1, max_col=6):
    for cell in row:
        print(cell.value)
    print()
