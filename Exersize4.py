def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Error: Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Invalid input: not enough arguments."
        except Exception as e:
            return f"Unexpected error: {e}"
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


# Проверка на ввод имени корректно (буквами)
def validate_name(name):
    if not name.isalpha():
        return "Invalid name: Name must contain only letters."
    if len(name) <= 1:
        return "Invalid name: name must contain more than 2 letters."
    return None


# Проверка на ввод номера корректно (цифрами) + кол-во
def validate_phone(phone):
    if not phone.isdigit():
        return "Invalid phone number: Phone number must contain only digits."
    if len(phone) <= 9:
        return "Invalid phone number: The phone number must contain more than 10 digits."
    return None


# Добавление имени и номера
@input_error
def add_contact(args, contacts):
    name, phone = args
    error_name = validate_name(name)
    if error_name:
        return error_name
    error_phone = validate_phone(phone)
    if error_phone:
        return error_phone
    contacts[name] = phone
    return "Contact added."


# Смена номера
@input_error
def change_contact(args, contacts):
    name, phone = args
    error_name = validate_name(name)
    if error_name:
        return error_name
    error_phone = validate_phone(phone)
    if error_phone:
        return error_phone
    if name in contacts:
        contacts[name] = phone
        return "Contact updated"
    else:
        return "Error: Contact not found"


# Показ номера
@input_error
def show_phone(args, contacts):
    name = args[0]
    error_name = validate_name(name)
    if error_name:
        return error_name
    if name in contacts:
        return f"The phone number for {name} is {contacts[name]}"
    else:
        return "Error: Contact not found"


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
            # print(contacts)
        elif command == "change":
            print(change_contact(args, contacts))
            # print(contacts)
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(contacts)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
