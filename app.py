from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
<html>
<head>
<meta charset="UTF-8">
<title>Nkateko Caring</title>
<style>
body{font-family:Arial;margin:0;background:#f8f9fa}
.header{background:#c2185b;color:white;padding:20px;text-align:center}
.hero{background:#c2185b;color:white;padding:30px;text-align:center}
.btn{background:white;color:#c2185b;padding:12px 25px;border-radius:30px;text-decoration:none;font-weight:bold;margin:5px;display:inline-block}
.card{background:white;padding:15px;margin:10px auto;max-width:900px;border-radius:10px}
.contact{background:#c2185b;color:white;padding:30px;text-align:center}
</style>
</head>
<body>
<div class="header">
<h1>Nkateko Caring at Your Own Home</h1>
<p>Trusted Caregivers</p>
</div>
<div class="hero">
<h2>LIVE - All 9 Provinces!</h2>
<p>Boksburg, Limpopo, Gauteng & All SA</p>
<p>Elderly | Frail | Disability | Dementia | 24/7</p>
<br>
<a class="btn" href="tel:0737938724">073 793 8724</a>
<a class="btn" href="https://wa.me/27737938724" style="background:#25D366;color:white">WhatsApp</a>
<p>www.nkatekocaring.co.za</p>
</div>
<div class="card">
<h3>Services</h3>
<p>Elderly, Frail, Disability, Dementia, Palliative, Live-in/out</p>
</div>
<div class="card">
<h3>All 9 Provinces</h3>
<p>Gauteng: Boksburg, Johannesburg, Pretoria</p>
<p>Limpopo: Polokwane, Thulamhashe, Giyani, Tzaneen, Lephalale, Nkowankowa</p>
<p>All: Limpopo, Gauteng, Mpumalanga, North West, Free State, KZN, Eastern, Western, Northern Cape</p>
</div>
<div class="contact">
<h2>Contact Nkateko!</h2>
<p style="font-size:24px"><b>073 793 8724</b></p>
<p>www.nkatekocaring.co.za</p>
<p>molletnkateko@gmail.com</p>
<br>
<a class="btn" href="https://wa.me/27737938724" style="background:#25D366;color:white">WhatsApp Now</a>
</div>
</body>
</html>
'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
