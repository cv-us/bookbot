# the purpose of this program is to take in the text of a book from a .txt file and count the number of words in it, the number of letters in it, and the number of times each letter, number, or symbol occurs
def main():
    # set the path to the book
    book_path = "books/frankenstein.txt"
    # store text of book in a variable
    text = get_book_text(book_path)
    # count the number of characters in the book
    num_words = get_num_words(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    output_count(clean_count(count_characters(text)))
    print("--- End report ---")

# function to filter, sort, and print the output of the character count
def clean_count(count):
    # filter out non-letters
    filtered_count = {}
    for key in count:
        if key.isalpha():
            filtered_count[key] = count[key]
    # sort the dictionary by key in reverse order to show highest count first
    sorted_count = dict(sorted(filtered_count.items(), key=lambda item: item[1], reverse=True))
    return sorted_count

def output_count(sorted_count):
    for key in sorted_count:
        print(f"The '{key}' character was found {sorted_count[key]} times")

# function to loop over each character in the giant string of the text of the book and count how many times each character occurs, including letters, numbers, and symbols
def count_characters(text):
    char_count = {}
    for character in text.lower():
        if character in char_count:
            char_count[character] = char_count[character] + 1
        else:
            char_count[character] = 1
    return char_count

# function to count the number of words in the book
def get_num_words(text):
    words = text.split()
    return len(words)

# function to read the text of the book
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
