@echo on

:: Create directories
mkdir "your__secccy_appName_goes_here_bb"
cd "flask_app"
mkdir "config"
mkdir "controllers"
mkdir "models"
mkdir "static"
cd "static"
mkdir "css"
mkdir "img"
mkdir "js"
cd ..
mkdir "templates"

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
cd ..
cd "static"
cd "css"
echo. > styles.css
cd ..
cd ..

:: Navigate back to the original directory
cd ..

echo Directory structure created successfully. Press Enter to exit.
pause > nul