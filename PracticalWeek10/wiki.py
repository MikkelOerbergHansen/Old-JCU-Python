import wikipedia


def main():
    main_menu()


def get_summary(your_search):
    try:
        the_page = wikipedia.page(your_search)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
        option_list = e.options

        while True:
            try:
                number = int(input("Choose from the list: "))
                try:
                    number = int(number)
                except ValueError:
                    print("invalid input; enter a valid number")
                    continue
                if number < 0:
                    print("The number must be >= 0")
                    raise ValueError()
                if number > len(option_list):
                    print("the number must be smaller than {}".format(option_list))
                    raise ValueError
                break
            except ValueError:
                continue

        choice = option_list[number]
        the_page = wikipedia.page(choice)

    print(the_page.title)
    print(the_page.url)
    print(the_page.summary)

    main_menu()


def main_menu():
    your_search = input("search Wikipedia: ")
    if not your_search:
        raise SystemExit(0)
    else:
        get_summary(your_search)


if __name__ == '__main__':
    main()
