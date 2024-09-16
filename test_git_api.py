from os import getenv
from requests import get, post, delete
from dotenv import load_dotenv

def create_repository():
    """Создание нового публичного репозитория."""
    response = post(API_URL, json={"name": REPO_NAME, "private": False}, auth=(GITHUB_USERNAME, GITHUB_TOKEN))
    if response.status_code == 201:
        print(f"Репозиторий '{REPO_NAME}' успешно создан.")
    else:
        print(f"Ошибка при создании репозитория: {response.json()}")

def check_repository_exists():
    """Проверка наличия репозитория."""
    response = get(API_URL, auth=(GITHUB_USERNAME, GITHUB_TOKEN))
    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            if repo['name'] == REPO_NAME:
                print(f"Репозиторий '{REPO_NAME}' существует.")
                return True
        print(f"Репозиторий '{REPO_NAME}' не найден.")
        return False
    else:
        print(f"Ошибка при получении списка репозиториев: {response.json()}")
        return False

def delete_repository():
    """Удаление репозитория."""
    delete_url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}"
    response = delete(delete_url, auth=(GITHUB_USERNAME, GITHUB_TOKEN))
    if response.status_code == 204:
        print(f"Репозиторий '{REPO_NAME}' успешно удален.")
    else:
        print(f"Ошибка при удалении репозитория: {response.json()}")

if __name__ == "__main__":
    # Загрузка переменных окружения из .env файла
    load_dotenv()

    # Получение переменных окружения
    GITHUB_USERNAME = getenv('GITHUB_USERNAME')
    GITHUB_TOKEN = getenv('GITHUB_TOKEN')
    REPO_NAME = getenv('REPO_NAME')

    # URL для GitHub API
    API_URL = "https://api.github.com/user/repos"

    create_repository()
    if check_repository_exists():
        delete_repository()
