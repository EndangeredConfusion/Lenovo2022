# you'll have to install this
import pandas as p
import openpyxl


def keyword_stats(data, *keywords) -> str:
    score_and_text = data[['OSAT', 'WHYOSATen']]
    positive_reviews = score_and_text[score_and_text.OSAT >= 7]
    negative_reviews = score_and_text[score_and_text.OSAT <= 3]
    print(f"positive associations: \n{p.Series(filter(lambda x: len(x) > 4, ' '.join(positive_reviews['WHYOSATen']).lower().split())).value_counts()[:10]}")
    print(f"negative associations: \n{p.Series(filter(lambda x: len(x) > 4, ' '.join(negative_reviews['WHYOSATen']).lower().split())).value_counts()[:10]}")


infos = p.read_excel(r'C:/Users/Kaeshev_Alapati/PycharmProjects/Lenovo 2022/Vantage March Feedback - Rows1-300 .xlsx')

total_mean_score = round(infos.OSAT.mean(), 2)
print(f"{total_mean_score = }")
mean_response_length = (sum([len(item[1]) for item in infos.WHYOSATen.iteritems()]) - len(
    infos.WHYOSATen.index) * 2) / len(infos.WHYOSATen.index)
print(f"{mean_response_length = }")

keyword_stats(infos)

print(infos.OSAT.describe())
