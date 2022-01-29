from flask import Flask, request, render_template
import json
from utils import get_settings, get_candidates, get_candidate_by_cid, search_candidate_by_name, search_candidate_by_skill



app = Flask(__name__)

@app.route("/")

def main_page():
    settings = get_settings()
    is_online = settings["online"]
    return render_template("index.html", is_online=is_online)



@app.route("/candidate/<int:cid>")
def page_candidate(cid):

    candidate = get_candidate_by_cid(cid)

    return render_template("candidate.html", candidate=candidate)

@app.route("/list")
def page_list():
    candidates = get_candidates()

    return render_template("list.html", candidates=candidates)



@app.route("/search/")
def page_search_by_name():
    name = request.args.get("name")
    candidates = search_candidate_by_name(name)
    candidates_count = len(candidates)

    return render_template("search_by_name.html", candidates=candidates, candidates_count=candidates_count)


@app.route("/skill/<skill_name>")
def page_search_by_skills(skill_name):

    candidates = search_candidate_by_skill(skill_name)
    candidates_count = len(candidates)

    return render_template("search_by_skills.html", candidates=candidates, candidates_count=candidates_count, skill_name=skill_name)

app.run()

