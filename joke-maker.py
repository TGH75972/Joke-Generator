import requests
import json
import time

def fetch_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    
    if response.status_code == 200:
        joke = response.json()
        return joke
    else:
        return None

def fetch_multiple_jokes(num_jokes):
    jokes = []
    for _ in range(num_jokes):
        joke = fetch_random_joke()
        if joke:
            jokes.append(joke)
        time.sleep(1) 
    return jokes

def display_joke(joke):
    if joke:
        print(f"Setup: {joke['setup']}")
        print(f"Punchline: {joke['punchline']}")
    else:
        print("Failed to fetch a joke.")

def save_jokes_to_file(jokes, filename):
    with open(filename, 'w') as file:
        json.dump(jokes, file, indent=4)

def load_jokes_from_file(filename):
    try:
        with open(filename, 'r') as file:
            jokes = json.load(file)
            return jokes
    except FileNotFoundError:
        return []

def show_menu():
    print("Random Joke Generator")
    print("1. Get a random joke")
    print("2. Get multiple random jokes")
    print("3. Save jokes to file")
    print("4. Load jokes from file")
    print("5. Exit")
    choice = input("Choose an option: ")
    return choice

def main():
    saved_jokes = []
    while True:
        choice = show_menu()
        
        if choice == '1':
            joke = fetch_random_joke()
            display_joke(joke)
        
        elif choice == '2':
            num_jokes = int(input("Enter the number of jokes: "))
            jokes = fetch_multiple_jokes(num_jokes)
            for joke in jokes:
                display_joke(joke)
            saved_jokes.extend(jokes)
        
        elif choice == '3':
            filename = input("Enter the filename to save jokes: ")
            save_jokes_to_file(saved_jokes, filename)
            print(f"Saved {len(saved_jokes)} jokes to {filename}.")
        
        elif choice == '4':
            filename = input("Enter the filename to load jokes: ")
            jokes = load_jokes_from_file(filename)
            for joke in jokes:
                display_joke(joke)
            saved_jokes.extend(jokes)
            print(f"Loaded {len(jokes)} jokes from {filename}.")
        
        elif choice == '5':
            print("Exiting the Random Joke Generator. Have a great day!")
            break
        
        else:
            print("Invalid choice. Please try again.")

        print("\n")

if __name__ == "__main__":
    main()
