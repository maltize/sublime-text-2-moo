import random
import sublime
import sublime_plugin

class MakeMoo(sublime_plugin.TextCommand):

  def run(self, edit):
    region = self.view.sel()[0]

    if region.empty():
      sublime.error_message("No selection, no moo!")
      return

    for reg in self.view.split_by_newlines(region):
      sentence = self.moo_string(reg.size())
      self.view.replace(edit, reg, sentence)

  def moo_string(self, size):
    le = 0; st = ""

    while len(st) < size:
      if len(st) != 0:
        st += ' '

      mx = size - len(st)
      if mx > 15:
        sz = 15
        le = random.randint(3, sz)
      else:
        sz = mx
        le = sz

      st += 'm' + 'o' * (le - 1)

    return st
