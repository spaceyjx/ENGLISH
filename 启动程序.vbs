Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

currentDir = fso.GetParentFolderName(WScript.ScriptFullName)
programPath = currentDir & "\vocab_trainer.py"

pythonPaths = Array( _
    "D:\PYTHON\python.exe", _
    "C:\Python311\python.exe", _
    "C:\Python310\python.exe", _
    "python.exe" _
)

pythonFound = False
For Each pythonPath In pythonPaths
    If fso.FileExists(pythonPath) Or InStr(pythonPath, ".exe") = 0 Then
        On Error Resume Next
        WshShell.Run """" & pythonPath & """ --version", 0, True
        If Err.Number = 0 Then
            On Error GoTo 0
            WshShell.CurrentDirectory = currentDir
            WshShell.Run """" & pythonPath & """ vocab_trainer.py", 0, False
            pythonFound = True
            Exit For
        End If
        On Error GoTo 0
    End If
Next

If Not pythonFound Then
    MsgBox "未检测到Python环境！" & vbCrLf & vbCrLf & _
           "请先安装Python 3.6或更高版本" & vbCrLf & _
           "下载地址：https://www.python.org/downloads/" & vbCrLf & _
           "安装时请勾选 ""Add Python to PATH""", vbCritical, "启动失败"
End If
