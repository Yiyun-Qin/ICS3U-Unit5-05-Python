#!/usr/bin/env python3

# Created by Yiyun Qin
# Created in May 2022
# This is the math program, formatting the address


def Mail_Address(
    name, street_number, street, city, province, postal_code, apartment_number=None
):
    # This function returns the string in mail format
    if apartment_number != None:
        mail = (
            name.upper()
            + "\n"
            + "{}".format(apartment_number)
            + "-"
            + "{}".format(street_number)
            + " "
            + street.upper()
            + "\n"
            + city.upper()
            + " "
            + province.upper()
            + "  "
            + postal_code.upper()
        )
    else:
        mail = (
            name.upper()
            + "\n"
            + "{}".format(street_number)
            + ""
            + street.upper()
            + "\n"
            + city.upper()
            + ""
            + province.upper()
            + "  "
            + postal_code.upper()
        )
    return mail


def main():
    # This function does try and catch and input, output
    apartment_number_string = None

    # input
    print("This program formats your address to a mailing address.")
    full_name = input("Enter your full name: ")
    question = input("Do you live in an apartment? (y/n): ")
    if question == "y" or question == "yes":
        apartment_number_string = input("Enter your apartment number: ")
    elif question != "n" or question != "no":
        print("Invalid answer!")
    street_number_string = input("Enter your street number: ")
    street_name = input("Enter your street name AND type (Main St, Express Pkwy...): ")
    city = input("Enter your city: ")
    province = input("Enter your province (as an abbreviation, ex: ON, BC...): ")
    postal_code = input("Enter your postal code: ")

    # process & output
    print("")
    try:
        street_number = int(street_number_string)
        # call functions
        if apartment_number_string != None:
            appartment_number = int(apartment_number_string)
            mail = Mail_Address(
                name=full_name,
                apartment_number=appartment_number,
                street_number=street_number,
                street=street_name,
                city=city,
                province=province,
                postal_code=postal_code,
            )
        else:
            mail = Mail_Address(
                name=full_name,
                street_number=street_number,
                street=street_name,
                city=city,
                province=province,
                postal_code=postal_code,
            )
        print(mail)
    except Exception:
        print("Invalid number!")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
