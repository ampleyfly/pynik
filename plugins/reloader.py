# coding: utf-8

from commands import Command
import os

class ReloadCommand(Command):
	def trig_reload(self, bot, source, target, trigger, argument):
		if has_admin_privileges(source, target):
			svnup_retn = " ".join(os.popen("svn up plugins").read().split("\n"))
			bot.reload_plugins()
			return "Reloaded and good to go! (%s)" % svnup_retn
			
class LoadCommand(Command):
	def trig_load(self, bot, source, target, trigger, argument):
		plugin = argument
		if has_admin_privileges(source, target):
			bot.load_plugin(plugin)
			return "Plugin %s loaded. Use 'reload' to initialize it." % plugin
