from datetime import datetime

import requests

'''
fetches partners
'''


def get_partners():
    URL = "https://candidate.hubteam.com/candidateTest/v3/problem/dataset"
    user_key = "28241e17a346c06a15c2c8657f5c"
    PARAMS = {'userKey': user_key}
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()
    return data["partners"]


'''
posts results
'''


def send_results(results):
    URL = "https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=28241e17a346c06a15c2c8657f5c"
    headers = {
        'Content-type': 'application/json',
        'Accept': 'application/json'
    }
    r = requests.post(url=URL, json={"countries": results}, headers=headers)
    print(r.text)

'''
calculates consecutive dates from the given dates
returns list of starting dates
'''


def get_consecutive_dates(date_strs):
    date_format = "%Y-%m-%d"
    dates = [datetime.strptime(d, date_format) for d in date_strs]
    dates.sort()

    consecutive_dates = []
    for i in range(1, len(dates)):
        if (dates[i] - dates[i - 1]).days == 1:
            consecutive_dates.append(dates[i - 1].strftime(date_format))

    return consecutive_dates


'''
keeps track of frequencies of consecutive dates per country
e.g {"Spain" : { "2017-05-07" : 14, "2017-05-09":2 ...},
     "USA": { "2017-05-07" : 7, "2017-05-09":9 ...}
}
'''


def update_valid_dates(consecutive_dates, country, freq):
    if country in freq:
        dates = freq[country]
        for date in consecutive_dates:
            if date in dates:
                dates[date] += 1
            else:
                dates[date] = 1
    else:
        freq[country] = {}
        for date in consecutive_dates:
            freq[country][date] = 1

'''
pick the best consecutive start date which has max frequency
'''


def pick_best_date(avail_dates):
    max_freq = 0
    best_date = None
    for d, f in avail_dates.items():
        if f > max_freq:
            max_freq = f
            best_date = d
    return best_date, max_freq


'''
calculates attendees and their consecutive available dates per country
e.g. {"Spain" : { "2017-05-07" : [abc@gmail.com,cde#gmail.com....]}}
'''


def collect_attendees_group_by_country_and_valid_dates():
    for date in consecutive_dates:
        if country in attendees_by_country:
            if date in attendees_by_country[country]:
                attendees_by_country[country][date].append(email)
            else:
                attendees_by_country[country][date] = [email]
        else:
            attendees_by_country[country] = {date: [email]}


if __name__ == "__main__":

    partners = get_partners()

    # tracks attendees and their consecutive available dates per country
    attendees_by_country = {}

    # tracks frequency of consecutive dates per country
    valid_dates_freq = {}

    for partner in partners:
        email = partner["email"]
        country = partner["country"]
        consecutive_dates = get_consecutive_dates(partner["availableDates"])
        collect_attendees_group_by_country_and_valid_dates()
        update_valid_dates(consecutive_dates, country, valid_dates_freq)

    results = []
    for country, dates in valid_dates_freq.items():
        result = dict()
        result["name"] = country
        result["startDate"], result["attendeeCount"] = pick_best_date(dates)
        result["attendees"] = attendees_by_country[country][result["startDate"]]
        results.append(result)

    send_results(results)