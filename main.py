# you'll have to install this
import pandas as p
import openpyxl


def keyword_stats(data, *keywords) -> None:
    score_and_text = data[['OSAT', 'WHYOSATen']]
    positive_reviews = score_and_text[score_and_text.OSAT >= 7]
    negative_reviews = score_and_text[score_and_text.OSAT <= 3]
    medium_reviews = score_and_text[score_and_text.OSAT.between(4, 7, inclusive=False)]
    print(f"medium associations: \n{p.Series(filter(lambda x: len(str(x)) > 4, ' '.join(medium_reviews['WHYOSATen']).lower().split())).value_counts()[:10]}")
    print(f"positive associations: \n{p.Series(filter(lambda x: len(str(x)) > 4, ' '.join(positive_reviews['WHYOSATen']).lower().split())).value_counts()[:10]}")
    print(f"negative associations: \n{p.Series(filter(lambda x: len(str(x)) > 4, ' '.join(negative_reviews['WHYOSATen']).lower().split())).value_counts()[:10]}")



#infos = p.read_excel(r'C:/Users/Kaeshev_Alapati/PycharmProjects/Lenovo 2022/Vantage March Feedback - Rows1-300 .xlsx')
infos = p.read_excel(r"C:/Users/Kaeshev_Alapati/Downloads/Vantage March Feedback Rows  301 -1000.xlsx")
#infos = p.read_excel(r"C:/Users/Kaeshev_Alapati/Downloads/Vantage Feedback - March 2022 - Intern V1.xlsx")
total_mean_score = round(infos.OSAT.mean(), 2)
print(f"{total_mean_score = }")
mean_response_length = (sum([len(str(item[1])) for item in infos.WHYOSATen.iteritems()]) - len(
    infos.WHYOSATen.index) * 2) / len(infos.WHYOSATen.index)
print(f"{mean_response_length = }")

keyword_stats(infos)

print(infos.OSAT.describe())
