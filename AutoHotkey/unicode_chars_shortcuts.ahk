; AutoHotkey script, creates shortcuts for printing unicode characters
#NoTrayIcon

; Ctrl+Alt+[nN] => [ñÑ]

^!n::Send , {U+00F1}
^!+n::Send , {U+00D1}
