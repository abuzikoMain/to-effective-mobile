### Требования:

1. Python 3.12 > 
2. Google Chrome версии 115 или новее

### Инструкции по установке и запуску:

## 1. Клонирование репозитория
Сначала клонируйте репозиторий с GitHub и перейдите в проект:
  ```
  git clone https://github.com/abuzikoMain/to-effective-mobile.git
  cd to-effective-mobile
  ```

## 2. Создание виртуального окружения
Рекомендуется создать виртуальное окружение для управления зависимостями проекта:
  ```
  python -m venv .venv
  ```

## 2. Активация виртуального окружения
### linux
  ```
  source .venv/bin/activate
  ```
### windows
  ```
  .\venv\Scripts\activate.bat
  ```

## 3. Установка зависимостей.
Установите зависимости, указанные в requirements.txt:
  ```
  pip install -r requirements.txt
  ```
## 4. Запуск тестов
Теперь вы можете запустить тесты:
```
python test_sauce.py
```
```
python test_git_api.py
```
  

Тест выполнит сценарий, описанный в проекте, и выведет результаты в консоль.

