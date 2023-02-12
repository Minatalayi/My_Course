import arcade

class spaceship():
    ...

class enemy():
    ...


class game(arcade.Window):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.SEA_BLUE)
        self.background=arcade.load_texture("Assignment_13\۲۰۲۲۰۱۱۶_۱۵۲۸۴۴.jpg")
    
    
    #show
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(10,20,800,600,self.background)


window=game()
arcade.run()        