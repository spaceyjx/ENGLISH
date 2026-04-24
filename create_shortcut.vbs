Set oWS = WScript.CreateObject("WScript.Shell")
sLinkFile = oWS.SpecialFolders("Desktop") & "\英语单词记忆训练.lnk"
Set oLink = oWS.CreateShortcut(sLinkFile)

' 使用VBS启动脚本，避免批处理文件的路径问题
oLink.TargetPath = "F:\GEI\CLI\ENGLISH\启动程序.vbs"
' 设置工作目录为脚本所在目录
oLink.WorkingDirectory = "F:\GEI\CLI\ENGLISH"
' 设置描述
oLink.Description = "英语单词记忆训练程序"
' 设置图标
oLink.IconLocation = "F:\GEI\CLI\ENGLISH\icon.ico,0"
' 保存快捷方式
oLink.Save

' 显示创建成功消息
MsgBox "桌面快捷方式已创建成功！" & vbCrLf & vbCrLf & _
       "快捷方式名称：英语单词记忆训练" & vbCrLf & _
       "位置：桌面" & vbCrLf & _
       "启动方式：VBS脚本（避免路径问题）", vbInformation, "创建成功"