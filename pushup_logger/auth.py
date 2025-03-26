from flask import Blueprint, render_template

auth =Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
    return "tThis page is for signing up"

@auth.route('/login')
def login():
    return "This page is for logging in"

@auth.route('/logout')
def logout():
    return "This page is for logging out"