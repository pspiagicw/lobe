import gi

from gi.repository import Gtk


class MyWindow(Gtk.Window):

    """Docstring for Mywindow. """

    def __init__(self):
        """TODO: to be defined. """
        Gtk.Window.__init__(self)

        self.button = Gtk.Button(label='Click Here')
        self.button.connect("clicked",self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self,widget):
        print("Hello World")

win = MyWindow()
win.connect('destroy',Gtk.main_quit)
win.show_all()
Gtk.main()
