@echo off
title 'JybTest'
COLOR 0E
:begin
python run.py
TIMEOUT /T 100
goto begin
exit




