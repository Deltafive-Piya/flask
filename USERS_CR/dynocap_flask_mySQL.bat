@echo on

:: Prompt user for project name or set a default name
set "defaultprojectname=dynocap_app"
set /p "projectname=Enter project name (or press Enter for default - %defaultprojectname%): "
if "%projectname%"=="" set "projectname=%defaultprojectname%"

@REM @REM @REM @REM @REM @REM @REM @REM @REM Bring me back alive if you want a file randomly created with no format suffix
@REM :: Prompt user for file name
@REM set /p "filename=Enter file name: "

:: Create the project folder
mkdir "%projectname%"

:: Navigate into the project folder
cd "%projectname%"

:: Create directories
mkdir "config"
mkdir "controllers"
mkdir "models"
mkdir "static"
mkdir "templates"
cd "static"
mkdir "css"
mkdir "img"
mkdir "js"
cd ..
cd "templates"
echo. > index.html
cd ..

:: Create files
cd "config"
echo. > mysqlconnection.py
cd ..
cd "controllers"
echo. > controller_user.py
echo You will have a controller file for every table in your database > controller_Readme.md
cd ..
cd "models"
echo. > model_user.py
echo You will have a model file for every table in your database > model_user_Readme.md
cd "static"
cd "css"
echo. > styles.css
cd ..
cd ..

:: Create the file inside the project folder
echo. > "%filename%"

echo.
echo.
echo.
echo Directory structure created successfully.
echo.
echo.
echo File "%filename%" created.
echo.
echo.
echo Thank you; Press Enter.Key to exit()