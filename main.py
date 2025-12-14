from stats import get_num_words, get_chars_dict, sorted_list
import sys

def get_book_text(filepath):
    #Read the file and return it as a string
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    pathname = sys.argv[1]

    #Get the whole content of a book into a string
    book = get_book_text(pathname)

    #turn the string book into dictionary of chars and their counts
    chars_dict = get_chars_dict(book)

    #create a sorted list out of previous steps, with chars only;
    chars_list = sorted_list(chars_dict)


    ### CRETE A REPORT
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {pathname}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book)} total words")
    print("--------- Character Count -------")

    for char in chars_list:
        print(f"{char['char']}: {char['num']}")

    print("============= END ===============")

   

main()