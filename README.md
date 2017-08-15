# Общая информация

Тестируемый класс `class_under_test.py` создан с применением [Type Hints](https://www.python.org/dev/peps/pep-0484/), чтобы часть тестовых случаев была покрыта статическим анализатором [mypy](http://mypy-lang.org). В этом же классе указан пример некорректного использования, чтобы увидеть **mypy** в работе. **mypy** можно использовать в [pre-commit hook](https://git-scm.com/book/ru/v1/Настройка-Git-Перехватчики-в-Git) в Git, чтобы выявлять ошибки еще на стадии commit'а.

# Установка и запуск тестов
```shell
pip install -r requirements.txt
./run.sh
```
