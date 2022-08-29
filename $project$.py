import sublime
import sublime_plugin
from typing import Optional, List

class $project$Command(sublime_plugin.WindowCommand):

  def run(self) -> None:
    window = self.window

    if window:
      print("$project$ is running")
    else:
      sublime.message_dialog("Could not find Window")

  def is_enabled(self) -> bool:
    return True

  def is_visible(self) -> bool:
    return True
