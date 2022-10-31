import re
import csv
from pprint import pprint

phone_pattern = re.compile(r'(\+7|8)\s?\(?\s?(\d{3})\)?\-?\s?(\d{3})\-?(\d{2}\-?\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*')
phone_sub = r'+7(\2)-\3-\4\5\6'


with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def fixing_info(list_: list):

    '''
    standartize all phone numbers
    and fixing other info about persons.
    '''

    fixed_info = []
    for item in contacts_list:
        full_name = ' '.join(item[:3]).split(' ')
        result = [full_name[0], full_name[1], full_name[2], item[3], item[4],
                  phone_pattern.sub(phone_sub, item[5]), item[6]]
        result_ = list(filter(None, result))
        fixed_info.append(result_)
    return fixed_info


pprint(fixing_info(contacts_list))












