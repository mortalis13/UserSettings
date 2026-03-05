# Formats Python JSON (dicts, or json with single quotes)

import sublime, sublime_plugin
import json
import ast
from json.decoder import JSONDecodeError

class JsonFormatterCommand(sublime_plugin.TextCommand):
  def run(self, edit, wrap_quotes=True, new_line=False):
    view = self.view
    sel = view.sel()[0]
    if sel.a == sel.b:
      sel = sublime.Region(0, view.size())
    text = view.substr(sel)

    is_json = True
    try:
      data = json.loads(text)
    except JSONDecodeError:
      is_json = False

    if not is_json:
      try:
        data = ast.literal_eval(text)
      except (ValueError, SyntaxError):
        print('JSON Formatter: Could not extract JSON')
        return

    result = json.dumps(data, indent=2)

    view.sel().clear()
    view.sel().add(sel)

    auto_indent = view.settings().get('auto_indent')
    view.settings().set('auto_indent', False)
    view.run_command('insert', {'characters': result})
    view.settings().set('auto_indent', auto_indent)
