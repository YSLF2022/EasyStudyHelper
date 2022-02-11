Dim WSHShell
Set WSHShell = WScript.CreateObject("WScript.Shell")
WSHShell.RegDelete("计算机\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\ADMX_ShellCommandPromptRegEditTools\DisableCMD")
WSHShell.RegDelete("计算机\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\ADMX_ShellCommandPromptRegEditTools\DisableRegedit")
msgbox("done") 