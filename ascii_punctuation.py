# -*- coding: utf-8 -*-
import sublime, sublime_plugin

drek = {u'“': '"', u'”': '"', u"’": "'", u"‘": "'", u'—': '-', u'−': '-', u'…': '...', u'•': '-'}
def clean(text):
  for key in drek.keys():
    text = text.replace(key, drek[key])
  return text

class AsciiCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		region = sublime.Region(0, self.view.size())
		text = self.view.substr(region)
		self.view.replace(edit, region, clean(text))
