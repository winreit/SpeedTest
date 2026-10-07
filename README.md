1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/winreit/SpeedTest
   ```

2. Создайте виртуальное окружение и активируйте его:
  
   Для macOS/Linux
   ```bash
   python3 -m venv venv
   source venv/bin/activate 
   ```
   Для Windows
   ```bash
   python -m venv myenv
   myenv\Scripts\activate
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Запуск проекта (так же можно использовать свою ссылку):
   ```bash
   python SpeedTest.py "https://downloader.disk.yandex.ru/disk/63403d3f3896065cf31b23c9044d7b332e94ec8bd103af866b9145dd3dd2fd01/6ac6db33/g6dcFBPLNdRgjkVf0XZ7jENGI17wceWfklg2gi4ky8u6EqPnUBuhmyrIwFFSnQIsZBtZJM67omEoGojcEwA3EA%3D%3D?uid=0&filename=potm2506a.jpg&disposition=attachment&hash=vgoXIC297kpfkWDUg78wiJt9W6z5mXmIOAy%2BVHQR2X2StTJupHtrwlEaT/ICXjDFq/J6bpmRyOJonT3VoXnDag%3D%3D%3A&limit=0&content_type=image%2Fjpeg&owner_uid=981591956&fsize=19499486&hid=1af7dae277c9f59f79502e810563d822&media_type=image&tknv=v3&is_direct_zip_experiment=1" 
   ```
