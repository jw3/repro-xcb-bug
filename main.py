import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from window_assistant import WindowAssistant

app = WindowAssistant()

Gtk.main()
