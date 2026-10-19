from flask import Flask

app = Flask(__name__)

# الصفحة الرئيسية - البطاقة الشخصية
@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>بطاقتي الشخصية</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
            body { background: linear-gradient(135deg, #0f172a, #1e293b); min-height: 100vh; display: flex; justify-content: center; align-items: center; color: #fff; }
            .card { background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 35px; width: 350px; text-align: center; box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5); }
            .profile-img { width: 110px; height: 110px; border-radius: 50%; border: 3px solid #38bdf8; margin-bottom: 15px; }
            h1 { font-size: 22px; margin-bottom: 5px; }
            p.title { color: #38bdf8; font-size: 14px; margin-bottom: 15px; }
            p.bio { color: #94a3b8; font-size: 13px; line-height: 1.6; margin-bottom: 25px; }
            .btn { display: block; width: 100%; padding: 12px; background: linear-gradient(45deg, #38bdf8, #6366f1); color: #fff; text-decoration: none; border-radius: 25px; font-weight: bold; transition: 0.3s; margin-bottom: 10px; }
            .btn-telegram { background: #229ED9; }
            .btn:hover { opacity: 0.9; transform: translateY(-2px); }
        </style>
    </head>
    <body>
        <div class="card">
            <img src="https://via.placeholder.com/150" alt="صورة شخصية" class="profile-img">
            <h1>محمد</h1>
            <p class="title">مطور ويب وسيرفرات بايثون 🚀</p>
            <p class="bio">أهلاً بك في موقعي الديناميكي المدار بسيرفر Python (Flask)!</p>
            <a href="/contact" class="btn">✉️ تواصل معي</a>
            <a href="https://t.me/your_telegram_username" target="_blank" class="btn btn-telegram">✈️ تلجرام</a>
        </div>
    </body>
    </html>
    """

# صفحة التواصل
@app.route("/contact")
def contact():
    return """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>تواصل معي</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
            body { background: linear-gradient(135deg, #0f172a, #1e293b); min-height: 100vh; display: flex; justify-content: center; align-items: center; color: #fff; }
            .contact-card { background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 35px; width: 380px; box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5); }
            h2 { font-size: 22px; margin-bottom: 20px; text-align: center; color: #38bdf8; }
            .form-group { margin-bottom: 15px; }
            label { display: block; margin-bottom: 6px; color: #94a3b8; font-size: 14px; }
            input, textarea { width: 100%; padding: 12px; background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.15); border-radius: 10px; color: #fff; outline: none; font-size: 14px; }
            textarea { resize: none; height: 100px; }
            .btn-submit { width: 100%; padding: 12px; background: linear-gradient(45deg, #38bdf8, #6366f1); color: #fff; border: none; border-radius: 25px; font-weight: bold; cursor: pointer; font-size: 15px; margin-top: 10px; }
            .back-link { display: block; text-align: center; margin-top: 15px; color: #94a3b8; text-decoration: none; font-size: 13px; }
        </style>
    </head>
    <body>
        <div class="contact-card">
            <h2>أرسل لي رسالة ✉️</h2>
            <form action="https://formspree.io/f/mqpejjbb" method="POST">
                <div class="form-group">
                    <label>الاسم الكامل:</label>
                    <input type="text" name="name" placeholder="اكتب اسمك هنا..." required>
                </div>
                <div class="form-group">
                    <label>البريد الإلكتروني:</label>
                    <input type="email" name="email" placeholder="example@mail.com" required>
                </div>
                <div class="form-group">
                    <label>الرسالة:</label>
                    <textarea name="message" placeholder="اكتب نص رسالتك هنا..." required></textarea>
                </div>
                <button type="submit" class="btn-submit">إرسال الرسالة</button>
            </form>
            <a href="/" class="back-link">← العودة للبطاقة الشخصية</a>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)