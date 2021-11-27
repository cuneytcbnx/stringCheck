import re
INPUT = ("nhoJ (Griffith) nodnoL saw (an) (American) ,tsilevon "
         ",tsilanruoj (and) laicos .tsivitca ((A) reenoip (of) laicremmoc "
         "noitcif (and) naciremA ,senizagam (he) saw eno (of) (the) tsrif "
         "(American) srohtua (to) emoceb (an) lanoitanretni ytirbelec "
         "(and) nrae a egral enutrof (from) ).gnitirw")

CORRECT_ANSWER = "John Griffith London was an American novelist, journalist, and social activist. (A pioneer of commercial fiction and American magazines, he was one of the first American authors to become an international celebrity and earn a large fortune from writing.)"

def fix_text(mystr):
    words = mystr.split()
    for index in range(len(words)):
        if re.findall(r'(\(\w+\))', words[index]):
            words[index] = re.search(r'(\(\w+\))', words[index]).string.replace("(", "", 1).replace(")", "", 1)   
        else:
            words[index]= words[index][::-1]
    return " ".join(words)

if __name__ == "__main__":
    print("Correct!" if fix_text(INPUT) == CORRECT_ANSWER else "Sorry, it does not match with the correct answer.")

