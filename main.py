from data_preprocessing.cleaning import clean_data
from data_preprocessing.embedding import embedding_data


def main():

    while True:

        print("\n[1] Clean data")
        print("[2] Embedding data")
        print("\n[0] Exit")
        choice = int(input("\nYour choice ? "))

        if choice == 1:
            clean_data()

        elif choice == 2:
            embedding_data()

        elif choice == 0:
            break


if __name__ == "__main__":
    main()
