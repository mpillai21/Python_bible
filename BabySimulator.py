from random import choice
questions=["Why is the sky blue?","Why was I not at my mom's and dad's wedding?!","Why are the stars so high?"]
question=choice(questions)
answer=input(question).strip().lower()
while answer!="just because":
    answer=input("why?:").strip().lower()
print("Oh...okay then")
