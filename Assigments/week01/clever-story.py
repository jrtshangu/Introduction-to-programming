print("Getting the user inputs and printing the prompt message")

#prompt message
print("Please enter the following:")

#getting inputs from the user
adjective=input("Adjective: ")
animal=input("Animal: ")
verb_one= input("Verb: ")
exclamation=input("Exclamation: ")
verb_two= input("Verb: ")
verb_three= input("Verb: ")

#checking if the inputs are correct
print("Your data are successfully received")

#generating a story
story=f"""
    Your story is:\n\n
    The other day, I was in trouble. It all started
    when I saw a very {adjective} {animal}
    {verb_one} down the hallway. "{exclamation}!"
    I yelled. I could think to {verb_two} over and over.
    Miraculously, that caused it to stop, but not before it tried
    to {verb_three} right in front of my family.
"""
print("Story successfully generated!!!")
print("Displaying.....")

print(story)

print("Done!\n Thanks for reading this story")


#writing this story on a file
write_story= open("My Story.txt", "w")
write_story.write(story)
print("This story is already saved on a text file for you")