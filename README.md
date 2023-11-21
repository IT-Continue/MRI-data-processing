# MRI-data-processing
 Разработка программного обеспечения предобработка сырых данных с магнитнорезонансной томографии

## Windows
0. [Скачайте Python](https://www.python.org/downloads/), версия Python должна быть 3.11.3 или выше
1. Клонируйте репозиторий 
```bash
git clone https://github.com/IT-Continue/MRI-data-processing.git

```
или скачайте архивом

2. Зайдите в папку с проектом
```bash
cd MRI-data-processing

```
3. Создайте виртуальное окружение
```bash
# Сначала установим пакет virtualenv
pip install virtualenv

# Затем создаём наше виртуальное окружение 
virtualenv venv

```
4. Активируйте виртуальное окружение
```bash
venv\scripts\activate

```
5. Запустите init.py
```bash
.\init.py

```
6. Скачайте необходимые библиотеки
```bash
pip install -r requirements.txt

```
7. Положите в директорию raw_data файлы: schem.npy и shuffeld_kspace.npy
8. Запустите скрипт raw_to_image.py, в папке output должен появится файл output.png
