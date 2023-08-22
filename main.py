from utils import sorting_from_empty, load_file, sorting_from_data, print_to_sum, \
    print_from_to, print_date_description

def main():
    print("Последние 5 выполненых операций:")
    for i in range(5):
        transaction = sorting_from_data(sorting_from_empty(load_file("operations.json")))[i]
        print(f"{print_date_description(transaction)} \n"
            f"{print_from_to(transaction)} \n"
            f"{print_to_sum(transaction)} \n")


if __name__ == "__main__":
    main()

