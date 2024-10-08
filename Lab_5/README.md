## Звіт лабораторної роботи №5

### Тема: Розбіжні модифікації

### Мета:

* Рефакторінг коду з проблемою «Розбіжні модифікації».

### Завдання:

Необхідно провести рефакторинг коду для зменшення залежності від класу.


**Pефакторинг:**

1. Створено окремі класи `ProductSearch`, `ProductDisplay` та `ProductOrder` для розділення відповідних функцій.
2. Клас `Product` був очищений від методів, які виконують дії, які не пов'язані з управлінням самим продуктом.
3. Кожен з нових класів має статичні методи, щоб можна було використовувати їх без створення екземплярів класу.
4. Тепер кожен клас відповідає лише одній відповідальності, що зменшує залежність коду від класу `Product`.

**Висновок:**

Це дозволить легше масштабувати та розуміти код у майбутньому, оскільки кожен клас відповідає за конкретний аспект управління товарами.
