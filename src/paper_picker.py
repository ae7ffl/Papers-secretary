import json
from pathlib import Path

PAPERS_PATH = Path(__file__).parent.parent / "papers.json"
STATE_PATH = Path(__file__).parent.parent / "state" / "state.json"


def load_papers() -> list[dict]:
    return json.loads(PAPERS_PATH.read_text(encoding="utf-8"))


def load_state() -> dict:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    return {"next_index": 0}


def save_state(state: dict):
    STATE_PATH.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")


def pick_next_paper() -> dict | None:
    """Devuelve el siguiente paper de papers.json en orden, o None si ya
    se han enviado todos (hasta que añadas más y reinicies el índice)."""
    papers = load_papers()
    state = load_state()
    idx = state["next_index"]

    if idx >= len(papers):
        return None

    paper = papers[idx]
    state["next_index"] = idx + 1
    save_state(state)
    return paper
