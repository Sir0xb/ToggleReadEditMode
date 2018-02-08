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

class OpenAutoCompletionCommand(sublime_plugin.TextCommand):
	def run(self, edit, **kargs):
		if self.view.is_read_only():
			# 向下滚动
			if kargs["keystroke"] == "j":
				self.view.run_command("scroll_lines", { "amount": -3.0 })
			if kargs["keystroke"] == "d":
				self.view.run_command("scroll_lines", { "amount": -10.0 })

			# 向上滚动
			if kargs["keystroke"] == "k":
				self.view.run_command("scroll_lines", { "amount": 3.0 })
			if kargs["keystroke"] == "u":
				self.view.run_command("scroll_lines", { "amount": 10.0 })

			# 顶部 / 底部
			if kargs["keystroke"] == "g":
				self.view.run_command("scroll_lines", { "amount": 50000.0 })
			if kargs["keystroke"] == "G":
				self.view.run_command("scroll_lines", { "amount": -50000.0 })
		else:
			self.view.run_command("insert", { "characters": kargs["keystroke"] })

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
