import sys
from src.paper_picker import pick_next_paper
from src.emailer import send_daily_paper


def main():
    paper = pick_next_paper()
    if paper is None:
        print("No quedan papers en papers.json. Añade más y/o reinicia state/state.json.")
        sys.exit(0)

    print(f"Paper elegido: {paper['title']}")
    send_daily_paper(paper)
    print("Email enviado correctamente.")


if __name__ == "__main__":
    main()
