from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Static file (css/js/img)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# Halaman login
@app.get("/", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


# Halaman dashboard setelah login
@app.post("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request, phone: str = Form(...)):
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "phone": phone
    })


#Isi Dashboard

# Menu Makanan
@app.get("/menu makanan", response_class=HTMLResponse)
def menu_makanan(request: Request):
    return templates.TemplateResponse("menu-makanan.html",{"request": request})

# Menu Booking
@app.get("/menu booking", response_class=HTMLResponse)
def menu_booking(request: Request):
    return templates.TemplateResponse("menu-booking.html",{"request": request})

# Menyimpan data booking
@app.post("/booking-submit", response_class=HTMLResponse)
def booking_submit(
    request: Request,
    nama: str = Form(...),
    tanggal: str = Form(...),
    jam: str = Form(...),
    jumlah_orang: int = Form(...)
):

    # simpan ke history
    menu_history.append({
        "nama": nama,
        "tanggal": tanggal,
        "jam": jam,
        "jumlah": jumlah_orang
    })

    return templates.TemplateResponse("booking-success.html", {
        "request": request,
        "nama": nama,
        "tanggal": tanggal,
        "jam": jam,
        "jumlah": jumlah_orang
    })



#Menu History
@app.get("/menu-history", response_class=HTMLResponse)
def menu_history(request: Request):
    return templates.TemplateResponse("menu-history.html", {
        "request": request,
        "history": menu_history
    })