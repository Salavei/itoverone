# itoverone
Импортировать зависимости из requirements.txt  

Создать в корневой папке файл '.env'.выглядеть он должен так:  
ALLOWED_HOSTS=YourHost  
DEBUG=True or False  
SECRET_KEY=YourSecretKey  
DATABASES_ENGINE=YourEngineDB  
DATABASES_NAME=YourNameDB  

Приложение не проверяет наличие ранее созданного изображения  

links:  
http://addres - главная страница  
http://addres/resize_img/ - страница с ссылкой на измененное изображение  
http://addres/admin - страница с админкой  
http://addres/api/ - страница на api  
http://addres/api/id - просматривать по id из БД конкретную запись  

Посмотреть логи можно будет в файле debug.log(в корне проекта)  
