from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Static file
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# Login Page
@app.get("/", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


# Dashboard
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard_get(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})


@app.post("/dashboard", response_class=HTMLResponse)
def dashboard_post(request: Request, phone: str = Form(...)):
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "phone": phone
    })


# Menu Makanan
@app.get("/menu-makanan", response_class=HTMLResponse)
def menu_makanan(request: Request):
    return templates.TemplateResponse("menu-makanan.html", {"request": request})


# Menu Booking Form
@app.get("/menu-form", response_class=HTMLResponse)
def menu_booking(request: Request, seat: str = None):
    return templates.TemplateResponse("menu-booking-form.html", {
        "request": request,
        "seat": seat
    })


# Halaman pilih kursi
@app.get("/menu-seats", response_class=HTMLResponse)
def menu_seats(request: Request):
    return templates.TemplateResponse("booking-chose-seat.html", {
        "request": request,
        "reserved_seats": reserved_seats
    })

# Booking history storage
menu_history = []

reserved_seats = set()

# Booking Submit
@app.post("/booking-submit", response_class=HTMLResponse)
def booking_submit(
    request: Request,
    seat: str = Form(...),
    nama: str = Form(...),
    tanggal: str = Form(...),
    jam: str = Form(...),
    jumlah_orang: int = Form(...)
):
    if seat in reserved_seats:
        return templates.TemplateResponse("booking-failed.html", {
            "request": request,
            "message": f"Kursi {seat} sudah dipesan! Silakan pilih kursi lain."
        })

    menu_history.append({
        "seat": seat,
        "nama": nama,
        "tanggal": tanggal,
        "jam": jam,
        "jumlah": jumlah_orang
    })

    reserved_seats.add(seat)

    return templates.TemplateResponse("booking-success.html", {
        "request": request,
        "seat": seat,
        "nama": nama,
        "tanggal": tanggal,
        "jam": jam,
        "jumlah": jumlah_orang
    })
# Menu History
@app.get("/menu-history", response_class=HTMLResponse)
def menu_history_page(request: Request):
    return templates.TemplateResponse("menu-history.html", {
        "request": request,
        "history": menu_history
    })
