# print("hello")
# print('this is a sentence')
# print("this is sentence with a 'another' word.")
# print('this is a sentence with a "another" work')
a = "A word"
# print(a)
#
# mutiline  strings
b = """
This is a
multi-line
string
"""
# print(b)
c = '''This is a
multi-line
string'''
# print(c)

# string arrays
text = "word is too big to romming arounf"
# print(text[0]) returns w
# print(text[10])  returns strings index out or range
# print("is" in text)  # returns True
# print("is" not in text)  # returns False
# print(len(text))  # returns 33 (including spaces)


# Slicing

p = "Hello world"

'''
 Index:   0   1   2   3   4   5   6   7   8   9  10
 String:  H   e   l   l   o       w   o   r   l   d
NegIdx: -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1
'''

if False:
    # posible

    # Direaction Left to right (+1)
    print(p[::]) #whole string
    print(p[1::1])
    print(p[1::2]) #el ol
    print(p[1:-5])
    # Direaction  right to left (-1)
    print(p[::-1]) #dlrow olleH
    print(p[1::-1]) #dlrow olleH
    print(p[1:0:-1])
    print(p[9:-9:-1])
    print(p[-1:-10:-1])

    # imposible
    # if direaction is backword
    print("p[2:9:-1]: ",p[2:9:-1],'p[2:9:-1] Not possible')
    print("p[1:-6:-1]: ",p[1:-6:-1],'p[1:-6:-1] Not possible')
    # if direaction is forwaord
    print("p[9:2]: ",p[9:2],'p[9:2] Not possible')
    print("p[6:-11]: ",p[6:-11],'p[6:-11] Not possible')
# strip
if False:
    text = "  \t  Clean Me!  \n  "

    print(text.strip())   # Output: "Clean Me!"
    print(text.lstrip())  # Output: "Clean Me!  \n  "
    print(text.rstrip())  # Output: "  \t  Clean Me!"

    # --- EXAMPLE 2: Using Custom Arguments ---
    url_text = "://www.python.org"
    strip_targets = "g.rto"  # Set becomes {'g', '.', 'r', 't', 'o'}

    cleaned_url = url_text.strip(strip_targets)

    print("--- Custom Argument Example ---")
    print("Original String :", url_text)
    print("Cleaned Output  :", cleaned_url)
    # Why? Left stopped at ':' (not in set).
    # Right deleted 'g','r','o','.' and stopped at 'n' (not in set).
# replace
if False:
    '''
    string.replace(old, new, [count])
    string: The original text you want to modify.
    old: The exact text sequence you want to find and remove.
    new: The new text sequence you want to put in its place.
    count (Optional): A whole number specifying how many times from the left side you want to make the swap
    '''
    # --- EXAMPLE 1: Using the Default Behavior (Replace All) ---
    message = "Error 101: Connection failed. Error 102: Timeout."
    new_message = message.replace('Error',"Alert")
    print("Without Count Parameter",new_message)

    new_message = message.replace("Error",'Alert',1)
    print("With Count Parameter",new_message)
# split
if False:
    # --- EXAMPLE 1: Using Default Behavior (Whitespace) ---
    raw_data = "  apple   \t banana\n\torange  barry\n"
    new_data = raw_data.split()
    print(new_data)

    # --- EXAMPLE 2: Using a Custom Separator ---
    csv_line = "John,Doe,30,New York"
    user_data = csv_line.split(',')
    print(user_data)


    # --- EXAMPLE 3: Using maxsplit Limit ---
    sentence = "one-two-three-four"
    limit_split = sentence.split('-',2)
    print(limit_split)
# Concatination
if False:
    # Normal concatincation
    str1 = "hello"
    str2 = "world"
    result = str1 + str2
    print("Result: ",result)

    # List concatination
    log_pieces = ["2026-07-21", "INFO", "System reboot completed."]
    formatted_logs = "|".join(log_pieces)
    print('formatted Logs: ',formatted_logs)

    # F string method
    modern_output = f"Welcome back {str1}! Your token is {str2}."
    print("mordern: ",modern_output)

    # Litteral Adjencecy
    txt = "hello" "world" # with space
    txt2 = "hello" " " "world"
    txt3 = "hello"
    "world"  #new line
    print(txt,txt2,txt3)
