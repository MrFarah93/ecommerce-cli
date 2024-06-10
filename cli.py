
from helpers import (
    exit_program,
    add_to_cart,
    update_quantity,
    calculate_total
    
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_to_cart()
        elif choice == "2":
            update_quantity()
        elif choice == "3":
            calculate_total()
       
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. add to cart")
    print("2. update quantity")
    print("3. calculate total price")
    

if __name__ == "__main__":
    main()
