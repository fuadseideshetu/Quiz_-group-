Q1=""" What is the primary characteristic of mammals? 
   
   A. They lay eggs                    C.They have feathers 

   B. They produce milk for their yuong  D.They live only in water """
Q2=""" Which adaptayion helps birds fly? 
  
   A.Heavy bones       B.Hollow hones      C.Thick fur      D.Large teeth """
Q3=""" Which animal hibernates during winter 

   A.Lion              B.Bear              C.Eagle          D.Shark """
Q4=""" How do fish breath under water 

  A.Through lungs      B.Through gills    C.Through their skin     D.Through their mouth """
Q5=""" What do herbivores primarily eat? 

  A.Meat               B.Plants           C.Both plants and meat    D.Insects """
Q6 ="""How do snake move without legs 
 
  A.By flying          B.By slithering    C.By hopping              D.By rolling """
Q7=""" What is the roll of aqueen bee in ahive? 
 
A.To gather food       B.To lay eggs       C.To protect the hive    D.To build the hive """
Q8 ="""Which animal is nocturnal? 

 A.Owl                 B.Eagle            C.Sparrow                D.Penguin """
Q9=""" In which kingdom would you classifay amold? 

 A.Animalia             B.Fungi            C.Protista               D.Plantae""" 
Q10=""" Anatomy is the study of? 
 
 A.Life                 B.Body structure    C.Cell                  D.Animal """
Q11=""" Which is the magnitude of unit vector?
 
 A.2                 B.1                     C.0            D.10 """
Q12=""" Acar goes from 100m/s to rest in 25s.What is its acceleration? 
 
 A,4m/s**             B.0m/s**                  C.O.25m/s**      D.-4m/s**""" 
Q13=""" Acircuit has asupply voltage of V=63v and R is R=62ohms.calculate the supply current in MA 
 
A.1.020MA             B.1.01MA                C.1020MA            D.100MA """
Q14 ="""              Is the tandency of an object of resist change in motion?  

A.Motion              B.Inertia               C Mass             D.None """
Q15=""" The sum of the measure of an interior angle of any quarilateral is? 

A.180 degree           B.200 degree            C.300 degree      D.360 degree """
Q16=""" How  many tangents are there from an external point to acircle? 

A.2                    B.3                     C.4               D.5 """
Q17=""" Which of the following is correct when 34495 is rounded to 3 significant figure? 

A,345                 B.34500                 C 344             D.3640 """
Q18=""" How many atomic orbitals are reqired form an sp**3 hybridization? 

A.2                   B.6                      C.4               D.8 """
Q19=""" The correct electronic configuration of phospheres with atomic number 16 is ? 

A.2,8,6              B.2,9,5                   C.2,7,7           D.2,6,8  """
Q20=""" Amolecule with covalent bond is? 

A.CuO                B.NaCl                     C.NH3            D.NH4Cl """
Q21=""" If to days after tommorow is 4 days before saturday,what day is it to day? 
 
A.Friday             B.Saturday                 C.Sunday         D.Monday """
Q22=""" Which of the  following can be rearranged in to a 5 latter english word? 

A.PYRIO               B.DWAEP                    C.GOFAT         D.PASEH """
Q23=""" How many days did the student study less than 8 hours? 

A.12                  B.24                        C.6             D.18 """
Q24=""" Which time in hours is the median amount of the study? 

A.4                    B.8                      C.2                D.6 """
Q25=""" What carries oxygen in the blood ? 

A.Hemoglobin           B.Plasma                  C.Platelets       D.All"""   
Question = { 
   Q1 :'B', Q2:'B', Q3:'B', Q4:'B', Q5:'B', Q6:'B', Q7:'B', Q8:'A', Q9:'B',
    Q10:'B', Q11:'B', Q12:'D', Q13:'C', Q14:'B', Q15:'D', Q16:'A', Q17:'B',
     Q18:'B', Q19:'A', Q20:'C', Q21:'C', Q22:'B', Q23:'B', Q24:'A', Q25:'A'
      }
