import csv
import re


def read_csv_file():
    print("Открываем файл")
    with open("phonebook_raw.csv", encoding='utf8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


# TODO 1: выполните пункты 1-3 ДЗ
contacts = {}
new_contacts = []


def file_processing(csv_list):
    print("Идет обработка файла...")
    for value in csv_list[:]:
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
            index = 0
            for _ in contacts[key]:
                if len(contacts[key][index]) == 0:
                    contacts[key][index] = value[index]
                index += 1
        else:
            contacts[key] = value
    # ===============================
    for elem in contacts.values():
        new_contacts.append(elem)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV


def file_record():
    with open("phonebook.csv", "w", encoding='utf8') as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(new_contacts)


if __name__ == '__main__':
    file_processing(read_csv_file())
    file_record()