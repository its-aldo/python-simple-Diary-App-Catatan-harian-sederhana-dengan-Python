print("Welcome to your Diary App!")

diary_entries = []

def display_menu():
    print(25 * "=")
    print("Menu: ")
    print(25 * "-")
    print("1. Add Entry")
    print("2. View Entries")
    print("3. Delete Entry")
    print("4. Exit")
    print(25 * "-")

    while True:
        choice = input("Choose an option (1-4): ")
        if choice in ['1', '2', '3', '4']:
            return choice
        else:
            print("Invalid choice. Please try again.")
            
def add_entry():
    entry = input("Write your diary entry: ")
    diary_entries.append(entry)
    print(25 * "=")
    print("Diary entry added.")

def view_entries():
    if not diary_entries:
        print(25 * "-")
        print("No diary entries found.")
    else:
        print(25 * "-")
        print("Your Diary Entries: ")
        for i, entry in enumerate(diary_entries, start=1):
            print(f"{i}. {entry}")
            print(25 * "-")

def delete_entry():
    view_entries()
    if diary_entries:
        try:
            print(25 * "-")
            entry_number = int(input("Enter the entry number to delete: "))
            if 1 <= entry_number <= len(diary_entries):
                removed_entry = diary_entries.pop(entry_number -1)
                print(25 * "-")
                print("Diary entry deleted.")
            else:
                print(25 * "-")
                print("Invalid entry number.")
        except ValueError:
            print("Please enter a valid number.")

# Main Loop
while True:
    choice = display_menu()
    if choice == '1':
        add_entry()
    elif choice == '2':
        view_entries()
    elif choice == '3':
        delete_entry()
    elif choice == '4':
        print("Exiting Diary App Goodbye!")
        break
