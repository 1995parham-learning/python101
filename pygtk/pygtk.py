import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class Base:
    def __init__(self, app):
        self.window = Gtk.ApplicationWindow(application=app)
        self.window.set_title("Parham Alvani")
        self.box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 0)
        self.button = Gtk.Button(label="Button-1")
        self.box.append(self.button)
        self.button.connect("clicked", Base.hello, None)
        self.window.set_child(self.box)
        self.window.connect("destroy", Base.exit, None)
        self.window.present()

    @staticmethod
    def hello(widget, arg):
        """
        :param widget: the widget to operate on
        :param arg: user-supplied data
        :type widget: Gtk.Widget
        :type arg: object
        :return:
        """
        print(widget.get_name())
        print("hello")

    @staticmethod
    def exit(widget, arg):
        """
        :param widget: the widget to operate on
        :param arg: user-supplied data
        :type widget: Gtk.Widget
        :type arg: object
        :return:
        """
        print("bye!")

    @staticmethod
    def main():
        Gtk.run()


if __name__ == "__main__":
    app = Gtk.Application(application_id="com.zetcode.QuitButton")
    app.connect("activate", lambda app: Base(app))
    app.run(None)
