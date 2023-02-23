@echo off
echo ===========================
echo 请选择命令：
echo ===========================
echo 1.拉取远程仓库
echo 2.准备部署
echo 3.确认信息
echo 4.推送部署
echo 5.一键部署
echo.
set /p input="使用哪种安装方式？1/2/3/4: "
if %input%==1 goto A
if %input%==2 goto B
if %input%==3 goto C
if %input%==4 goto D
if %input%==5 goto E

:A
start cmd.exe /k "@echo 正在拉取远程仓库 && git pull origin main && echo  拉取成功！&& echo. && pause && cls && 部署.bat"
exit

:B
start cmd.exe /k "@echo 准备部署 && git add . && echo  已完成准备工作！&& echo. && pause && cls && 部署.bat"
exit


:C
start cmd.exe /k "@echo 确认信息 && git commit -m "来自PC端 Liam 自动部署的更新推送！" && echo  信息确认无误 && echo. && pause && cls && 部署.bat"
exit

:D
start cmd.exe /k "@echo 正在部署 && git push origin main && echo  部署完成 && echo. && pause && cls && 部署.bat"
exit

:E
start cmd.exe /k "@echo 一键部署启动 正在拉取远程仓库 && git pull origin main && echo 远程仓库与本地仓库资源融合完毕，正在准备新的部署··· && echo.  && git add . && echo 部署工作准备完成，正在进行信息核实··· && echo.  && git commit -m "来自PC端 Liam 自动部署的更新推送！" && echo 信息核实无误，正在部署··· && echo.  && git push origin main && echo 远程部署完成！&& echo. && echo 一键部署成功！ && pause && cls && 部署.bat"
exit

pause

