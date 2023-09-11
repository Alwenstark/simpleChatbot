Below packages are need to import

from dict import chat_dict, symptom_to_disease, lang, keyword_urls
from flask import Flask, render_template, request, jsonify
import requests
import webbrowser
from translate import Translator
from bs4 import BeautifulSoup
from datetime import datetime
import time