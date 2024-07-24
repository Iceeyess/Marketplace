Создание Фикстур и Команд для загрузки данных по пользователям, каталогу, блогу, полномочиям.
1) Делаем миграции:
python3 manage.py makemigrations
python3 manage.py migrate
2) Запускаем скрипт create_user
python3 manage.py create_user
P.S. есть еще противо-команда python3 manage.py delete_user
Удаление лучше не делать, пока все команды с фикстурами не прогрузятся, так как, если это сделать, то уже каталог не
загрузится, по причине изменения ID в users_user.
3) загружаем каталог. В каталоге есть owner, поэтому там жесткая привязка к Владельцу.
python3 manage.py loaddata catalog.json
4) Запускаем команду создания группы модераторов, и наделяем их полномочиями из задания 23.1
python3 manage.py create_moderators
5) Запускает команду создания группы content_managers и, наделяем их полномочиями из задания 23.1
python3 manage.py create_content_managers
6) Запускаем создание блога в кол-ве 1 шт. Который должен был создать Павлик Кроликов, а проверить может Антоша Гагарин.
python3 manage.py loaddata blog.json