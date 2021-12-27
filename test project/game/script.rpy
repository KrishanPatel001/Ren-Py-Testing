# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define f = Character("Forrest")

# The game starts here.

label start:

    scene bg code

    show forrest wave
    with dissolve

    # These display lines of dialogue.

    f "Hi everyone!"
    f "Not all of you may know me, but I'm Forrest!"
    f "I'll be the one bringing Danganronpa 4: Hello, Hope, to life!"

    show forrest worried
    f "At least... the coding part of it!"

    show forrest happy
    f "This is just a quick little test run that i threw together in order to familarize myself with Renpy, which is what I'll be using to build the game."
    f "Of course, if any issues come up and I need to switch over to another engine, I don't have much of a choice, huh?"

    show forrest worried
    f "To be completely honest, I'm a bit worried about how I'll do, since this is the first major project I've ever worked on."
    f "Especially since I have my next semester of classes starting soon... hopefully I'll have some time to work on this."

    show forrest happy
    f "Currently, I'm hoping to have a working demo by April/May so that I can spend the summer refining and finishing the game."

    show forrest excited
    f "I'm excited to be working on this project with you guys! If you have any questions, feel free to DM me anytime!"
    f "I'll be sending out some more test projects like this over the next week! Don't want to burn myself out right away!"

    show forrest wave
    f "Bye bye for now!"

    # This ends the game.

    return
