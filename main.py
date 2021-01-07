import re
from nltk.corpus import stopwords  # re for split and nltk for stopwords


def read_the_book(file_name):  # Reads the given book and returns clear word dictionary
    return_dict = dict()

    with open(file_name) as file:
        line = file.read()
        splitted = re.split('\\s|\\.|,|\'|"|!|\\?|-|\\(|\\)|:|;|\\*|/|\\+|=|#|>|_|]|\\[|<|‚|%', line)
        # Splitting the line from punctuations and space

        for word in splitted:  # re.split sometimes returns ''.If word != '' and !=numeric, add into the dictionary
            word = word.lower()
            if word != "" and word not in stopwords.words('english') and not word.isnumeric():
                if word not in return_dict:
                    return_dict[word] = 1  # If word is not in dictionary,add it new
                else:
                    return_dict[word] = return_dict[word] + 1  # If word is in dictionary,update its value
    return return_dict


def print_book_statistics(current_book, common_flag=False):  # Prints the given books statistics,
    # if the flag=true printing common words table
    count = input("How many word frequencies they wish to see: ")
    ordered = sorted(current_book.items(), key=lambda x: x[1], reverse=True)  # Sort the dict/book by value

    count = int(count)
    no = 1
    max_digit_number = len(str(ordered[0][1]))  # It's for formatting the table.Calculating the space count
    table_flag = True  # Space count is depends on the maximum length number in a column
    # It is for the getting only once to maximum length numbers of the columns
    for i in ordered:
        if count < 10:  # Lines 32 to 58 is formatting the table,calculating the space sizes.
            print("", end=' ')
        print(no, end=' ')
        print(i[0], end=' ')
        if not common_flag:
            space_count = (8 - (len(i[0]) - 4)) + max_digit_number - len(str(i[1]))
            for k in range(1, space_count):
                print("", end=' ')
            print(i[1])
        else:
            if table_flag:
                max_digit_number_1 = len(str(book_1_words[i[0]]))
                max_digit_number_2 = len(str(book_2_words[i[0]]))
                table_flag = False

            space_count = (8 - (len(i[0]) - 1)) + max_digit_number_1 - len(str(book_1_words[i[0]]))
            for k in range(1, space_count):
                print("", end=' ')
            print(book_1_words[i[0]], end='')
            space_count = 5 + max_digit_number_2 - len(str(book_2_words[i[0]]))
            for k in range(1, space_count):
                print("", end=' ')
            print(book_2_words[i[0]], end=' ')
            space_count = 5 + max_digit_number - len(str(i[1]))
            for k in range(1, space_count):
                print("", end=' ')
            print(i[1])

        count = count - 1
        no = no + 1
        if count ==0:
            break


def print_common_words():  # Calculating the common words between 2 books and returns the dict from common words
    common_words = dict()

    for key in book_1_words:
        if key in book_2_words:
            total_value = book_1_words[key] + book_2_words[key]
            common_words[key] = total_value

    print_book_statistics(common_words, True)  # Send the common words to the printing
    print_distinct_words()


def print_distinct_words():  # Calculates the distinct words dict and send them to the statistics function to print
    distinc_words_in_1 = dict()
    distinc_words_in_2 = dict()

    for key in book_1_words:
        if key not in book_2_words:
            distinc_words_in_1[key] = book_1_words[key]

    for key in book_2_words:
        if key not in book_1_words:
            distinc_words_in_2[key] = book_2_words[key]

    print("\nBOOK 1:", file_name_1[:len(file_name_1) - 4])
    print("DISTINCT WORDS")
    print("NO WORD       FREQ_1")
    print_book_statistics(distinc_words_in_1, False)
    print("\nBOOK 2:", file_name_2[:len(file_name_2) - 4])
    print("DISTINCT WORDS")
    print("NO WORD       FREQ_2")
    print_book_statistics(distinc_words_in_2, False)


# Files must be in the current working directory and in .txt format.
file_name_1 = "Non-Programmer's_Tutorial_for_Python_2.6.txt"
file_name_2 = "Non-Programmer's_Tutorial_for_Python_3.txt"
flag = 1  # Correct input flag, if user enter anything different from 1-2-3-4, provides loop
choice = 4  # Users choice,default exit
book_1_words = dict()  # Book 1 dict
book_2_words = dict()  # Book 2 dict

while flag:  # Getting a correct input
    try:
        choice = int(input("\nPlease select the book(s)\n1- {}\n2- {}\n3- Both(Comparison)\n4- Exit\n".
                           format(file_name_1, file_name_2)))
        if 5 > choice > 0:
            flag = 0
        else:
            print("Please enter a valid number.")  # Entered number is not in 0-5
    except ValueError:  # Entered different from number
        print("Please enter a number.")

if choice == 4:  # Exit condition
    print("Program finished.")
    exit(0)
elif choice == 2:  # Second book statistics condition
    print("BOOK 2:", file_name_2[:len(file_name_2) - 4])
    book_2_words = read_the_book(file_name_2)
    print("NO WORD       FREQ_2")
    print_book_statistics(book_2_words)
elif choice == 3:  # Common and Distinct words statistics condition
    print("BOOK 1:", file_name_1[:len(file_name_1) - 4])
    print("BOOK 2:", file_name_2[:len(file_name_2) - 4])
    print("COMMON WORDS")
    print("NO WORD       FREQ_1 FREQ_2 FREQ_SUM")
    book_1_words = read_the_book(file_name_1)
    book_2_words = read_the_book(file_name_2)
    print_common_words()
else:  # First book statistics condition
    print("BOOK 1:", file_name_1[:len(file_name_1) - 4])
    print("NO WORD       FREQ_1")
    book_1_words = read_the_book(file_name_1)
    print_book_statistics(book_1_words)
