label drowning1:
    stop audio
    stop music
    stop sound
    scene black 
    with Pause(2)
    
    scene lakeside_night
    play sound "drowning.mp3"
    play music i loop
    with Pause(5)
    show head at Transform(align=(0.8,0.8)) with Dissolve(25)
    pause 15

    scene black with dissolve
    with Pause(5)