import ipywidgets as widgets
from IPython.display import display


def report_card(my_answers, question_list, correct_answers, passing_marks=0.5):
    
    points = 0
    for i in range(len(my_answers)):
        
        print("Question {}: {}".format(i+1, question_list[i]))
        is_correct = (int(my_answers[i].lower() == correct_answers[i].lower()))
        points += is_correct
        print("Your answer: {}, Correct answer: {}, Points: {}".format(my_answers[i], correct_answers[i], is_correct))
        print('\n')    
    
    per = (points/len(my_answers))
    print("You have got {}/{} marks.".format(points, len(my_answers)))
    if per < passing_marks:
        print("Final result: Failed!")
    else:
        print("Final result: Passed! Congratulations!")
        
        
def asses(assesment_dict):

    question_widgets = []
    my_answers = []
    question_list = []
    correct_answers = []
    
    # Create and display widgets for each question
    for i, mc_question in enumerate(assesment_dict):
        print(f"Question {i+1}: {mc_question['question']}")
        options = mc_question['options']
        answer = mc_question['correct_answer']

        radio_options = widgets.RadioButtons(options=options, disabled=False)
        display(radio_options)
        question_widgets.append(radio_options)
        question_list.append(mc_question['question'])
        correct_answers.append(answer)

    # Create a button for submitting the answers
    button = widgets.Button(description="Submit")
    display(button)

    # Define a function to run when the submit button is clicked
    def on_button_clicked(b):
        for i, widget in enumerate(question_widgets):
            my_answers.append(widget.value)
        report_card(my_answers, question_list, correct_answers)    

    # Link the button click event to our function
    button.on_click(on_button_clicked)
    return my_answers, question_list