
label warning:
    stop music
    stop audio
    play audio ip
    scene black 
    # show logo at truecenter 
    $ renpy.alt("Warning this project contains themes and subjects of violence, suffocation and inner demons. imagery shown may not be fitted for the faint of heart. player discretion is adviced", force=True)
    centered "Warning this project contains themes and subjects of violence, suffocation and inner demons. imagery shown may not be fitted for the faint of heart. player discretion is adviced"
    
    scene black with dissolve
    with Pause(1)
    $ _skipping = True
    $ _dismiss_pause = True
    return

# i have warned you now