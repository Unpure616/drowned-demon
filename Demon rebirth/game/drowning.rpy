label drowning1:
    scene black 
    with Pause(2)
    scene lakeside_night
    play sound "drowning.mp3"
    play music i loop
    with Pause(5)
    show head at Transform(align=(0.8,0.8)) with Dissolve(15)
    pause 15

    scene black with dissolve
    with Pause(5)