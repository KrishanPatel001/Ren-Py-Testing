define f = Character("Forrest")

label start:

    scene bg code
    with fade

    show forrest wave
    with dissolve
    f "Hey guys! I'm back again with another demo!"

    show forrest excited
    f "I'm actually really excited to show you guys today's demo!"
    f "This is actually something gameplay related! It's... room exploration!"

    show forrest worried
    f "Maybe that's not the best way to put it... but I think you guys get what I mean!"

    show forrest happy
    f "Pretty much, this demo will let you click things to take a closer look and get more info!"
    f "And for the test room... why not take a look at the room that started it all: Makoto Naegi's room!"
    f "Look around to your heart's content, and when you're done just click the exit button!"

    show forrest wave
    f "Have fun!"

    scene bg room
    with fade
    call screen pointAndClick

    label bed:
        show forrest happy
        f "Here's Makoto's bed! Hopefully Kyoko doesn't sneak up on him while he's sleeping anymore..."
        scene bg room
        call screen pointAndClick
    
    label metal:
        show forrest worried
        f "Those huge metal panels kept everyone trapped in Hope's Peak... not even Sakura could break them..."
        scene bg room
        call screen pointAndClick

    label camera:
        show forrest worried
        f "Monokuma was watching everyone through those cameras... kinda creepy..."
        scene bg room
        call screen pointAndClick
    
    label door:
        show forrest happy
        f "The door to Makoto's bathroom."
        f "I'm pretty sure that it was actually creaky or broken... fitting for the Ultimate Lucky Student."
        show forrest worried
        f "Oh, and a certain uh... 'incident' took place here too..."
        scene bg room
        call screen pointAndClick
    
    label tv:
        show forrest happy
        f "This is where Monokuma would give all of his announcments."
        show forrest excited
        f "A body has been discovered!"
        show forrest happy
        f "I can actually do a pretty good Monokuma impression!"
        scene bg room
        call screen pointAndClick

    label sword:
        show forrest worried
        f "I... don't remember if there was any context as to why Makoto just... had a sword in his room."
        f "You guys'll have to correct me if I'm wrong."
        scene bg room
        call screen pointAndClick

    label exit:
        show forrest happy
        f "I hope you had fun looking around! Things'll get a bit complicated with more rooms, but I'm up for the task!"
        show forrest wave
        f "See you guys next time!"
        return

    screen pointAndClick:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.28
            ypos 0.76
            idle "bed.png"
            action Jump("bed")

        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.245
            ypos 0.465
            idle "metal.png"
            action Jump("metal")

        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.1
            ypos 0.37
            idle "camera.png"
            action Jump("camera")
        
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.56
            ypos 0.56
            idle "door.png"
            action Jump("door")

        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.71
            ypos 0.45
            idle "tv.png"
            action Jump("tv")

        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos .89
            ypos 0.6
            idle "sword.png"
            action Jump("sword")

        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.9
            ypos 0.45
            idle "exit.png"
            action Jump("exit")

