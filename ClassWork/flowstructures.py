'''marks = 80
result = " "
if marks <30:
    result ="failed"
elif marks > 75:
    result = "passed with distinction"
else:
    result = "passed"
print(result)

#next exercise
def checkVowel(n):
   match n:
     case 'a': return "vowel alphabet"
     case 'e': return "vowel alphabet"
     case 'i': return "vowel alphabet"
     case 'o': return "vowel alphabet"
     case 'u': return "vowel alphabet"
     case _: return "simple alphabet"
      
print(checkVowel('a'))
print(checkVowel('e'))
print(checkVowel('m'))'''
#another exercise
bike = "BmW"

if bike == "Hero":
  print("bike is Hero")
elif bike == "suzuki" :
  print("this bike is suzuki")
elif bike == "yahama":
   print("bike is yamaha") 
else: 
   print("input another value")
  
  
