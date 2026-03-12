# This lets you easily add the Konami code to your Ren'Py game. When
# the Konami code (up up down down left right left right a b) has been
# entered, this calls the konami_code label (in a new context, so that
# the current game state isn't lost.

init python hide:

    class KonamiListener(renpy.Displayable):

        def __init__(self,):

            renpy.Displayable.__init__(self)

            import pygame
            
            # The label we jump to when the code is entered.
    

            # This is the index (in self.code) of the key we're
            # expecting.
            self.state = 0

            # The code itself.
            self.code = [
                pygame.K_d,
                pygame.K_r,
                pygame.K_o,
                pygame.K_w,
                pygame.K_n,
                ]

        # This function listens for events.
        def event(self, ev, x, y, st):
            import pygame

            # We only care about keydown events.
            if ev.type != pygame.KEYDOWN:
                return

            # If it's not the key we want, go back to the start of the statem
            # machine.
            if ev.key != self.code[self.state]:
                self.state = 0
                return

            # Otherwise, go to the next state.
            self.state += 1

            # If we are at the end of the code, then call the target label in
            # the new context. (After we reset the state machine.)
            if self.state == len(self.code):
                self.state = 0
                renpy.call_in_new_context("wiki")
            
                
            return

        # Return a small empty render, so we get events.
        def render(self, width, height, st, at):
            return renpy.Render(1, 1)


    # Create a KonamiListener to actually listen for the code.
    store.konami_listener = KonamiListener()

    # This adds konami_listener to each interaction.
    def konami_overlay():
        ui.add(store.konami_listener)

    config.overlay_functions.append(konami_overlay)


# This is called in a new context when the konami code is entered.
label wiki:
    
    stop music fadeout(0.5)
    scene red with Dissolve(5)
    $renpy.open_url("https://en.wikipedia.org/wiki/Drowning")
    $renpy.play("note.ogg",channel = "audio")
    $ persistent.drown = True
    play music theme2
    pause 3.3
    $ renpy.quit(relaunch = True)
    return