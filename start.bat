@echo off
TITLE dc Robot
:: Enables virtual env mode and then starts dc
env\scripts\activate.bat && py -m DCManeger
