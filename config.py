
from calendar import month
from telnetlib import STATUS
from unicodedata import name
from click import style
from flask import Flask, render_template, request, redirect, url_for, session,flash, redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import os
import urllib.request
from jmespath import search
from werkzeug.utils import secure_filename