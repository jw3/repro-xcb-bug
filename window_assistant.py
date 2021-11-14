import time

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from my_thread import MyThread


class WindowAssistant:

    def __init__(self):

        # load UI glade
        self.builder = Gtk.Builder()
        self.builder.add_from_file("interface.glade")
        self.builder.connect_signals(self)
        self.win_assist = self.builder.get_object("window_assistant")

        # threads
        self.thread_step1 = MyThread(self.callback_step1)
        self.thread_step2 = MyThread(self.callback_step2)
        self.thread_step3 = MyThread(self.callback_step3)
        self.thread_step4 = MyThread(self.callback_step4)
        self.thread1_started = False
        self.thread2_started = False
        self.thread3_started = False
        self.thread4_started = False

        self.win_assist.show()

    def on_window_assistant_cancel(self, widget, data=None):
        self.thread_step1.stop()
        self.thread_step2.stop()
        self.thread_step3.stop()
        Gtk.main_quit()

    def on_window_assistant_show(self, widget, data=None):
        self.thread1_started = True
        self.thread_step1.start()

    def on_window_assistant_apply(self, widget, data=None):
        pass

    def callback_step1(self, value):
        if not self.thread2_started:
            step1_spinner = self.builder.get_object("step1_spinner")
            step1_icon_ok = self.builder.get_object("step1_icon_ok")
            step1_next_msg = self.builder.get_object("step1_next_msg")
            page1 = self.builder.get_object("page1")
            if value:
                step1_spinner.hide()
                step1_icon_ok.show()
                step1_next_msg.show()
                self.win_assist.set_page_complete(page1, True)
                self.thread2_started = True
                self.thread_step2.start()

    def callback_step2(self, value):
        if not self.thread3_started:
            step2_spinner = self.builder.get_object("step2_spinner")
            step2_icon_ok = self.builder.get_object("step2_icon_ok")
            step2_next_msg = self.builder.get_object("step2_next_msg")
            page2 = self.builder.get_object("page2")
            if value:
                step2_spinner.hide()
                step2_icon_ok.show()
                step2_next_msg.show()
                self.win_assist.set_page_complete(page2, True)
                self.thread3_started = True
                self.thread_step3.start()

    def callback_step3(self, value):
        if not self.thread4_started:
            step3_spinner = self.builder.get_object("step3_spinner")
            step3_icon_ok = self.builder.get_object("step3_icon_ok")
            step3_next_msg = self.builder.get_object("step3_next_msg")
            page3 = self.builder.get_object("page3")

            step3_spinner.hide()
            step3_icon_ok.show()
            step3_next_msg.show()
            self.win_assist.set_page_complete(page3, True)
            self.thread4_started = True
            self.thread_step4.start()


    def callback_step4(self, value):
        step4_spinner = self.builder.get_object("step4_spinner")
        step4_icon_ok = self.builder.get_object("step4_icon_ok")
        step4_next_msg = self.builder.get_object("step4_next_msg")
        page4 = self.builder.get_object("page4")

        # mise à jour des objets
        step4_spinner.hide()
        step4_icon_ok.show()
        step4_next_msg.show()
        self.win_assist.set_page_complete(page4, True)
        