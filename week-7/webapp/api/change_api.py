from flask import *
import mysql.connector
from mysql.connector import errors

# 藍圖
change_bp=Blueprint("change", __name__)

@change_bp.route("/api/member", methods=["GET", "POST"])
def change():
    pass