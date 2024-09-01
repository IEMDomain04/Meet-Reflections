# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Story Characters - Name, Color of the Tag
define em = Character("Man", color="#42f551")
define goro = Character("Goro")



# The game starts here.

label start:

    # Welcome Scene
    #"Welcome to Meet Reflections," 
    #"This is more than just a Visual Novel—it's a glimpse into the creator's soul."
    #"Every scene you see, every person you meet, reflects a part of the journey."
    #"Just like in life, these moments shaped who the creator of this game is today."
    #"Basically, each character is a piece of an anime, crafting the story of his present—and his future."
    #"So, enjoy the journey, and maybe, you'll see a reflection of your own life within these moments."

    # Start of the Story
    #Dapat may scene na background about something ganun. 

    #1st Part
    scene bg room
    with fade
    "The Story starts in the Room."

    em "Hello, I'm \"Man\" a Computer Science Student!"

    "This is Man, our main Character in this story."

    "Man usually watches anime in his leasure time. Sometimes, 
    when the character is cool, he tends to adapt his character"

    scene bg livingroom
    with fade
    "Choose what Man will do today."

    return
