## Звіт лабораторної роботи № 2

### Тема: Довгий список параметрів. Надлишкові елементарні типи

### Мета:

* Аналіз та оптимізація методів з великою кількістю параметрів.
* Рефакторинг класів з надлишковими елементарними типами данних.

### Завдання:

#### 1. Оптимізація функції `calculate_score`

* **Зменшення кількості параметрів:**
    * Замість окремих параметрів `score1`, `score2`, ..., `score5` використовуйте один параметр `scores` у вигляді списку або словника.
    * Використовуйте значення за замовчуванням для параметрів `gender`, `height` і `weight`, якщо вони не надаються.
* **Підвищення читабельності:**
    * Використовуйте описові імена змінних.
    * Розбийте код на логічні блоки з використанням коментарів.

#### 2. Рефакторинг класу `User`

* **Використання перерахувань:**
   * Замість констант `type_engineer` і `type_manager` використовуйте перерахування `UserType`.
* **Інкапсуляція:**
   * Змініть атрибути `phone_code` і `phone` на приватні, використовуючи префікс `_`.
   * Додайте метод `get_phone_number()` для доступу до номера телефону.

**Рефакторинг:**

1. Оптимізація функції `calculate_score`
   
Аналіз:

Функція `calculate_score` мала 10 параметрів, що робило її код складним для читання та розуміння.
5 з цих параметрів `(score1, score2, ..., score5)` дублювали один одного, що вело до неефективного використання пам'яті.
Прийняті рішення:

Зменшення кількості параметрів:

Замість 5 окремих параметрів для оцінок використовується один параметр scores у вигляді списку або словника.
Значення за замовчуванням для `gender ("unknown")`, `height (None)` та `weight (None)` дозволяють не вказувати ці параметри при виклик функції.

Підвищення читабельності:

Використані описові імена змінних (`name`, `age`, `gender`, `height`, `weight`, `scores`, `total_score`, `is_adult`).
Код розбитий на логічні блоки з використанням коментарів.

Результат:

Зменшення кількості параметрів з 10 до 6.
Покращення читабельності та розуміння коду.
Ефективніше використання пам'яті.

2. Рефакторинг класу `User`
   
Аналіз:

Клас User використовував константи `type_engineer` та `type_manager` для зберігання типів користувачів.
Ці константи дублювали значення перерахування `UserType`.
Атрибути `phone_code` та `phone` зберігалися як відкриті, що не відповідало принципам інкапсуляції.

Прийняті рішення:

- Використання перерахувань:
Створено перерахування `UserType` з типами користувачів `ENGINEER` та `MANAGER`.
Використання `UserType` замість `type_engineer` та `type_manager` для зберігання типу користувача.
- Інкапсуляція:
Змінено атрибути `phone_code` та `phone` на приватні, використовуючи префікс `_`.
Додано метод `get_phone_number()` для доступу до номера телефону.

Результат:

Покращення структури та організації коду.
Підвищення рівня інкапсуляції.
Зменшення ризику помилок через випадкове змінення приватних атрибутів.

**Висновок:**

В ході лабораторної роботи проведено аналіз та оптимізацію кодів, що дозволило:

Зменшити кількість параметрів та покращити читабельність функції `calculate_score`.
Покращити структуру та інкапсуляцію класу `User`.
Завдяки цим змінам код став більш зрозумілим, лаконічним та стійким до помилок.
