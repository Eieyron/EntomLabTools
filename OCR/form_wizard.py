import json

page_header = input("Input Questionaire Title: \n>> ")

no_of_questions = int(input("How many questions will you have?: \n>> "))

page_format = {}
page_format["page_header"] = page_header
form_format = {}

for i in range(1, no_of_questions+1):

    question_format = {}

    question_header = input("For question number {}: Input Question Header (max 10 characters): \n>>".format(i))
    while len(question_header) > 10:
        question_header = input("[ERROR] Max Character length reached. \nInput Question Header (max 10 Characters): \n>>")
    question_format["qheader"] = question_header

    question_type = int(input("For question number {}: What is your question type? [1] Multiple Choice [2] Float Input [0] Quit wizard \n>> ".format(i)))
    question_format["qtype"] = question_type

    if question_type == 0:
        break

    elif question_type == 1:

        no_of_choices = int(input("For question number {}: How many choices do you have? (min 2, max 7 choices): \n>> ".format(i)))
        while 2 < no_of_choices > 7:
            no_of_choices = int(input("[ERROR] Max no. of choices reached. \nFor question number {}: How many choices do you have? (min 2, max 7 choices): \n>> ".format(i)))

        question_format["choices"] = []

        for j in range(0, no_of_choices):
            choice_value = input("For question number {}, choice {}: Give the choice value. \n>> ".format(i,j))
            question_format["choices"].append(choice_value)
        
        form_format[i] = question_format
    
    elif question_type == 2:

        # question_format[]

        form_format[i] = question_format

print(form_format)
# json_form_format = json.dumps(form_format) # dumps turns the dictionary to a json object

page_format["form_format"] = form_format

with open("forms/sample.json", "w") as outfile: 

    json.dump(page_format, outfile) # dump dumps the dictionary to a json file