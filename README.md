Перед запуском выполнить:  
export FLASK_DEBUG=True  
export FLASK_APP=run.py  

пример запроса:  
POST /perform_query/?cmd1=filter&value1=GET&file_name=apache_logs.txt&cmd2=map&value2=0&cmd3=unique&value3=%22%22&cmd4=sort&value4=desc&cmd5=limit&value5=15

Проект работает с любым количеством аргументов  
