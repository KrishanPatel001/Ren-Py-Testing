define f = Character("Forrest")

label start:

    scene bg code

    show forrest wave
    with dissolve

    f "Hey again! It's me, Forrest!"

    python:
        name = renpy.input("May I ask who's playing today's demo?", length=32)
        name = name.strip()
    f "Cool, it looks like the input worked! But I've got some other things to test out!"

    show forrest excited
    f "Today, I'm gonna be trying out menus/option select!"

    show forrest happy
    f "Let's start with something simple..."
    f "Are you excited to be working on this project with everyone!"

    menu:
        "You bet!":
            jump yes
        "Not really...":
            jump no

    label yes:
        show forrest excited
        f "Great! I'm excited to be working on this too!"
        jump a

    label no:
        show forrest worried
        f "Oh... well I understand that this project can be kinda rough at times, but I believe in you!"

    label a:

    show forrest happy
    f "In the game demos, I'll be sure to put flags into more important decisions so that the game remembers it!"
    f "Let's try something else now..."
    f "What do you think, [name]?"

    show forrest worried
    f "Sorry if I surprised you there! Just wanted to see if the variable saved!"
    f "Besides, I can't really see what you guys put into the text boxes... so you'll just have to let me know in the server"

    show forrest wave
    f "I think that's all I've got for tonight! Another small project, but baby steps, right?"
    f "Bye bye!"

    return
