basic.show_string("Setting up...")
light_level = input.light_level() - 25
basic.show_string("Setup complete!")

def on_forever():
    if input.light_level() >= light_level and input.pin_is_pressed(TouchPin.P1) == False:
        basic.pause(1500)
        music.play_melody("A - A - A - A - ", 400)
        basic.show_leds("""
            # . . . #
                        # . . . #
                        # . . . #
                        # . . . #
                        . . . . #
        """)
        basic.show_leds("""
            # . . . #
                        # . . # #
                        # . . # #
                        # . . # #
                        . . . # .
        """)
        basic.show_leds("""
            # . . . #
                        # . # # #
                        # . # # #
                        # . # # #
                        . . # . .
        """)
        basic.show_leds("""
            # . . # #
                        # # # # #
                        # # # # #
                        # # # # #
                        . # # . .
        """)
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        . . . . .
        """)
    else:
        basic.clear_screen()
        music.stop_all_sounds()
        basic.pause(500)
basic.forever(on_forever)
