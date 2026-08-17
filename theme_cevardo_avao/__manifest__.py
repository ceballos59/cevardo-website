{
    "name": "Cevardo AVAO Prototype Theme",
    "summary": "Minimal, editorial prototype theme for the AVAO brand",
    "description": """
        First visual prototype for Cevardo, the group behind the AVAO brand.
        A focused website theme designed to orient people through action,
        value, critical thinking and opportunity.
    """,
    "version": "18.0.1.0.1",
    "category": "Theme",
    "author": "Cevardo Creative",
    "website": "https://avaopolis.es",
    "license": "LGPL-3",
    "depends": ["website"],
    "data": [
        "views/website_templates.xml",
        "views/website_pages.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "theme_cevardo_avao/static/src/scss/avao.scss",
        ],
    },
    "post_init_hook": "post_init_hook",
    "installable": True,
    "application": False,
    "auto_install": False,
}
