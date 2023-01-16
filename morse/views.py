from django.shortcuts import render

# Forming morse character dictionary
with open("morse-code.csv", "r") as file_name:
    morse_chars = file_name.read()
morse_chars = morse_chars.split('\n')
morse_chars_dictionary = {letter.split(",")[0]: letter.split(",")[1] for letter in morse_chars}


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


def calculate_morse(request):
    context={}
    if request.method=="POST":
        user_string=request.POST.get('user_string')
        calculated_morse=calculate_morse_value(user_string)
        context = {"calculated_morse": calculated_morse,
                   'value': user_string}

    print(context)
    return render(request,'morse_calculator.html',context=context)