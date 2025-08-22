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
