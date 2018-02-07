import sublime, sublime_plugin

settings = None
readonly_default = None
readonly_status = "readonly_status"

def plugin_loaded():
    global settings
    global readonly_default
    settings = sublime.load_settings("ToggleReadEditMode.sublime-settings")
    readonly_default = settings.get("readonly_default")

class ToggleReadEditModeListener(sublime_plugin.EventListener):
	def on_load(self, view):
		if readonly_default:
			view.run_command("set_readonly")
			view.set_status(readonly_status, "readonly")
		else:
			view.run_command("set_writable")
			view.set_status(readonly_status, "writable")

	def on_activated(self, view):
		view.set_status(readonly_status, view.is_read_only() and "readonly" or "writable")

	def on_deactivated(self, view):
		if settings.get("deactivated_lock"):
			view.set_read_only(True)

class SetReadonlyCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.set_read_only(True)
		self.view.set_status(readonly_status, "readonly")

class SetWritableCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.set_read_only(False)
		self.view.set_status(readonly_status, "writable")

class ToggleAutoReadonlyCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if readonly_default:
			settings.set("auto_readonly", False)
		else:
			settings.set("auto_readonly", True)
