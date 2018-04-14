from kivy.app import App
from kivy.uix.widget import Widget

from kivy.graphics import (Color, Ellipse, Rectangle, Line)


class PainterWidget(Widget):
    def __init__(self, **kwargs):
        super(PainterWidget, self).__init__(**kwargs)

        with self.canvas:
            Color(0, 1, 0, 1)
            Ellipse(pos=(200, 200),
                    size=(50, 50))
            Rectangle(pos=(500, 100),
                      size=(200, 300))
            Line(points=(200,400,250,500,300,400),
                 width=5,
                 close=True)
            self.line = Line(points=(),
                             width=5,
                             cap='square',
                             joint='miter')

    def on_touch_down(self, touch):
        self.line.points += (touch.x,touch.y)


class PaintApp(App):
    def build(self):
        return PainterWidget()


if __name__ == '__main__':
    PaintApp().run()
