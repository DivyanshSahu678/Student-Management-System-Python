from utils.menu import show_menu


def main():

    while True:

        show_menu()

        choice = input("\nEnter Choice : ")

        if choice == "0":
            print("\nThank You 😊")
            break

        else:
            print("\nFeature Coming Soon...")


if __name__ == "__main__":
    main()