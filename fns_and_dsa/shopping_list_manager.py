#!/usr/bin/python3
"""utilizes list to create a simple shopping list manager that allows
users to add items, view the current list, and remove items.
"""

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Name of item to add: ")
            shopping_list.append(item)
        elif choice == '2':
            item = input("Name of item to remove: ")
            shopping_list.pop(item)
        elif choice == '3':
            print('-' * 50)
            if len(shopping_list) > 0:
                for index, item in enumerate(shopping_list):
                    print(f"{index + 1}. {item}")
            else:
                print("EMPTY CHART!")
            print('-' * 50)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
