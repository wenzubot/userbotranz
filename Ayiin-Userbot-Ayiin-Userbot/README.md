<h1 align="center">
  <img src="assets/flamepurple.gif" width="40" /> RANZ USERBOT <img src="assets/flamepurple.gif" width="40" />
</h1>

<p align="center">
  <a href="https://github.com/wenzubot/userbotranz/commits">
    <img src="https://img.shields.io/github/last-commit/wenzubot/userbotranz?color=red&logo=github&logoColor=blue&style=for-the-badge" />
  </a>
</p>

<p align="center">
  <a href="https://github.com/wenzubot/userbotranz">
    <img src="https://badges.frapsoft.com/os/v2/open-source.png?v=103" width="120" />
  </a>
  <a href="https://github.com/wenzubot/userbotranz/graphs/commit-activity">
    <img src="https://img.shields.io/badge/Maintained%3F-Yes-blue" width="120" />
  </a>
  <a href="https://app.codacy.com/gh/wenzubot/userbotranz/dashboard">
    <img src="https://img.shields.io/codacy/grade/a723cb464d5a4d25be3152b5d71de82d?color=blue&logo=codacy" width="120" />
  </a>
</p>

<p align="center">
  <a href="https://github.com/wenzubot/userbotranz/fork">
    <img src="https://img.shields.io/github/forks/wenzubot/userbotranz?&logo=github" width="100" />
  </a>
  <a href="https://github.com/wenzubot/userbotranz/stargazers">
    <img src="https://img.shields.io/github/stars/wenzubot/userbotranz?&logo=github" width="100" />
  </a>
</p>

<p align="center">
  <img src="assets/logo.jpg" />
</p>

<h3 align="center">
  👩‍💻 Ranzneweraa-Userbot adalah userbot Telegram modular yang berjalan di Python3 dengan database sqlalchemy.
</h3>

Berbasis [Paperplane](https://github.com/RaphielGang/Telegram-UserBot) dan [ProjectBish](https://github.com/adekmaulana/ProjectBish) userbot.  
Repository ini dibuat untuk memilih dan menambahkan modul sesuai kebutuhan dengan banyak perubahan dan fitur baru.

---

## Disclaimer

Saya tidak bertanggung jawab atas penyalahgunaan bot ini. Bot ini dimaksudkan untuk bersenang-senang sekaligus membantu anda mengelola grup secara efisien dan mengotomatiskan beberapa hal yang membosankan. Gunakan bot ini dengan risiko Anda sendiri, dan gunakan userbot ini dengan bijak.

---

<details>
<summary><b>🔗 String Session</b></summary>
<br>

> Anda memerlukan API_ID & API_HASH untuk menghasilkan sesi telethon. Ambil APP ID dan API Hash di [my.telegram.org](https://my.telegram.org)

### Generate Session via Repl
<p>
<a href="https://repl.it/@AyiinXd/AyiinString?lite=1&outputonly=1">
  <img src="https://img.shields.io/badge/Generate%20On%20Repl-blueviolet?style=for-the-badge&logo=appveyor" width="200" />
</a>
</p>

### Generate Session via Telegram StringGen Bot
<p>
<a href="https://t.me/GeneratorStringRobot">
  <img src="https://img.shields.io/badge/TG%20String%20Gen%20Bot-blueviolet?style=for-the-badge&logo=appveyor" width="200" />
</a>
</p>

</details>

<details>
<summary><b>🔗 Deploy di VPS</b></summary>
<br>

### Tutorial Deploy di VPS

```bash
git clone https://github.com/wenzubot/userbotranz
cd userbotranz
pip3 install -U -r requirements.txt
mv sample.env .env
nano .env
# isi vars, ctrl+S lalu ctrl+X
screen -S userbotranz
bash start