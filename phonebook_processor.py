import re
import csv


def read_contacts_from_csv(filename_read):
    contacts_list = []

    try:
        with open(filename_read, encoding="utf-8") as f:
            rows = csv.reader(f, delimiter=",")
            next(rows)
            contacts_list = list(rows)
    except FileNotFoundError:
        print(f"Файл {filename_read} не найден.")
    except Exception as e:
        print(f"Ошибка при чтении файла {filename_read}: {e}")

    return contacts_list


def write_contacts_to_csv(data_list, filename_write):
    try:
        with open(filename_write, "w", encoding="utf-8") as f:
            datawriter = csv.writer(f, delimiter=',')
            datawriter.writerows(data_list)
    except Exception as e:
        print(f"Ошибка при записи файла {filename_write}: {e}")


def update_data_list(data_list, lastname, firstname, surname, organization, position, phone_number_full, email):
    for num, data_contact in enumerate(data_list):
        if data_contact[0] == lastname and data_contact[1] == firstname:
            if not data_list[num][3]:
                data_list[num][3] = organization
            if not data_list[num][5]:
                data_list[num][5] = phone_number_full
            if not data_list[num][6]:
                data_list[num][6] = email
            if not data_list[num][4]:
                data_list[num][4] = position
            break
    else:
        data_list.append(
            [
                lastname,
                firstname,
                surname,
                organization,
                position,
                phone_number_full,
                email,
            ]
        )

    return data_list


def format_full_name(contact):
    full_name = " ".join(contact[:3]).split()

    while len(full_name) < 3:
        full_name.append('')

    return full_name


def format_phone(phone):
    if re.search(r'\d', phone):
        digits = re.sub(r'\D', '', phone)

        if digits[0] == '8':
            digits = '7' + digits[1:]

        phone_number = digits[:11]
        phone_number_full = f'+{phone_number[0]}({phone_number[1:4]}){phone_number[4:7]}-{phone_number[7:9]}-{phone_number[9:11]}'
        if len(digits) > 11:
            phone_number_full += f' доб.{digits[11:]}'

        return phone_number_full
    else:
        return ''


def process_contacts(filename_read, filename_write):
    contacts_list = read_contacts_from_csv(filename_read)

    data_list = []

    for contact in contacts_list:
        full_name = format_full_name(contact)

        lastname = full_name[0]
        firstname = full_name[1]
        surname = full_name[2]

        phone = contact[5]
        phone_number_full = format_phone(phone)

        organization = contact[3]
        position = contact[4]
        email = contact[6]

        data_list = update_data_list(
            data_list,
            lastname,
            firstname,
            surname,
            organization,
            position,
            phone_number_full,
            email
        )

    write_contacts_to_csv(data_list, filename_write)
