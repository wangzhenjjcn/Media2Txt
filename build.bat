pip install -r requirements.txt
pip install pyinstaller

pyinstaller -y -F -w -n MP4toTXT app.py   --noconsole --add-data "ffmpeg.exe;."
@pause
@pause
@pause
@pause

pyinstaller -y -D -w -n MP4toTXT app.py   --noconsole --add-data "ffmpeg.exe;."
