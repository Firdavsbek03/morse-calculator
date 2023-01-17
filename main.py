def calculate_morse_value(user_string):
    morse_values=[]
    for each_char in user_string:
        if each_char==" ":
            value="......."
        elif each_char==",":
            value="--..--"
        else:
            value=morse_chars_dictionary[each_char.upper()]
        morse_values.append(value)
    return " ".join(morse_values)


# Forming morse character dictionary
with open("morse-code.csv","r") as file_name:
    morse_chars=file_name.read()
morse_chars=morse_chars.split('\n')
morse_chars_dictionary={letter.split(",")[0]:letter.split(",")[1] for letter in morse_chars}

# Starting the application
print("Welcome to the Morse Code Converter!")
while True:
    morse_code=input("Please, enter your string below:\n")
    morse_translated=calculate_morse_value(morse_code)
    print("Equivalent morse value:",morse_translated)