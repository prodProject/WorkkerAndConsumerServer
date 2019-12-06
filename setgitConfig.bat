@echo off
SetLocal EnableDelayedExpansion

IF [%1] EQU [] (echo you not selecting any server)
IF [%1] EQU [] (GOTO:EOF)
IF [%2] EQU [] (echo you not selecting any branch)
IF [%2] EQU [] (GOTO:EOF)
heroku git:remote -a %1
git add .
git commit -am "make it better"
git push heroku %2:master

