from base64 import b64encode
from pathlib import Path


def post_init_hook(env):
    """Give the default website menu a Spanish, AVAO-oriented first impression."""
    for website in env["website"].search([]):
        mark_path = Path(__file__).parent / "static" / "src" / "img" / "avao-mark.png"
        if mark_path.exists():
            website.favicon = b64encode(mark_path.read_bytes())

        menus = env["website.menu"].search(
            [("website_id", "=", website.id), ("url", "in", ["/", "/contactus"])]
        )
        for menu in menus:
            menu.name = "Inicio" if menu.url == "/" else "Contacto"

        homepage = env["website.page"].search(
            [("website_id", "=", website.id), ("url", "=", "/")], limit=1
        )
        homepage.write(
            {
                "website_meta_title": "AVAO — Orientación práctica para construir tu lugar",
                "website_meta_description": (
                    "AVAO es una filosofía práctica de vida para personas que buscan "
                    "dirección, desarrollan capacidades, crean valor y construyen oportunidades."
                ),
                "website_meta_keywords": (
                    "AVAO, filosofía práctica de vida, acción, valor, oportunidad, "
                    "desarrollo personal, comunidad"
                ),
                "website_meta_og_img": "/theme_cevardo_avao/static/src/img/avao-mark.png",
            }
        )
