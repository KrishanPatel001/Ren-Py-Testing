define f = Character("Forrest")

label start:

    scene bg code

    show forrest wave
    with dissolve
    f "Hey everyone! Glad to see you again!"

    show forrest happy
    f "For today's demo, I'm messing around with the GUI, also known as the Guided User Interface."

    show forrest excited
    f "Today, I'm gonna be trying out menus/option select!"
    f "So... nothing with the actual gameplay, but the aesthetics are still just as important in my opinion!"
    f "Feel free to mess around in the preferences menu and let me know how everything looks"

    show forrest worried
    f "I really want to hear everyone's honest opinions on this, since I'm not really the best at these things..."

    show forrest happy
    f "Well anyways, I guess I should see if these things are working how I want them too, huh?"
    f "*ahem*"

    show forrest excited
    f "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

    show forrest worried
    f "*cough cough*"
    f "Crap... I think I strained myself there, huh? That may have been a bit too much text... gotta remember how many characters can fit in a text box!"
    
    show forrest happy
    f "Anyways... lets test out the buttons next!"
    f "Tell me if you guys like how this is going!"

    menu:
        "Gotcha!":
            jump gotcha
        "Who even are you?":
            jump idk
    
    label gotcha:
        f "Sweet! We... probably shouldn't be using official Dangaronpa assets, but since this is just testing it should be fine!"
        f "Once I know what's needed, I'll let the artists know what needs to be made!"
        jump a
    label idk:
        show forrest worried
        f "Oh... well, I'm Forrest! I'm the programmer for the project!"
        f "You can check out the previous demos on the GitHub page if you'd like!"

    label a:

    show forrest happy
    f "Well, I think that should be it for today!"
    
    show forrest wave
    f "See you guys!"

    return
        
