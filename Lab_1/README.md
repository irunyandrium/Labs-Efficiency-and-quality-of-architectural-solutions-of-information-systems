1. Опис проблеми:

Цей метод можна вважати "довгим", адже він містить умовний оператор, який розрізняє погодинну та фіксовану оплату. Це може призвести до зниження читабельності та ускладнення розуміння логіки коду.
2. Аналіз проблеми:

Проаналізувавши код, можна виділити наступні ділянки, які можна покращити:

Умовний оператор робить код громіздким.
Можна використовувати поліморфізм для обчислення зарплати працівників.
