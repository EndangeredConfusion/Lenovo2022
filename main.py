# you'll have to install this
import pandas as p
import openpyxl

infos = p.read_excel(r'C:/Users/Kaeshev_Alapati/PycharmProjects/Lenovo 2022/Vantage March Feedback - Rows1-300 .xlsx')

total_mean_score = round(infos.OSAT.mean(), 2)
print(f"{total_mean_score = }")
mean_response_length = sum([len(item[1]) for item in infos.WHYOSATen.iteritems()]) / len(infos.WHYOSATen.index)
print(f"{mean_response_length = }")