# tg_bot
Инструкция по запуску через Docker:
1)Открыть папку данного репозитория в VSCode, далее открыть терминал и убедиться что в терминале указан путь до текущей директории (где находится папка), еще нужно перейти в файл dockerfile  и вставить ваш токен ENV TOKEN='our token' (вместо 'our token')
2)Выполить команду docker build . (вместе с точкой, указывает на текущую директорию)
3)После еыполнить команду docker images , там нужно скопировать самый 'свежий' image id (это можно определить по времени в стобце Created)
4)Выполнить команду docker run -d 'тут вставить image id из пункта 3'
5)Вуаля, магия сделана, теперь можете открыть вашего телеграмм бота (ссылка на него у вас должна быть после создания токена) и увидеть что он переделывает полученные ФИО (их надо еще написать, да, мысли он пока читать не умеет) в нужный нам формат.
