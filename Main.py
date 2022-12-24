from pprint import pprint
import csv
import re


def read_csv_file():
    with open("phonebook_raw.csv", encoding='utf8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


# TODO 1: выполните пункты 1-3 ДЗ
# RE"\+?[7|8]?\s?\(?(\d\d\d)\)?\s?\-?(\d\d\d)\-?\s?(\d\d)\-?\s?(\d\d)\s?\(?(доб.\s?\d{2,4})?\)?"
# RE"+7(\1)\2 \3 \4 \5"
contacts = {}


def file_processing(csv_list):
    for value in csv_list[:]:
        # print(f"{value[0]} / {len(value[3:])}")
        pprint(f" -- {len(value)}")
        pattern = re.sub(
            r"\+?[7|8]?\s?\(?(\d\d\d)\)?\s?\-?(\d\d\d)\-?\s?(\d\d)\-?\s?(\d\d)\s?\(?(доб.\s?\d{2,4})?\)?",
            r"+7(\1)\2-\3-\4 \5",
            value[5])
        value[5] = pattern
        s = value[0].split()
        if len(s) == 3:
            value[0] = s[0]
            value[1] = s[1]
            value[2] = s[2]
        elif len(s) == 2:
            value[0] = s[0]
            value[1] = s[1]
        elif len(s) == 1 and len(value[1].split()) == 2:
            d = value[1].split()
            value[1] = d[0]
            value[2] = d[1]
        key = value[0]+" "+value[1]
        if key in contacts:
            print(contacts[key], len(contacts[key]))
            print(value, len(value))
            # index = 0
            # for _ in contacts[key]:
            #     if len(contacts[key][index]) == 0:
            #         contacts[key][index] = value[index]
            #     index += 1
        else:
            contacts[key] = value

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#     datawriter = csv.writer(f, delimiter=',')
#     # Вместо contacts_list подставьте свой список
#     datawriter.writerows(contacts_list)


if __name__ == '__main__':
    file_processing(read_csv_file())
