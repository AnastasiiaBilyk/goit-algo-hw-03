from datetime import datetime

date_today = datetime.today()

def get_days_from_today(date):

    try:
        date_formatted = datetime.strptime(date, "%Y-%m-%d")
        diff_date = (date_today - date_formatted).days
        return diff_date
    except:
        print('Некоректний формат дати. Введіть дату у форматі yyyy-mm-dd:')

result = get_days_from_today("2025-04-12")
print(result)