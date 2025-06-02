# Step 1: Define questions with options and answers
import random
print("Rules:\n1.User will get 1 marks if the answer is correct.\n2.1 marks will be deducted if the answer is wrong.\n3.You can skip the questions and also skip the game.\n")
quiz_questions = [
    {
        "question": "Which of these countries is NOT part of Scandinavia?",
        "options": ["a) Sweden", "b) Norway", "c) Finland", "d) Denmark"],
        "answer": "c"
    },
    {
        "question": "What is the capital city of Canada?",
        "options": ["a) Toronto", "b) Vancouver", "c) Montreal", "d) Ottawa"],
        "answer": "d"
    },
    {
        "question": "Which ocean is the largest and deepest on Earth?",
        "options": ["a) Atlantic Ocean", "b) Indian Ocean", "c) Pacific Ocean", "d) Arctic Ocean"],
        "answer": "c"
    },
    {
        "question": "How many continents are generally recognized on Earth?",
        "options": ["a) 5", "b) 6", "c) 7", "d) 8"],
        "answer": "c"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["a) Ag", "b) Au", "c) Fe", "d) Pb"],
        "answer": "b"
    },
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "options": ["a) Venus", "b) Mars", "c) Jupiter", "d) Saturn"],
        "answer": "b"
    },
    {
        "question": "What gas do plants primarily absorb from the atmosphere for photosynthesis?",
        "options": ["a) Oxygen", "b) Nitrogen", "c) Carbon Dioxide", "d) Hydrogen"],
        "answer": "c"
    },
    {
        "question": "What is the powerhouse of the cell?",
        "options": ["a) Nucleus", "b) Ribosome", "c) Mitochondria", "d) Endoplasmic Reticulum"],
        "answer": "c"
    },
    {
        "question": "Which of the following is the hardest natural substance on Earth?",
        "options": ["a) Gold", "b) Iron", "c) Diamond", "d) Quartz"],
        "answer": "c"
    },
    {
        "question": "What is the approximate percentage of nitrogen in Earth's atmosphere?",
        "options": ["a) 21%", "b) 50%", "c) 78%", "d) 90%"],
        "answer": "c"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["a) Charles Dickens", "b) Jane Austen", "c) William Shakespeare", "d) Mark Twain"],
        "answer": "c"
    },
    {
        "question": "In which year did the Titanic sink?",
        "options": ["a) 1905", "b) 1912", "c) 1918", "d) 1923"],
        "answer": "b"
    },
    {
        "question": "Which famous scientist developed the theory of relativity?",
        "options": ["a) Isaac Newton", "b) Albert Einstein", "c) Stephen Hawking", "d) Galileo Galilei"],
        "answer": "b"
    },
    {
        "question": "The ancient city of Rome is located on which continent?",
        "options": ["a) Asia", "b) Africa", "c) Europe", "d) South America"],
        "answer": "c"
    },
    {
        "question": "Who was the first President of the United States?",
        "options": ["a) Thomas Jefferson", "b) Abraham Lincoln", "c) George Washington", "d) John Adams"],
        "answer": "c"
    },
    {
        "question": "Which of these musical instruments has keys but is also a string instrument?",
        "options": ["a) Trumpet", "b) Flute", "c) Piano", "d) Drum"],
        "answer": "c"
    },
    {
        "question": "Which animated film features a character named Simba?",
        "options": ["a) Finding Nemo", "b) The Lion King", "c) Shrek", "d) Toy Story"],
        "answer": "b"
    },
    {
        "question": "What is the name of the wizard in J.R.R. Tolkien's 'The Lord of the Rings'?",
        "options": ["a) Dumbledore", "b) Merlin", "c) Gandalf", "d) Saruman"],
        "answer": "c"
    },
    {
        "question": "Which iconic band sang the hit song 'Bohemian Rhapsody'?",
        "options": ["a) The Beatles", "b) Led Zeppelin", "c) Queen", "d) Pink Floyd"],
        "answer": "c"
    },
    {
        "question": "Who painted the 'Mona Lisa'?",
        "options": ["a) Vincent van Gogh", "b) Pablo Picasso", "c) Leonardo da Vinci", "d) Claude Monet"],
        "answer": "c"
    }
]
random.shuffle(quiz_questions)
score= 0

for q in quiz_questions:
    print("\n",q["question"])
    for i in q["options"]:
        print(i)
  
    print("Note:Type yes if you want to skip the question.")
    x=input("Enter your answer:").strip().lower()

    if x==q["answer"]:
        print("Correct answer")
        score+=1
    elif x=="yes":
        pass
    else:
        print("Sorry,Wrong answer.") 
        score-=1;
    y=input("Press 1 if you want to quit or simply press enter if you want to continue:")    
    if y=="1":
        break
  

print(f"\n Your score is {score} out of {len(quiz_questions)}")
