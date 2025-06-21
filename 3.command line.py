import csv
import os

def load_scores(path: str) -> list[tuple[str, int]]:
    if not os.path.exists(path):
        return []
    with open(path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        return [(row[0], int(row[1])) for row in reader]

def add_score(records: list[tuple[str, int]], name: str, score: int) -> None:
    records.append((name, score))

def save_scores(path: str, records: list[tuple[str, int]]) -> None:
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(records)

def top_n(records: list[tuple[str, int]], n: int) -> list[tuple[str, int]]:
    return sorted(records, key=lambda x: x[1], reverse=True)[:n]

def main():
    path = 'scores.csv'
    records = load_scores(path)

    while True:
        print("\nQuiz Score Tracker")
        print("1. Add Score")
        print("2. Show Top Scores")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter the name: ")
            try:
                score = int(input("Enter the score: "))
            except ValueError:
                print("Please enter a valid integer score.")
                continue
            add_score(records, name, score)
            save_scores(path, records)1
            print("Score added.")


        elif choice == '2':
            try:
                n = int(input("How many top scores to show? "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            top_scores = top_n(records, n)
            print("\nTop Scores:")
            for name, sc in top_scores:
                print(f"{name}: {sc}")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
