import subprocess
import os

def setup_arch_aur(package_list_file="aur.lst"):
    # Путь для клонирования yay
    repo_url = "https://aur.archlinux.org/yay.git"
    local_dir = "/tmp/yay"
    # Клонирование репозитория yay
    print(f"Клонирование {repo_url} в {local_dir}")
    subprocess.run(["git", "clone", repo_url, local_dir], check=True)
    # Сборка и установка yay
    print("Сборка yay...")
    subprocess.run(["makepkg", "-si"], cwd=local_dir, check=True)
    print("yay успешно установлен!")
    subprocess.run(["sudo", "rm", "-rf", local_dir])
def setup_arch_pkg(package_list_file="app.lst"):
    # Включаем службу обновления ключей репо
    subprocess.run(["sudo", "systemctl", "enable", "archlinux-keyring-wkd-sync.timer"], check=True)
    # Выполняем обновление
    subprocess.run(["sudo", "pacman", "-Suy"], check=True)

    # Чтение списка пакетов из файла
    try:
        with open(package_list_file, "r") as pkg_file:
            packages = [pkg.strip() for pkg in pkg_file if pkg.strip()]  # Убираем пустые строки
    except FileNotFoundError:
        print(f"Файл {package_list_file} не найден.")
        return

    # Установка всех пакетов одной командой
    if packages:
        subprocess.run(["yay", "-S"] + packages)
        print("Пакеты установлены")
        subprocess.run(["sudo", "mkinitcpio", "-P"])