print("Welcome to General Quiz")
name = input("Enter your full name: ")
print(f"Dear {name}, Welcome to Exam Hall")
print("Please ready carefully the following instructions")
print("Instr. 1: Don't forgot to write your full name")
print("Instr. 2: Cheating will nullifyyour total result")

mark = 0
list = ['a', 'b', 'c', 'd']
for item in Question:
    print(item)
    answer = input("Choose the correct answer a/b/c/d: ").upper()
   
    if answer==Question[item]:
        print(f" {answer} is correct answer, you got 2 pts.")
        mark = mark+2
    else:
        print(f"{answer} is incorrect, {Question[item]} is the correct answer")
        mark = mark
    



if mark >= 55:
    print(f"{mark}/50, Excellent")
elif mark >=50:
    print(f"{mark}/50, V.good!")
elif mark >=40:
    print(f"{mark}/50, Gooooood")
elif mark >=50:
    print(f"{mark}/50, Satisfactory")
else:
    print(f"{mark}/50, Failed")
import random

# 25 multiple choice questions (5 per subject)
questions = [
    # English
    {"q": "1. Which word is a synonym of 'happy'?", "options": ["Sad", "Joyful", "Angry", "Tired"], "answer": ["Joyful"]},
    {"q": "2. What is the plural of 'child'?", "options": ["Childs", "Children", "Childes", "Childrens"], "answer": ["Children"]},
    {"q": "3. Which sentence is correct?", "options": ["She go to school.", "She goes to school.", "She going school.", "She goed to school."], "answer": ["She goes to school."]},
    {"q": "4. Which part of speech is the word 'quickly'?", "options": ["Noun", "Verb", "Adjective", "Adverb"], "answer": ["Adverb"]},
    {"q": "5. 'He ___ playing football.'", "options": ["are", "is", "were", "be"], "answer": ["is"]},

    # Chemistry
    {"q": "6. What is the chemical symbol of water?", "options": ["O2", "CO2", "H2O", "HO2"], "answer": ["H2O"]},
    {"q": "7. Atomic number of Carbon is?", "options": ["6", "8", "12", "14"], "answer": ["6"]},
    {"q": "8. Which gas is used by plants in photosynthesis?", "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"], "answer": ["Carbon dioxide"]},
    {"q": "9. pH value less than 7 indicates?", "options": ["Neutral", "Acidic", "Basic", "Salty"], "answer": ["Acidic"]},
    {"q": "10. NaCl is commonly known as?", "options": ["Sugar", "Salt", "Baking soda", "Chalk"], "answer": ["Salt"]},

    # Biology
    {"q": "11. The powerhouse of the cell is?", "options": ["Nucleus", "Mitochondria", "Chloroplast", "Ribosome"], "answer": ["Mitochondria"]},
    {"q": "12. Which blood cells fight infection?", "options": ["Red blood cells", "White blood cells", "Platelets", "Plasma"], "answer": ["White blood cells"]},
    {"q": "13. Plants prepare food by?", "options": ["Respiration", "Photosynthesis", "Digestion", "Fermentation"], "answer": ["Photosynthesis"]},
    {"q": "14. Which organ purifies blood in humans?", "options": ["Heart", "Kidney", "Liver", "Lungs"], "answer": ["Kidney"]},
    {"q": "15. The largest organ in the human body is?", "options": ["Heart", "Skin", "Brain", "Lungs"], "answer": ["Skin"]},

    # Physics
    {"q": "16. SI unit of force is?", "options": ["Joule", "Newton", "Watt", "Pascal"], "answer": ["Newton"]},
    {"q": "17. Speed of light in vacuum is?", "options": ["3x10^8 m/s", "3x10^6 m/s", "1.5x10^8 m/s", "1x10^6 m/s"], "answer": ["3x10^8 m/s"]},
    {"q": "18. Which energy is possessed by a moving body?", "options": ["Potential", "Kinetic", "Thermal", "Nuclear"], "answer": ["Kinetic"]},
    {"q": "19. Earth’s gravity pulls objects towards?", "options": ["Moon", "Sun", "Center of Earth", "North Pole"], "answer": ["Center of Earth"]},
    {"q": "20. 1 kilowatt = ? watts", "options": ["100", "1000", "10", "10,000"], "answer": ["1000"]},

    # Maths
    {"q": "21. Simplify: 12 ÷ 3 × 2", "options": ["2", "6", "8", "10"], "answer": ["8"]},
    {"q": "22. Square root of 81 is?", "options": ["7", "8", "9", "10"], "answer": ["9"]},
    {"q": "23. The value of π is approximately?", "options": ["2.14", "3.14", "4.14", "5.14"], "answer": ["3.14"]},
    {"q": "24. Perimeter of a square with side 5cm is?", "options": ["10cm", "15cm", "20cm", "25cm"], "answer": ["20cm"]},
    {"q": "25. 15% of 200 is?", "options": ["25", "30", "35", "40"], "answer": ["30"]}
]

