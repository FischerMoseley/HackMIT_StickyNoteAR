from StickyJump import *
def launch_game(cv_data = None):
    print("launching game")
    g = StickyJump(cv_data)
    g.show_start_screen()
    while g.running:
        g.new()
        g.show_go_screen()