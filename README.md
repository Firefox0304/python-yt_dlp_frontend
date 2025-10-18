🎬 yt-dlp 多功能下載控制台 (中文介面) 使用說明書(Python) v5.1

第1部分：安裝流程 & 常見 Q&A

1️⃣ 解壓縮與準備
C:\
 └─ Users
     └─ 使用者名
         └─ Public
             └─ Desktop
                 └─ python_yt_dlp_frontend
                     ├─ yt_dlp_frontend.py
                     ├─ requirements.txt
                     └─ 其他附檔
步驟說明：

1.下載壓縮檔後解壓縮到桌面，路徑建議如上圖所示。
2.確認電腦已安裝 Python 3.10+ 並加入系統 PATH。
3.開啟 CMD(［Win］+［R］輸入cmd) / PowerShell(［Win］+［R］輸入PowerShell)，切換到資料夾：
輸入：cd "C:\Users\使用者名\Public\Desktop\python_yt_dlp_frontend"
4.安裝必要套件：
輸入：pip install -r requirements.txt
5.確認 yt-dlp 可以執行：
輸入：yt-dlp --version


2️⃣ 常見問題 Q&A

| 問題                                 | 解法                                        |
| ------------------------------------ | ------------------------------------------- |
| 執行 `python yt_dlp_frontend.py` 閃退 | 確認路徑正確且 yt-dlp 可執行                 |
| 字元亂碼                              | CMD 編碼請設為 `chcp 65001`                 |
| 下載資料夾不存在                       | 程式會自動建立預設資料夾與 MP3/MP4 子資料夾   |
| 想刪除資料夾                           | 主選單 → 3. 刪除資料夾，選擇資料夾後確認即可  |
| 下載播放清單限制                       | yt-dlp 本身受 YouTube 限制，請分批下載       |


第2部分：使用說明

============================================================
             🎬 yt-dlp 多功能下載控制台 (中文介面)
             作者：郭子睿 版本 v5.1  協助Bot：ChatGPT
============================================================
1. 下載音樂 (MP3)
2. 下載影片 (MP4)
3. 刪除資料夾
4. 離開
請輸入選項 [1-4]:

說明：

選擇 1 → 下載 MP3

選擇 2 → 下載 MP4

選擇 3 → 刪除自訂資料夾

選擇 4 → 離開程式

［本次新增功能］

1️⃣新增多頻台可執行功能
1.本包內包含了其他平台的Python下載包，除了Linux
2.MAC OS用戶 & Linux用戶使用到的是閹割版，但主要下載功能都還在
3.Linux(Ubuntu / Debian 系列)用戶需要在Terminal安裝最新 Python 3
檢查版本：
python3 --version
pip3 --version
4.Fedora / CentOS / RHEL用戶：
sudo dnf install python3 python3-pip -y
CentOS 7：
sudo yum install python3 python3-pip -y
5.Arch Linux / Manjaro用戶：
sudo pacman -S python python-pip
4.修復了在程式內的新增連結BUG

2️⃣從官方源碼編譯（適用於任何 Linux 發行版）
1.下載 Python 官方壓縮包（Gzipped 或 XZ）：
wget https://www.python.org/ftp/python/3.13.9/Python-3.13.9.tgz
tar -xvzf Python-3.13.9.tgz
cd Python-3.13.9
2.編譯安裝：
./configure --enable-optimizations
make -j$(nproc)
sudo make altinstall
3.驗證：
python3.13 --version
pip3.13 --version


如有任何問題請與作者聯繫

🎬 yt-dlp 多功能下載控制台 (中文介面) 使用說明書(exe) v5.1


第1部分：安裝流程 & 常見 Q&A

1️⃣ 解壓縮與準備
C:\
 └─ Users
     └─ 使用者名
         └─ Public
             └─ Desktop
                 └─ python_yt_dlp_frontend
                     ├─ python-yt_dlp_frontend-V5.1
                     ├─ python yt_dlp_frontend說明書-V5.1.txt
                     └─ 其他附檔
步驟說明：

1.下載壓縮檔後解壓縮到桌面，路徑建議如上圖所示。

              ［本次新增功能］

1️⃣新增多頻台可執行功能
1.本包內包含了其他平台的Python下載包，除了Linux
2.MAC OS用戶 & Linux用戶使用到的是閹割版，但主要下載功能都還在
3.Linux(Ubuntu / Debian 系列)用戶需要在Terminal安裝最新 Python 3
檢查版本：
python3 --version
pip3 --version
4.Fedora / CentOS / RHEL用戶：
sudo dnf install python3 python3-pip -y
CentOS 7：
sudo yum install python3 python3-pip -y
5.Arch Linux / Manjaro用戶：
sudo pacman -S python python-pip
4.修復了在程式內的新增連結BUG

2️⃣從官方源碼編譯（適用於任何 Linux 發行版）
1.下載 Python 官方壓縮包（Gzipped 或 XZ）：
wget https://www.python.org/ftp/python/3.13.9/Python-3.13.9.tgz
tar -xvzf Python-3.13.9.tgz
cd Python-3.13.9
2.編譯安裝：
./configure --enable-optimizations
make -j$(nproc)
sudo make altinstall
3.驗證：
python3.13 --version
pip3.13 --version


如有任何問題請與作者聯繫
