from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget


class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    V_NB_LINES = 7
    V_LINES_SPACING = .1  # percentage in screen width
    vertical_lines = []

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        # print("INIT W:" + str(self.width) + " H:" + str(self.height))
        self.init_vertical_lines()
    

    def on_parent(self, widget, parent):
        # print("ON PARENT W:" + str(self.width) + " H:" + str(self.height))
        pass

    def on_size(self, *args):
        # print("ON SIZE W:" + str(self.width) + " H:" + str(self.height))
        # self.perspective_point_x = self.width/2
        # self.perspective_point_y = self.height * 0.75
        self.update_vertical_lines()
        # self.update_horizontal_lines()
        

    def on_perspective_point_x(self, widget, value):
        # print("PX: " + str(value))
        pass

    def on_perspective_point_y(self, widget, value):
        # print("PY: " + str(value))
        pass

    def init_vertical_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            #self.line = Line(points=[100, 0, 100, 100])
            for i in range(0, self.V_NB_LINES):
                self.vertical_lines.append(Line())

    def update_vertical_lines(self):
        central_line_x = int(self.width / 2)
        spacing = self.V_LINES_SPACING * self.width
        offset = -int(self.V_NB_LINES/2)+0.5
        for i in range(0, self.V_NB_LINES):
            line_x = central_line_x + offset*spacing

            x1, y1 = self.transform(line_x, 0)
            x2, y2 = self.transform(line_x, self.height)
            self.vertical_lines[i].points = [x1, y1, x2, y2]
            offset += 1

    def transform(self, x, y):
        # return self.transform_2D(x, y)
        return self.transform_perspective(x, y)

    def transform_2D(self, x, y):
        return int(x), int(y)

    def transform_perspective(self, x, y):
        lin_y = y * self.perspective_point_y / self.height
        if lin_y > self.perspective_point_y:
            lin_y = self.perspective_point_y

        diff_x = x-self.perspective_point_x
        diff_y = self.perspective_point_y-lin_y
        factor_y = diff_y/self.perspective_point_y  # 1 when diff_y == self.perspective_point_y / 0 when diff_y = 0
        factor_y = pow(factor_y, 4)

        tr_x = self.perspective_point_x + diff_x*factor_y
        tr_y = self.perspective_point_y - factor_y*self.perspective_point_y

        return x, lin_y

class GalaxyApp(App):
    pass


GalaxyApp().run()
