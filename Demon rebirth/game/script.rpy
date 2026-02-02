# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Avery")

label splashscreen:
    
    scene black 
    show logo at truecenter 
    with Pause(0.1)
  
    play sound "intro_jingle.wav"


    with Pause(5)

    scene black with dissolve
    with Pause(1)
    return


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene lakeside_fog

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    show kana at Transform(zoom=0.3)
    a "im gonan go swim"
    show kana_wintersei_open at Transform(zoom=0.3)
    play audio gig1
    a "hehehehe"

    jump intro
    # This ends the game.

    return
