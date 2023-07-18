echo off
chcp 936
set DestPath=%~dp0
python D:\Apps\Git\text_to_voice\text_to_voice.py %1 run