score = 0

for q in questions:
    print("\n" + q["q"])
    for i, opt in enumerate(q["options"], 1):
        print(f"{i}. {opt}")
    
    try:
        choice = input("Your answer(s) (comma separated, e.g., 2 or 2,3): ").split(',')
        chosen = [q["options"][int(c.strip()) - 1] for c in choice if c.strip().isdigit()]
        if set(chosen) == set(q["answer"]):
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer(s): {', '.join(q['answer'])}")
    except:
        print("Invalid input. Skipping question.")

print(f"\nYour final score: {score}/25")

#this part is done by Fuad

name = input("Enter your name: ")
print(f"\Welcome, {name}! ")
print("This is general quiz")
questions = {
    "Mathematics": [
        {"question": "Solve for x: 2x + 3 = 13", "options": ["A) 4", "B) 6", "C) 7", "D) 5"], "answer": "A"},
        {"question": "The roots of x² - 5x + 6 = 0 are:", "options": ["A) 1 and 6", "B) 2 and 3", "C) 3 and 5", "D) 6 and 2"], "answer": "B"},
        {"question": "A train travels 120 km in 3 hours. Its average speed is:", "options": ["A) 30 km/h", "B) 60 km/h", "C) 40 km/h", "D) 80 km/h"], "answer": "B"},
        {"question": "If the perimeter of a square is 48 cm, the area is:", "options": ["A) 144 cm²", "B) 196 cm²", "C) 121 cm²", "D) 576 cm²"], "answer": "A"},
        {"question": "Simplify: (25 ÷ 5) + (12 ÷ 3)", "options": ["A) 3", "B) 7", "C) 9", "D) 11"], "answer": "D"}
    ],
    "Chemistry": [
        {"question": "Electronic configuration of Sodium (Z = 11):", "options": ["A) 2, 8, 1", "B) 2, 6, 3", "C) 2, 7, 2", "D) 2, 8, 2"], "answer": "A"},
        {"question": "Valency of Oxygen is:", "options": ["A) 1", "B) 2", "C) 3", "D) 4"], "answer": "B"},
        {"question": "Which of the following is a physical change?", "options": ["A) Burning of paper", "B) Melting of ice", "C) Rusting of iron", "D) Cooking rice"], "answer": "B"},
        {"question": "Law of Conservation of Mass states:", "options": ["A) Mass is lost", "B) Mass is gained", "C) Mass is neither created nor destroyed", "D) Mass changes"], "answer": "C"},
        {"question": "Ionic bond is formed by:", "options": ["A) Sharing of electrons", "B) Transfer of electrons", "C) Both A and B", "D) None"], "answer": "B"}
    ],
    "Biology": [
        {"question": "Function of mitochondria:", "options": ["A) Photosynthesis", "B) Protein synthesis", "C) Energy production", "D) Transport"], "answer": "C"},
        {"question": "Xylem transports:", "options": ["A) Food", "B) Water", "C) Oxygen", "D) Hormones"], "answer": "B"},
        {"question": "Photosynthesis produces:", "options": ["A) Oxygen and Glucose", "B) CO2 and Water", "C) Heat and ATP", "D) Protein and Oxygen"], "answer": "A"},
        {"question": "Aerobic respiration requires:", "options": ["A) Oxygen", "B) Nitrogen", "C) No oxygen", "D) Water only"], "answer": "A"},
        {"question": "Oxygen in humans is transported by:", "options": ["A) Platelets", "B) RBC", "C) WBC", "D) Plasma"], "answer": "B"}
    ],
    "English": [
        {"question": "Synonym of 'brave':", "options": ["A) Cowardly", "B) Courageous", "C) Weak", "D) Lazy"], "answer": "B"},
        {"question": "Passive voice of 'The teacher is explaining the lesson':", "options": ["A) The lesson was explained", "B) The lesson is being explained", "C) The teacher explains", "D) The lesson has been explained"], "answer": "B"},
        {"question": "Figure of speech in 'The sun smiled at us':", "options": ["A) Metaphor", "B) Simile", "C) Personification", "D) Hyperbole"], "answer": "C"},
        {"question": "Importance of reading:", "options": ["A) Makes us lazy", "B) Improves knowledge", "C) Wastes time", "D) Is boring"], "answer": "B"},
        {"question": "Correct sentence: She is taller ___ her brother.", "options": ["A) than", "B) then", "C) there", "D) that"], "answer": "A"}
    ],
    "Physics": [
        {"question": "Newton’s First Law is also called:", "options": ["A) Law of Acceleration", "B) Law of Inertia", "C) Law of Gravity", "D) Law of Work"], "answer": "B"},
        {"question": "A car moves with velocity 20 m/s for 10 s. Distance covered =", "options": ["A) 100 m", "B) 150 m", "C) 200 m", "D) 250 m"], "answer": "C"},
        {"question": "SI unit of work is:", "options": ["A) Watt", "B) Joule", "C) Newton", "D) Pascal"], "answer": "B"},
        {"question": "Difference between mass and weight:", "options": ["A) Mass depends on gravity", "B) Weight depends on gravity", "C) Both depend on gravity", "D) Neither"], "answer": "B"},
        {"question": "Splitting of white light by prism is called:", "options": ["A) Reflection", "B) Refraction", "C) Dispersion", "D) Diffraction"], "answer": "C"}
    ],
    "Aptitude": [
        {"question": "If 5 pens cost $75, cost of 8 pens =", "options": ["A) $100", "B) $110", "C) $120", "D) $150"], "answer": "C"},
        {"question": "Average of 4 numbers = 20. Sum =", "options": ["A) 60", "B) 70", "C) 80", "D) 90"], "answer": "C"},
        {"question": "Next term: 2, 4, 8, 16, ?", "options": ["A) 18", "B) 24", "C) 30", "D) 32"], "answer": "D"},
        {"question": "A man walks 3 km east, then 4 km north. Distance from start =", "options": ["A) 5 km", "B) 6 km", "C) 7 km", "D) 8 km"], "answer": "A"},
        {"question": "Boys : Girls = 3 : 2. If 30 students, girls =", "options": ["A) 10", "B) 12", "C) 15", "D) 18"], "answer": "C"}
    ]
}


total_score = 0
total_questions = 0

for subject, questions in questions.items():
    print(f"\n--- {subject} ---")
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        user_ans = input("Your answer (A/B/C/D): ")
        total_questions += 1
        if user_ans.upper() == q["answer"]:
            print("✅ Correct!")
            total_score += 1
        else:
            print(f"❌ Wrong! Correct answer is {q['answer']}")

print(f"\nYour Total Score = {total_score}/{total_questions}")

