from phonebook_processor import process_contacts


def main():
    process_contacts(filename_read="phonebook_raw.csv", filename_write="phonebook.csv")


if __name__ == '__main__':
    main()
