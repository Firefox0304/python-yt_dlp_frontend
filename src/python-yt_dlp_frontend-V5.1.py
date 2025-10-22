import os
import sys
import subprocess
from pathlib import Path
import shutil
import platform

try:
    import winshell
    from win32com.client import Dispatch
except ImportError:
    winshell = None

# 判斷程式是被打包成 EXE 還是原本的 .py
if getattr(sys, 'frozen', False):  # EXE 模式
    BASE_FOLDER = Path(sys.executable).parent / "yt-dlp_downloads"
else:  # .py 開發模式
    BASE_FOLDER = Path.cwd() / "yt-dlp_downloads"

CONFIG_FOLDER = BASE_FOLDER / "config"
DEFAULT_FOLDER = BASE_FOLDER / "預設"
DEFAULT_MP3 = DEFAULT_FOLDER / "MP3"
DEFAULT_MP4 = DEFAULT_FOLDER / "MP4"

SHORTCUT_NAME = "yt-dlp_可視化下載器.lnk"
NEVER_REMIND_FILE = CONFIG_FOLDER / "never_remind_shortcut.txt"

def ensure_folders():
    for folder in [BASE_FOLDER, CONFIG_FOLDER, DEFAULT_FOLDER, DEFAULT_MP3, DEFAULT_MP4]:
        folder.mkdir(parents=True, exist_ok=True)

def print_header():
    os.system("cls" if os.name == "nt" else "clear")
    print("="*60)
    print("             🎬 yt-dlp 多功能下載控制台 (中文介面)")
    print("         作者：Firefox_0304 版本 v5.1  協助Bot：ChatGPT")
    print("="*60)

def check_shortcut():
    print_header()
    if platform.system() != "Windows":
        print("⚠️ 非 Windows 系統，捷徑功能已自動跳過。")
        return

    desktop = Path(os.path.join(os.path.expanduser("~"), "Desktop"))
    shortcut_path = desktop / SHORTCUT_NAME
    if NEVER_REMIND_FILE.exists():
        return

    if not shortcut_path.exists():
        while True:
            choice = input("系統偵測到桌面沒有捷徑，是否新增一個捷徑? (Y/N/E): ").strip().upper()
            if choice == "Y":
                create_shortcut(shortcut_path)
                input("✅ 捷徑建立完成，按任意鍵進入主程式…")
                break
            elif choice == "N":
                print("❎ 已取消建立捷徑")
                input("按任意鍵進入主程式…")
                break
            elif choice == "E":
                CONFIG_FOLDER.mkdir(parents=True, exist_ok=True)
                NEVER_REMIND_FILE.touch()
                print("🛑 系統將不再提醒建立捷徑")
                input("按任意鍵進入主程式…")
                break
            else:
                print("⚠️ 請輸入 Y/N/E")

def create_shortcut(path):
    if winshell is None:
        ans = input("⚠️ winshell 模組未安裝，是否立即安裝? (Y/N): ").strip().upper()
        if ans == "Y":
            subprocess.run([sys.executable, "-m", "pip", "install", "winshell", "pywin32"])
            print("✅ 安裝完成")
        else:
            print("⚠️ 無法建立捷徑，跳過…")
            return
    try:
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(str(path))

        # 分辨 Python 模式 vs EXE 模式
        if getattr(sys, 'frozen', False):
            # 打包成 EXE 時
            shortcut.Targetpath = sys.executable
            shortcut.Arguments = ""
        else:
            # 開發時（.py 模式）
            shortcut.Targetpath = str(sys.executable)
            shortcut.Arguments = f'"{Path(__file__).resolve()}"'

        shortcut.WorkingDirectory = str(Path(__file__).parent)
        shortcut.IconLocation = str(sys.executable)
        shortcut.save()
    except Exception as e:
        print(f"⚠️ 建立捷徑失敗: {e}")

def list_folders():
    ensure_folders()
    folders = [f.name for f in BASE_FOLDER.iterdir() if f.is_dir() and f.name != "config"]
    print("目前資料夾:")
    for idx, f in enumerate(folders, start=1):
        print(f" {idx}. {f}")
    return folders

def select_folder():
    while True:
        print_header()
        print("📂 儲存位置設定")
        print("1. 查看現有資料夾")
        print("2. 建立新資料夾")
        print("3. 不建立資料夾 - 預設目錄")
        print("4. 退回上一頁")
        print("5. 刪除資料夾")
        choice = input("請輸入選項 [1-5]: ").strip()
        if choice == "1":
            folders = list_folders()
            selection = input("輸入資料夾編號選擇，空白返回上一頁: ").strip()
            if selection == "":
                continue
            try:
                idx = int(selection) - 1
                if 0 <= idx < len(folders):
                    return BASE_FOLDER / folders[idx]
            except:
                input("⚠️ 無效選項，按任意鍵繼續…")
        elif choice == "2":
            new_name = input("請輸入新資料夾名稱 (空白返回): ").strip()
            if new_name == "":
                continue
            new_folder = BASE_FOLDER / new_name
            new_folder.mkdir(parents=True, exist_ok=True)
            (new_folder / "MP3").mkdir(exist_ok=True)
            (new_folder / "MP4").mkdir(exist_ok=True)
            return new_folder
        elif choice == "3":
            return DEFAULT_FOLDER
        elif choice == "4":
            return None
        elif choice == "5":
            delete_folder()
        else:
            input("⚠️ 無效選項，按任意鍵繼續…")

def delete_folder():
    folders = list_folders()
    if not folders:
        input("⚠️ 沒有可刪除的資料夾，按任意鍵返回…")
        return
    selection = input("輸入要刪除的資料夾編號 (空白返回): ").strip()
    if selection == "":
        return
    try:
        idx = int(selection) - 1
        if 0 <= idx < len(folders):
            folder_to_delete = BASE_FOLDER / folders[idx]
            confirm = input(f"⚠️ 確定要刪除資料夾 '{folders[idx]}' 及其內容嗎? (Y/N): ").strip().upper()
            if confirm == "Y":
                shutil.rmtree(folder_to_delete)
                print(f"✅ 已刪除資料夾 '{folders[idx]}'")
                input("按任意鍵返回…")
    except:
        input("⚠️ 無效選項，按任意鍵繼續…")

def start_download(url, folder, media_type):
    target_folder = folder / media_type
    target_folder.mkdir(exist_ok=True)
    print("下載中請稍後…")
    cmd = [
        "yt-dlp",
        "-o", str(target_folder / "%(title)s.%(ext)s"),
        "--progress-template", "[{bar:40}] {percent:.1f}% {speed} {eta}",
        url
    ]
    subprocess.run(cmd)

def download(media_type):
    url = input("請輸入影片或播放清單網址: ").strip()
    if url == "":
        return
    folder = select_folder()
    if folder is None:
        return
    start = input("是否開始下載? (Y/N): ").strip().upper()
    if start != "Y":
        return
    start_download(url, folder, media_type)
    input("✅ 下載完成，按任意鍵返回主選單…")

def main_menu():
    ensure_folders()
    check_shortcut()
    while True:
        print_header()
        print("1. 下載音樂 (MP3)")
        print("2. 下載影片 (MP4)")
        print("3. 刪除資料夾")
        print("4. 離開")
        choice = input("請輸入選項 [1-4]: ").strip()
        if choice == "1":
            download("MP3")
        elif choice == "2":
            download("MP4")
        elif choice == "3":
            delete_folder()
        elif choice == "4":
            sys.exit(0)
        else:
            input("⚠️ 無效選項，按任意鍵繼續…")

if __name__ == "__main__":
    main_menu()
