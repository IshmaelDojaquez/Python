from Question import Question

question_prompts = [
    "How many suns are there for the planet Tatooine? \nA. 1 \nB. 2 \nC. 3 \n4. 4\n\n",
    "What species is Jabba? \nA. Ithorian \nB. Jawa  \nC. Hutt \nD. Jenet\n\n",
    "Which order brought about the death of the Jedi? \nA. Order 55 \nB. Order 66 \nC. Order 77 \nD. Order 88\n\n",
    "Who are the only two characters who appear in every Star Wars movie? \nA. Luke & Leia \nB. Han & Chewbacca \nC. Darth Vader & Emperor Palpatine \nD. C-3PO & R2-D2\n\n",
    "On which planet do we first meet Rey in The Force Awakens? \nA. Jakku \nB. Tatooine \nC. Dantooine \nD. Farlax\n\n"
]

questions = [
    Question(question_prompts[0], "B"),
    Question(question_prompts[1], "C"),
    Question(question_prompts[2], "B"),
    Question(question_prompts[3], "D"),
    Question(question_prompts[4], "A"),
]


def run_test(questions):
        print("Welcome to the Star WArs Trivia Game! \nAll answers will be given as A-D choices... \nHave fun and...\nMAY THE FORCE BE WITH YOU!\n")
    score = 0
    for question in questions:
        answer = input(question.prompt).upper()
        if answer == question.answer:
            score += 1
    print(f"You got {str(score)}/{str(len(questions))} correct!")


run_test(questions)
