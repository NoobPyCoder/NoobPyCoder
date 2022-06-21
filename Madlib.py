# Madlib Generator

print("Fill the suitable nouns, pronouns, adjectives, determiner, verb and adverbs replacing __.")
print("\n")
print("Title: The Things You Can See When You Slow Down by Haemin Sunim")
print("-------------------------------------------------------------------")
print("When (pronoun) are joyful, our (noun) opens up to new things.")
print("When we are in a bad (noun2), we can't be open to new things, no matter\
 how (adjective) they are.")
print("Withour joy in our (noun), our progress in (noun3) is slow and (adjective2).")
print("Those who work in a (adjective3), relaxed manner (verb) to work efficiently creatively.")
print("(pronoun2) who work nonstop, driven (adverb) by stress, work without joy.")
print("\n")

"""Taking various input from the user. Hope this works well."""
pronoun = input("Choose pronoun: ")
noun = input("Choose a noun: ")
noun2 = input("Choose another noun: ")
adjective = input("Choose another adjective: ")
noun3 = input("Choos another noun: ")
adjective2 = input("Choose another adjective: ")
adjective3 = input("Choose another adjective: ")
verb = input("Choose a verb: ")
pronoun2 = input("Choose another pronoun: ")
adverb = input("Choose an adverb: ")
print("\n")

"""Using the input from the user, we will build our story
First Method:"""
print("Title: The Things You Can See When You Slow Down by Haemin Sunim")
print("------------------------------------------------------------------")
print("When",pronoun,"are joyful, our",noun," opens up to new things.")
print("When we are in a bad",noun2,", we can't be open to new things, no matter how",adjective,"they are.")
print("Without joy in our",noun,", our progress in",noun3,"is slow and",adjective2,".")
print("Those who work in a",adjective3,", relaxed manner",verb,"to work efficiently creatively.")
print(pronoun2,"who work nonstop, driven",adverb,"by stress, work without joy.")
print("\n")

#Second Method: Using curly braces as a placeholder and format keyword
print("Title: The Things You Can See When You Slow Down by Haemin Sunim")
print("-------------------------------------------------------------------")
print("When {} are joyful, our {} opens up to new things.".format(pronoun, noun))
print("When we are in a bad {}, we can't be open to new things, no matter how {} they\
 are.".format(noun2, adjective))
print("Without joy in our {}, our progress in {} is slow\
 and {}.".format(noun, noun3, adjective2))
print("Those who work in a {}, relaxed manner {} to work efficiently \
creatively.".format(adjective3, verb))
print("{} who work nonstop, driven {} by stress, work without joy.".format(pronoun2, adverb))
print("\n")

#Third Method: using f string
print("Title: The Things You Can See When You Slow Down by Haemin Sunim")
print("----------------------------------------------------------------")
print(f"When {pronoun} are joyful, our {noun} opens up to new things.")
print(f"When we are in bad {noun2}, we can't be open to new things, no matter \
how {adjective} they are.")
print(f"Without joy in our {noun}, our progress in {noun3} is slow and {adjective2}.")
print(f"Those who work in a {adjective3}, relaxed manner {verb} to work \
efficiently and creatively.")
print(f"{pronoun2} who work nonstop, driven {adverb} by stress, work without joy.")
