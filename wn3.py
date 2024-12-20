from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

from instr import win_x, win_y, win_width, win_height, txt_index, txt_workheart


class Wnd3(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.init_ui()
        self.connect()
        self.show()

    def init_ui(self):
        v_layout = QVBoxLayout()
        self.setLayout(v_layout)
        index_text = QLabel(txt_index)
        v_layout.addWidget(index_text)
        workheart = QLabel(txt_workheart)
        v_layout.addWidget(workheart)


    def connect(self):
        pass

    def set_appear(self):
        self.setWindowTitle('химия 11 класс арбузов')
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def results(self):
       if self.exp.age < 7:
           self.index = 0
           return "нет данных для такого возраста"
       self.index = (4 * (int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3)) - 200) / 10
       if self.exp.age == 7 or self.exp.age == 8:
           if self.index >= 21:
               return txt_res1
           elif self.index < 21 and self.index >= 17:
               return txt_res2
           elif self.index < 17 and self.index >= 12:
               return txt_res3
           elif self.index < 12 and self.index >= 6.5:
               return txt_res4
           else:
               return txt_res5
       if self.exp.age == 9 or self.exp.age == 10:
           if self.index >= 19.5:
               return txt_res1
           elif self.index < 19.5 and self.index >= 15.5:
               return txt_res2
           elif self.index < 15.5 and self.index >= 10.5:
               return txt_res3
           elif self.index < 10.5 and self.index >= 5:
               return txt_res4
           else:
               return txt_res5
       if self.exp.age == 11 or self.exp.age == 12:
           if self.index >= 18:
               return txt_res1
           elif self.index < 18 and self.index >= 14:
               return txt_res2
           elif self.index < 14 and self.index >= 9:
               return txt_res3
           elif self.index < 9 and self.index >= 3.5:
               return txt_res4
           else:
               return txt_res5
       if self.exp.age == 13 or self.exp.age == 14:
           if self.index >= 16.5:
               return txt_res1
           elif self.index < 16.5 and self.index >= 12.5:
               return txt_res2
           elif self.index < 12.5 and self.index >= 7.5:
               return txt_res3
           elif self.index < 7.5 and self.index >= 2:
               return txt_res4
           else:
               return txt_res5
       if self.exp.age >= 15:
           if self.index >= 15:
               return txt_res1
           elif self.index < 15 and self.index >= 11:
               return txt_res2
           elif self.index < 11 and self.index >= 6:
               return txt_res3
           elif self.index < 6 and self.index >= 0.5:
               return txt_res4
           else:
               return txt_res5
