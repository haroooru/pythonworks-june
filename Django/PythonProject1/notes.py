# django 2

# ==============================
# Django Request-Response Notes
# ==============================

# Client (Browser) -----> Server (Django)
#        HttpRequest
# ------------------------------
# URL: http://127.0.0.1:8000/
# ------------------------------
# Server view:
# def home(request):
#     return HttpResponse("Welcome to Django")
# ------------------------------
# Browser output:
# Welcome to Django
# ------------------------------
# Flow:
# Browser sends request --> Django view returns response --> Browser shows text

# ------------------------------
# URL: http://127.0.0.1:8000/index/
# ------------------------------
# Server view:
# def index(request):
#     return HttpResponse("Index Page")
# ------------------------------
# Browser output:
# Index Page
# ------------------------------
# Flow:
# Browser sends request --> Django view returns response --> Browser shows text

# ==============================
# Summary:
# - Each URL maps to a view function
# - View returns HttpResponse
# - Browser displays that response
# ==============================
