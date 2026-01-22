# Opens the project path in a terminal
# Examples:
# {"keys": ["f10"], "command": "open_terminal", "args": {"cmd": "cmd.exe"}},
# {"keys": ["ctrl+f10"], "command": "open_terminal", "args": {"cmd": "c:/windows-terminal/wt.exe --window last new-tab -d"}},

import sublime
import sublime_plugin

import os
import shlex
import subprocess

class OpenTerminalCommand(sublime_plugin.WindowCommand):
    def run(self, cmd):
        path = os.path.expanduser('~')

        data = self.window.project_data()
        if data:
            project_path = data['folders'][0]['path']
            path = project_path

        else:
            view = self.window.active_view()
            if view and view.file_name():
                path = os.path.dirname(view.file_name())
                print(path)

        path = path.replace('\\', '/')

        cmd = f'{cmd} {path}'
        args = shlex.split(cmd)
        subprocess.Popen(args, cwd=path)
