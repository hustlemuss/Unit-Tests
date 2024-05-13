import json
import requests
import os
import pytest


def load_config(filename):
    with open(filename, "r") as f:
        config = json.load(f)
    return config


config = load_config("config.json")


yandex_disk_token = config.get("yandex_disk_token")


def test_create_folder_positive():
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {"Authorization": "OAuth " + yandex_disk_token}
    params = {"path": "/test_folder"}

    response = requests.put(url, headers=headers, params=params)


    assert response.status_code == 201


    assert check_folder_exists("/test_folder")


def check_folder_exists(folder_path):
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {"Authorization": "OAuth " + yandex_disk_token}
    params = {"path": folder_path}

    response = requests.get(url, headers=headers, params=params)


    return response.status_code == 200 and "name" in response.json()


def test_create_existing_folder_negative():
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {"Authorization": "OAuth " + yandex_disk_token}
    params = {"path": "/test_folder"}  # Попытка создания папки с уже существующим именем

    response = requests.put(url, headers=headers, params=params)


    assert response.status_code == 409


def test_create_folder_no_name_negative():
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {"Authorization": "OAuth " + yandex_disk_token}

    # Не указываем параметр "path" для создания папки без имени
    response = requests.put(url, headers=headers)


    assert response.status_code == 400
