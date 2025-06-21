def read_lines(filename: str) -> list[str]:
    """
    Reads a text file and returns its lines as a list.

    Parameters:
    filename (str): The name of the file to read.

    Returns:
    list[str]: The lines from the file.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []

def main():
    filename = input("Please enter the file name: ").strip()
    lines = read_lines(filename)
    print(f"Line count: {len(lines)}")

if __name__ == "__main__":
    main()
