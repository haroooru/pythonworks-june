# ============================================================
# DJANGO REST FRAMEWORK (DRF) - BEGINNER NOTES
# ============================================================
#
# API
# ---
# API = Application Programming Interface.
# It is a method that enables communication between different applications.
#
# Example:
# A mobile app requests student data from our Django server.
# Mobile App -> API request -> Django/DRF -> API response -> Mobile App
#
#
# JSON
# ----
# JSON = JavaScript Object Notation.
# JSON is a commonly used data format for APIs.
#
# Example:
# {
#     "name": "Hari",
#     "age": 24
# }
#
#
# REST
# ----
# REST = Representational State Transfer.
# REST is an architectural style / set of guidelines commonly used
# for designing Web APIs.
#
# Common HTTP methods:
# GET     -> read/retrieve data
# POST    -> create new data
# PUT     -> update/replace data
# PATCH   -> partially update data
# DELETE  -> delete data
#
#
# DRF
# ---
# DRF = Django REST Framework.
#
# DRF is NOT a replacement for Django and is not simply an
# "advanced version of Django".
#
# DRF is a framework/toolkit built on Django that makes it easier
# to create Web APIs.
#
# ============================================================
# 1. DJANGO vs DRF
# ============================================================
#
# DJANGO provides:
# - Admin panel
# - URL-to-view mapping
# - ORM
# - MVT architecture
# - Form handling
# - Template engine
#
# DRF adds API-focused tools such as:
# - APIView
# - Serializers
# - ModelSerializer
# - Response
# - Authentication
# - Permissions
#
#
# Easy idea:
#
# Django = general Python web framework
# DRF    = tools built on Django for creating APIs
#
#
# ============================================================
# 2. ENVIRONMENT SETUP
# ============================================================
#
# We need:
# - Python
# - Django
# - Django REST Framework
#
# Optional:
# - Virtual environment
#
# Install Django:
#
#     pip install django
#
# Install DRF:
#
#     pip install djangorestframework
#
# Virtual environment:
# A virtual environment keeps packages for one project separate
# from packages used by other projects.
#
#
# ============================================================
# 3. DJANGO CONCEPTS WE ALREADY KNOW
# ============================================================
#
# Admin panel
#     -> Interface for managing database data.
#
# URL-to-view mapping
#     -> Connects a URL to the view that handles the request.
#
# ORM
#     -> Object Relational Mapper.
#     -> Lets us work with database tables using Python models.
#
# MVT architecture
#     -> Model    = data/database
#     -> View     = logic
#     -> Template = presentation/UI
#
# Form handling
#     -> Helps create/process HTML forms.
#
# Template engine
#     -> Used to generate dynamic HTML pages.
#
#
# ============================================================
# 4. MAIN DRF COMPONENTS
# ============================================================
#
# APIView
#     -> DRF class used to create API views/endpoints.
#
# Serializer
#     -> Converts and validates data for API use.
#
# ModelSerializer
#     -> Serializer designed to work with Django models.
#
# Response
#     -> Used to return API response data to the client.
#
# Authentication
#     -> Identifies WHO is making the request.
#
# Permissions
#     -> Decides WHAT the user is allowed to access/do.
#
#
# ============================================================
# 5. APIView
# ============================================================
#
# APIView is a DRF class used to create API endpoints.
#
# Example:
#
# from rest_framework.views import APIView
# from rest_framework.response import Response
#
#
# class HelloWorld(APIView):
#     def get(self, request):
#         return Response({"message": "Hello World"})
#
#
# Explanation:
#
# class HelloWorld(APIView)
#     -> creates an API view using DRF.
#
# def get(self, request)
#     -> handles a GET request.
#
# Response(...)
#     -> sends data back to the client.
#
#
# ============================================================
# 6. RESPONSE
# ============================================================
#
# DRF provides:
#
#     from rest_framework.response import Response
#
# Example:
#
#     return Response({
#         "message": "Good Morning"
#     })
#
# The client receives structured API data.
#
#
# ============================================================
# 7. SERIALIZER
# ============================================================
#
# Serializer is one of the most important concepts in DRF.
#
# It helps convert complex data such as Django model objects
# into data that can be returned by an API, commonly as JSON.
#
# It also validates incoming API data.
#
# Simple idea:
#
# DATABASE / MODEL DATA
#          |
#          v
#      SERIALIZER
#          |
#          v
#       API / JSON
#
# For incoming data:
#
# API / JSON
#     |
#     v
# SERIALIZER
#     |
#     v
# VALIDATED DATA
#     |
#     v
# DATABASE
#
#
# ============================================================
# 8. ModelSerializer
# ============================================================
#
# ModelSerializer is a special serializer used with Django models.
#
# Example model:
#
# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#
# A ModelSerializer can use this model and automatically create
# serializer fields based on the model.
#
# Easy difference:
#
# Serializer
#     -> We generally define fields ourselves.
#
# ModelSerializer
#     -> Fields can be generated from a Django model.
#
#
# ============================================================
# 9. AUTHENTICATION
# ============================================================
#
# Authentication answers:
#
#     "WHO are you?"
#
# It identifies the user/client making the request.
#
# Examples:
#
# BasicAuthentication
#     -> Uses username/password-based authentication.
#
# TokenAuthentication
#     -> Uses a token sent with the request to identify the user.
#
# IMPORTANT:
# Authentication and Permission are different.
#
# Authentication = WHO are you?
# Permission     = WHAT are you allowed to do?
#
#
# ============================================================
# 10. PERMISSIONS
# ============================================================
#
# Permissions control access to an API/view.
#
# Examples:
#
# AllowAny
#     -> Anyone can access the view.
#
# IsAuthenticated
#     -> User must be authenticated.
#
# IsAdminUser
#     -> User must have the required admin/staff privileges.
#
#
# Memory trick:
#
# Authentication -> WHO?
# Permission     -> ALLOWED TO DO WHAT?
#
#
# ============================================================
# 11. HTTP METHODS
# ============================================================
#
# GET
#     -> Retrieve/read data.
#
# POST
#     -> Create/send new data.
#
# PUT
#     -> Update/replace an existing resource.
#
# PATCH
#     -> Partially update an existing resource.
#
# DELETE
#     -> Delete data.
#
#
# ============================================================
# 12. URL -> APIView CONNECTION
# ============================================================
#
# Example:
#
# from django.urls import path
# from .views import HelloWorld
#
# urlpatterns = [
#     path("hello/", HelloWorld.as_view()),
# ]
#
# If the client requests:
#
#     /hello/
#
# Django finds HelloWorld.as_view().
#
# Then the HTTP method determines which method inside APIView runs:
#
# GET     -> get()
# POST    -> post()
# PUT     -> put()
# PATCH   -> patch()
# DELETE  -> delete()
#
#
# ============================================================
# 13. SIMPLE API EXAMPLE
# ============================================================
#
# from rest_framework.views import APIView
# from rest_framework.response import Response
#
#
# class GoodMorning(APIView):
#     def get(self, request):
#         return Response({
#             "message": "Good Morning"
#         })
#
#
# URL:
#
# path("morning/", GoodMorning.as_view())
#
#
# Request:
#
#     GET /morning/
#
#
# Response:
#
#     {
#         "message": "Good Morning"
#     }
#
#
# ============================================================
# 14. COMPLETE DRF REQUEST FLOW
# ============================================================
#
#                         CLIENT
#                            |
#                            | HTTP REQUEST
#                            v
#                           URL
#                            |
#                            v
#                         APIView
#                            |
#                 +----------+----------+
#                 |                     |
#                 v                     v
#          Authentication        Permissions
#                 |                     |
#                 +----------+----------+
#                            |
#                            v
#                       Serializer
#                            |
#                            v
#                     Model / Database
#                            |
#                            v
#                         Response
#                            |
#                            | JSON/API DATA
#                            v
#                          CLIENT
#
#
# ============================================================
# 15. CLASS DIAGRAM FROM THE LECTURE - SIMPLIFIED
# ============================================================
#
#                     Django REST Framework
#                              |
#       +----------------------+----------------------+
#       |                      |                      |
#       v                      v                      v
# Authentication           Responses                Views
#       |                      |                      |
#   +---+---+                  v                      v
#   |       |               Response                APIView
#   v       v
# Basic   Token
# Auth    Auth
#
# DRF also provides:
#
#                         Permissions
#                              |
#               +--------------+--------------+
#               |              |              |
#               v              v              v
#           AllowAny    IsAuthenticated   IsAdminUser
#
# And for data:
#
#                     Serializer
#                         |
#                         v
#                   ModelSerializer
#
#
# ============================================================
# 16. BEGINNER ANALOGY
# ============================================================
#
# Imagine an API like a restaurant:
#
# CLIENT
#     = Customer
#
# URL
#     = Correct restaurant counter/entrance
#
# APIView
#     = Person handling the order
#
# Authentication
#     = Checking who the customer is
#
# Permission
#     = Checking what the customer is allowed to order
#
# Model / Database
#     = Restaurant's stored information
#
# Serializer
#     = Converts/validates the information into a form suitable
#       for the API.
#
# Response
#     = The final data/order sent back to the customer.
#
#
# ============================================================
# 17. ONE-LINE EXAM DEFINITIONS
# ============================================================
#
# API:
# Application Programming Interface; a method that enables
# communication between different applications.
#
# JSON:
# JavaScript Object Notation; a commonly used data format for APIs.
#
# REST:
# Representational State Transfer; an architectural style/
# guidelines commonly used for designing Web APIs.
#
# DRF:
# Django REST Framework; a framework/toolkit built on Django
# for developing Web APIs.
#
# APIView:
# A DRF class used to create API views/endpoints.
#
# Serializer:
# A component that converts and validates data for API use.
#
# ModelSerializer:
# A serializer designed to work with Django models and generate
# fields from the model.
#
# Authentication:
# Identifies who is making the request.
#
# Permission:
# Determines whether a user is allowed to access/perform something.
#
# Response:
# A DRF class used to return API response data to the client.
#
#
# ============================================================
# 18. WHAT WE WILL BUILD IN PYCHARM
# ============================================================
#
# STEP 1  -> Create Django project
# STEP 2  -> Create Django app
# STEP 3  -> Install/configure DRF
# STEP 4  -> Create a model
# STEP 5  -> Run makemigrations and migrate
# STEP 6  -> Create Serializer
# STEP 7  -> Create APIView
# STEP 8  -> Connect APIView to URL
# STEP 9  -> Test GET/POST using Postman
# STEP 10 -> Add Authentication
# STEP 11 -> Add Permissions
#
# We will write the actual project code separately.
# The code will contain beginner-friendly comments explaining
# WHAT each line does and WHY we need it.
#
# ============================================================
# END OF DRF NOTES
# ============================================================


# CLIENT
# |
# HTTP
# REQUEST
# ↓
# URL
# ↓
# APIView
# |
# ┌───────┴───────┐
# ↓               ↓
# Authentication
#                 Permissions
# | |
# └───────┬───────┘
# ↓
# Serializer
# ↓
# Model / Database
# ↓
# Response
# ↓
# CLIENT