import json
from configs import SETTINGS_PATH,CANDIDATES_PATH




def get_settings():
    """
    Получить из жсона настройки
    :return: настройки
    """
    with open(SETTINGS_PATH) as file:
        settings = json.load(file)
    return settings


def get_candidates():
    """
    Получить из жсона словарь с кандидатами
    :return: словарь с кандидатами
    """
    with open(CANDIDATES_PATH, "r", encoding="utf-8") as file:
        candidates = json.load(file)
    return candidates


def get_candidate_by_cid(сid):
    """
    Получить кандидата по айди
    :param сid: айди кандидата
    :return: кандидат
    """
    candidates = get_candidates()
    for candidate in candidates:
        if candidate.get("id") == сid:
            return candidate


def search_candidate_by_name(name):
    """
    Найти кандидата по имени
    :param name: имя
    :return: список всех подходящих кандидатов
    """

    settings = get_settings()
    case_sensitive = settings["case-sensitive"]
    candidates = get_candidates()

    candidates_match = []

    for candidate in candidates:
        if name in candidate["name"]:
            candidates_match.append(candidate)

        if not case_sensitive:
            if name.lower() in candidate["name"].lower():
                candidates_match.append(candidate)

    return candidates_match


def search_candidate_by_skill(skill_name):
    """
    Найти кандидата по скиллу
    :param skill_name: название скилла
    :return: список всех кандидатов с этим скиллом с ограничением кол-ва, указанным в настройках
    """
    settings = get_settings()
    limit = settings.get('limit', 3)
    candidates = get_candidates()
    candidates_match = []

    skill_name = skill_name.lower()

    for candidate in candidates:
        skills = candidate["skills"].lower().split(", ")
        if skill_name in skills:
            candidates_match.append(candidate)

    return candidates_match[:limit]