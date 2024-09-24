from flask import render_template, request
from app import app
from steam_web_api import Steam
import os
from dotenv import load_dotenv

load_dotenv()


KEY = os.getenv("STEAM_API_KEY", "default_value")
steam = Steam(KEY)


@app.route("/")
def home():
    list_steam_id = [1245620, 570, 1151340, 2519060, 495420, 1509960]
    list_game_name = []
    list_game_img = []
    list_steamid = []

    for game in list_steam_id:
        game_id = game
        game = steam.apps.get_app_details(game)
        name_game = game[str(game_id)]["data"]["name"]
        img_game = game[str(game_id)]["data"]["header_image"]
        list_game_name.append(name_game)
        list_game_img.append(img_game)

    for steamid in list_steam_id:
        list_steamid.append(steamid)

    stream_id = list_steamid
    img = list_game_img
    contexto = {"listas": zip(stream_id, img)}
    return render_template("main.html", **contexto)


@app.route("/DetailsGame/<int:steam_id>")
def details_game(steam_id):
    log = 1
    game_search = steam.apps.search_games(str(steam_id))
    price_game = game_search["apps"][0]["price"]
    game = steam.apps.get_app_details(steam_id)
    game_rec = game[str(steam_id)]["data"]
    name_game = game_rec["name"]
    img_game = game_rec["header_image"]
    description_game = game_rec["short_description"]
    description_game_long = game_rec["detailed_description"]
    lenguages = game_rec.get("supported_languages", "No disponible")
    pc_requirements = game_rec.get("pc_requirements", {})
    mac_requirements = game_rec.get("mac_requirements", {})
    linux_requirements = game_rec.get("linux_requirements", {})
    pc_requirement_minimum = pc_requirements.get("minimum", "No disponible")
    pc_requirement_recommended = pc_requirements.get("recommended", "No disponible")
    mac_requirement_minimum = mac_requirements.get("minimum", "No disponible")
    mac_requirement_recommended = mac_requirements.get("recommended", "No disponible")
    linux_requirement_minimum = linux_requirements.get("minimum", "No disponible")
    linux_requirement_recommended = linux_requirements.get(
        "recommended", "No disponible"
    )

    lista_zip = ""
    if "dlc" in game[str(steam_id)]["data"]:
        dlc_game = game[str(steam_id)]["data"]["dlc"]
        name_dlc_list = []
        img_list_dlc = []
        price_list_dlc = []
        try:
            if dlc_game:
                for dlc in dlc_game:
                    dlc_game_search = steam.apps.search_games(str(dlc))
                    game_dlc = steam.apps.get_app_details(dlc)[str(dlc)]
                    name_dlc = game_dlc["data"]["name"]
                    img_dlc = game_dlc["data"]["capsule_image"]
                    price_dlc = dlc_game_search["apps"][0]["price"]
                    name_dlc_list.append(name_dlc)
                    img_list_dlc.append(img_dlc)
                    price_list_dlc.append(price_dlc)
                lista_zip = zip(name_dlc_list, img_list_dlc, price_list_dlc)
            else:
                print("No hay dlc")
        except Exception as e:
            print("Error al obtener DLC", e)

    contexto = {
        "name": name_game,
        "img": img_game,
        "price": price_game,
        "desc": description_game,
        "dlc": lista_zip,
        "desc_long": description_game_long,
        "pc_minimum": pc_requirement_minimum,
        "pc_recommended": pc_requirement_recommended,
        "mac_minimum": mac_requirement_minimum,
        "mac_recommended": mac_requirement_recommended,
        "linux_minimum": linux_requirement_minimum,
        "linux_recommended": linux_requirement_recommended,
        "lenguage": lenguages,
        "log": log,
    }
    return render_template("details_game.html", **contexto)


@app.route("/MoreGames")
def more_games():
    query = request.args.get("q")

    steam_app = steam.apps.search_games(str(query))
    steam_app_list = steam_app["apps"]

    name_game_list = []
    img_game_list = []
    for i in range(len(steam_app_list)):
        list_id = steam_app["apps"][i]
        name_game = list_id["name"]
        img_game = list_id["img"]

        name_game_list.append(name_game)
        img_game_list.append(img_game)

    context = {"lista": zip(name_game_list, img_game_list)}
    return render_template("more_games.html", **context)


@app.route("/Login")
def login():
    return render_template("login.html")


@app.route("/Register")
def register():
    return render_template("register.html")
