# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Avery")

label splashscreen:
    $ _skipping = False
    $ _dismiss_pause = False
    scene black 
    # show logo at truecenter 
    show ren at truecenter
    show unpure 
    with Pause(0.1)
  
    play sound "intro_jingle.wav"


    with Pause(5)

    scene black with dissolve
    with Pause(2)
    jump credit

label credit:
    
    scene black 
    # show logo at truecenter 
    show credit at truecenter,Transform(zoom=2)
    show assets at top
    show credit1 at center, default
    
    with Pause(0.1)
  
    play sound "credit_theme.wav"


    with Pause(5)

    scene black with dissolve
    with Pause(1)
    $ _skipping = True
    $ _dismiss_pause = True
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
    show k f_c at left_char
    a "im gonan go swim"
    show k s_o_m at left_char with Dissolve(0.08)
    play audio gig1
    a "hehehehe"
    

    jump intro 
    # This ends the game.

    return
# k means kana. f or s means frown/smile. o/c means closed/open. so k_f_c = kana frown closed