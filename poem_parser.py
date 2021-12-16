import re
import datetime


def parse_poem(poem_string):
    poems = [i.strip() for i in re.findall(r'####([^#]+)####', poem_string, re.MULTILINE)]
    parsed_poem = []
    for each_poem in poems:
        split = [i.strip() for i in each_poem.split('\n') if i]
        parsed_poem.append([split[0], each_poem[len(split[0]):].strip()])
    return parsed_poem


def parse_date(date_string):
    month, day, year = map(int, re.findall(r'DATE:\s*(\d+)\/(\d+)\/(\d+)', date_string)[0])
    date = datetime.date(year, month, day)
    return date
