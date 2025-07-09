# 🚦 MiniNMS - Lightweight Network Monitoring Tool

**MiniNMS** is a lightweight, Python-based tool designed for monitoring network devices using basic **ping** and **SNMP** queries. Ideal for small to mid-size networks where simplicity and visibility matter the most.

---

## 📸 Preview (Coming Soon)


---

## ⚙️ Features

- ✅ Periodic device availability check (via `ping`)
- ✅ SNMP-based `sysUpTime` retrieval
- ✅ Outputs results to a readable `JSON` format
- ✅ Simple `devices.json` configuration file

---

## 📁 Project Structure

```
mini-nms/
├── monitor.py # Main monitoring script
├── config/
│ └── devices.json # Device list and SNMP settings
├── monitoring_output.json # Output status
└── README.md # This file


```

## 🚀 Getting Started

### 1. Clone the repo


git clone https://github.com/your-username/mini-nms.git
cd mini-nms

### 2. Install dependencies
pip install pysnmp


### 3. Create your device config
```
[
  {
    "name": "Switch01",
    "ip": "192.168.1.1",
    "community": "public"
  },
  {
    "name": "Router01",
    "ip": "192.168.1.254",
    "community": "public"
  }
]
```



Save the file to config/devices.json.

### 4. Run the monitor
```
python monitor.py
```


##  Output Example
```
[
  {
    "name": "Switch01",
    "ip": "192.168.1.1",
    "status": true,
    "uptime": "12345678"
  }
]
```




# MiniNMS - مانیتورینگ سبک برای شبکه‌های کوچک تا متوسط

MiniNMS یک ابزار ساده و سبک برای مانیتور کردن وضعیت دستگاه‌های شبکه (Ping و SNMP) است که برای شبکه‌های کوچک و متوسط طراحی شده. این پروژه به شما اجازه می‌دهد وضعیت دسترسی و uptime تجهیزات شبکه را از طریق یک فایل کانفیگ ساده بررسی و مانیتور کنید.

## ✨ امکانات فعلی:
- بررسی دسترسی دستگاه‌ها از طریق ping
- دریافت `sysUpTime` از طریق SNMP
- ذخیره‌سازی خروجی در قالب JSON برای استفاده در سیستم‌های دیگر یا رابط‌های گرافیکی

## 📁 ساختار پروژه
```
mini-nms/
├── monitor.py              # اسکریپت اصلی مانیتورینگ
├── config/
│   └── devices.json        # فایل کانفیگ لیست دستگاه‌ها
├── monitoring_output.json  # خروجی وضعیت دستگاه‌ها
└── README.md               # همین فایل
```

## ⚙️ نحوه استفاده:
1. مخزن را کلون کنید:
```bash
git clone https://github.com/yourusername/mini-nms.git
cd mini-nms
```

2. فایل `devices.json` را طبق قالب زیر بسازید:
```json
[
  {
    "name": "Switch01",
    "ip": "192.168.1.1",
    "community": "public"
  },
  {
    "name": "Router01",
    "ip": "192.168.1.254",
    "community": "public"
  }
]
```

3. اجرای مانیتور:
```bash
python monitor.py
```

## 🐍 پیش‌نیازها:
- Python 3.8+
- پکیج `pysnmp`

نصب پکیج:
```bash
pip install pysnmp
```

## 🔜 برنامه‌های آینده:
- رابط گرافیکی تحت وب (Flask / React)
- هشدارهای تلگرامی / ایمیل
- پشتیبانی از SNMPv3
- مانیتورینگ میزان پهنای باند

---

🤝 خوشحال می‌شیم اگر پیشنهادی برای بهبود پروژه دارید یا Pull Request بزنید!

#شبکه #پایتون #SNMP #Monitoring #NetworkTools
