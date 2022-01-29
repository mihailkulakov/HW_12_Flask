from flask import Flask, request
import json
from utils import get_settings, get_candidates, get_candidate_by_cid, search_candidate_by_name, search_candidate_by_skill



app = Flask(__name__)

@app.route("/")

def main_page():
    settings = get_settings()
    if settings["online"]:
        return "Приложение работает"
    return "Приложение не работает"


@app.route("/candidate/<int:cid>")
def page_candidate(cid):

    candidate = get_candidate_by_cid(cid)
    page_content = f"""
    <h1>{candidate["name"]}</h1>
    <p>{candidate["position"]}</p>
    <img src="{candidate["picture"]}" width=200/>
    <p>{candidate["skills"]}</p>
    """
    return page_content

@app.route("/list")
def page_list():
    candidates = get_candidates()
    page_content = "<h1>Все кандидаты</h1>"
    for candidate in candidates:
        page_content += f"""
        <p><a href="/candidate/{candidate["id"]}">{candidate["name"]}</a></p>
        """
    return page_content



@app.route("/search")
def page_search_by_name():
    name = request.args.get("name", "")
    candidates = search_candidate_by_name(name)
    candidates_count = len(candidates)
    page_content = f"<h1> Найдено кандидатов: {candidates_count}"

    for candidate in candidates:
        page_content += f"""
        <p><a href="/candidate/{candidate["id"]}">{candidate["name"]}</a></p>
        """
    return page_content


@app.route("/skill/<skill_name>")
def page_search_by_skills(skill_name):

    candidates = search_candidate_by_skill(skill_name)
    candidates_count = len(candidates)
    page_content = f"<h1> Найдено со скиллом {skill_name}: {candidates_count}"

    for candidate in candidates:
        page_content += f"""
        <p><a href="/candidate/{candidate["id"]}">{candidate["name"]}</a></p>
        """
    return page_content

app.run()

