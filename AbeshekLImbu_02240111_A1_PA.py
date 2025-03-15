import math

def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(begin, finish):
    total_sum = 0
    for n in range(begin, finish + 1):
        if is_prime_number(n):
            total_sum += n
    return total_sum

def convert_length(amount, conversion_type):
    if conversion_type.upper() == 'M':
        return round(amount * 3.28084, 2) 
    elif conversion_type.upper() == 'F':
        return round(amount / 3.28084, 2)  
    else:
        raise ValueError("Invalid conversion type. Use 'M' for meters to feet or 'F' for feet to meters.")

def count_consonants(input_text):
    vowel_set = "aeiouAEIOU"
    consonant_list = [char for char in input_text if char.isalpha() and char not in vowel_set]
    return len(consonant_list)

def find_min_max(*args):
    if not args:
        raise ValueError("At least one number must be provided.")
    smallest_value = min(args)
    largest_value = max(args)
    return f"Smallest: {smallest_value}, Largest: {largest_value}"

def is_palindrome(input_string):
    sanitized_string = ''.join(char.lower() for char in input_string if char.isalnum())
    return sanitized_string == sanitized_string[::-1]

def count_words_in_file(file_location, words_to_count):
    try:
        with open(file_location, 'r') as file:
            file_content = file.read().lower()
            word_count_dict = {word: file_content.split().count(word) for word in words_to_count}
            return word_count_dict
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_location} was not found.")
        
def main_program():
    words_to_count = ["the", "was", "and"]
    while True:
        print("\nAvailable Functions:")
        print("1. Prime Number Sum Calculator")
        print("2. Length Unit Converter")
        print("3. Count consonants in string")
        print("4. Find min and max numbers")
        print("5. Check for palindrome")
        print("6. Word Counter")
        print("0. Exit program")
        
        user_choice = input("\nEnter your choice: ").strip()
        
        try:
            if user_choice == '1':
                start_range = int(input("Enter the start of the range: "))
                end_range = int(input("Enter the end of the range: "))
                result_sum = sum_of_primes(start_range, end_range)
                print(f"Sum of prime numbers in the range {start_range}-{end_range}: {result_sum}")
            
            elif user_choice == '2':
                numeric_value = float(input("Enter a numeric value: "))
                conversion_direction = input("Enter conversion direction ('M' for meters to feet, 'F' for feet to meters): ").strip()
                converted_value = convert_length(numeric_value, conversion_direction)
                print(f"Converted value: {converted_value}")
            
            elif user_choice == '3':
                input_string = input("Enter a string: ")
                consonant_count = count_consonants(input_string)
                print(f"Number of consonants: {consonant_count}")
            
            elif user_choice == '4':
                number_list = list(map(int, input("Enter numbers separated by space: ").split()))
                min_max_result = find_min_max(*number_list)
                print(min_max_result)
            
            elif user_choice == '5':
                input_string = input("Enter a string: ")
                palindrome_result = is_palindrome(input_string)
                print(f"Is palindrome: {palindrome_result}")
            
            elif user_choice == '6':
                file_path = input("Enter the file path: ").strip()
                word_counts = count_words_in_file(file_path, words_to_count)
                print(f"Word counts: {word_counts}")
            
            elif user_choice == '0':
                print("Exiting program...")
                break
            
            else:
                print("Invalid choice, please enter a number between 0 and 6.")
        
        except ValueError as e:
            print(f"Error: {e}")
        except FileNotFoundError as e:
            print(f"Error: {e}")
        
        continue_prompt = input("\nWould you like to try another function? (y/n): ").strip().lower()
        if continue_prompt != 'y':
            break

if __name__ == "__main__":
    main_program()