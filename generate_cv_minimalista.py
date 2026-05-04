"""
Generador de CV - Estilo Minimalista
Genera un HTML a partir de los archivos JSON en /data.

Uso:
    python generate_cv_minimalista.py
    python generate_cv_minimalista.py --headline head_plataformas
    python generate_cv_minimalista.py --headline consultor_senior --output outputs/CV_Consultor.html

Opciones de headline:
    head_plataformas     Head de Plataformas Financieras & Transformación Digital
    lider_transformacion Líder de Transformación Digital & Plataformas Financieras (default)
    gerente_tecnologia   Gerente de Tecnología & Plataformas
    consultor_senior     Consultor Senior en Transformación Digital & Plataformas
"""

import json
import argparse
from pathlib import Path
from datetime import date


# ---------------------------------------------------------------------------
# Carga de datos
# ---------------------------------------------------------------------------

def load_json(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_all_data() -> dict:
    base = Path("data")
    return {
        "profile":      load_json(base / "profile_master.json"),
        "roles":        load_json(base / "roles.json")["roles"],
        "skills":       load_json(base / "skills.json"),
        "achievements": load_json(base / "achievements.json")["achievements"],
    }


# ---------------------------------------------------------------------------
# Helpers HTML
# ---------------------------------------------------------------------------

def h(text: str) -> str:
    """Escapa caracteres HTML básicos."""
    return (text
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;"))


def tech_tags(items: list[str]) -> str:
    return "".join(f'<span class="tech-tag">{h(i)}</span>' for i in items)


def sidebar_list(items: list[str]) -> str:
    rows = "".join(f"<li>{h(i)}</li>" for i in items)
    return f"<ul>{rows}</ul>"


# ---------------------------------------------------------------------------
# Secciones del sidebar
# ---------------------------------------------------------------------------

def section_expertise(skills: dict) -> str:
    items = skills["expertise_areas"][0]["skills"]
    short = [s.split(" y ")[0].split(" e ")[0] for s in items]
    return f"""
    <div class="sidebar-section">
        <h2>Expertise</h2>
        {sidebar_list(short)}
    </div>"""


def section_technologies(skills: dict) -> str:
    # Aplanar todas las tecnologías en tags
    all_techs = []
    for cat in skills["technologies"]:
        all_techs.extend([item["name"] for item in cat["items"]])
    tags = tech_tags(all_techs)
    return f"""
    <div class="sidebar-section">
        <h2>Tecnologías</h2>
        <div>{tags}</div>
    </div>"""


def section_education(profile: dict) -> str:
    items = ""
    for ed in profile["education"]:
        items += f"""
        <div class="education-item">
            <div class="degree">{h(ed['degree'])}</div>
            <div class="institution">{h(ed['institution'])} · {h(ed['period'])}</div>
        </div>"""
    return f"""
    <div class="sidebar-section">
        <h2>Formación</h2>
        {items}
    </div>"""


def section_certifications(profile: dict) -> str:
    names = [c["name"] for c in profile["certifications"]]
    return f"""
    <div class="sidebar-section">
        <h2>Certificaciones</h2>
        {sidebar_list(names)}
    </div>"""


def section_languages(profile: dict) -> str:
    langs = [f"{l['language']} ({l['level']})" for l in profile["languages"]]
    return f"""
    <div class="sidebar-section">
        <h2>Idiomas</h2>
        {sidebar_list(langs)}
    </div>"""


# ---------------------------------------------------------------------------
# Secciones del contenido principal
# ---------------------------------------------------------------------------

def section_profile(profile: dict) -> str:
    summary = h(profile["profile_summary"])
    return f"""
    <section class="section">
        <h2 class="section-title">Perfil Ejecutivo</h2>
        <p class="profile-text">{summary}</p>
    </section>"""


def section_experience(roles: list) -> str:
    jobs = ""
    for role in roles:
        bullets = "".join(
            f"<li>{h(r)}</li>" for r in role["responsibilities"]
        )
        end = role["end_date"]
        jobs += f"""
        <div class="job">
            <div class="job-header">
                <div class="job-left">
                    <div class="company">{h(role['company'])}</div>
                    <div class="job-title">{h(role['position'])}</div>
                </div>
                <div class="period">{h(role['start_date'])} – {h(end)}</div>
            </div>
            <ul>{bullets}</ul>
        </div>"""

    return f"""
    <section class="section">
        <h2 class="section-title">Experiencia Profesional</h2>
        {jobs}
    </section>"""


def section_differentials(profile: dict) -> str:
    items = "".join(
        f'<div class="differential-item">{h(d)}</div>'
        for d in profile["differentials"]
    )
    return f"""
    <section class="section">
        <h2 class="section-title">Diferenciales Profesionales</h2>
        <div class="differentials-grid">{items}</div>
    </section>"""


# ---------------------------------------------------------------------------
# Ensamblado del HTML completo
# ---------------------------------------------------------------------------

def build_html(data: dict, headline: str) -> str:
    profile  = data["profile"]
    roles    = data["roles"]
    skills   = data["skills"]

    personal = profile["personal"]
    title    = profile["headline_variants"].get(headline, personal["title"])
    name     = personal["full_name"]
    email    = personal["email"]
    linkedin = personal["linkedin"]
    location = personal["location"]
    linkedin_display = linkedin.replace("https://", "").rstrip("/")

    sidebar = (
        section_expertise(skills)
        + section_technologies(skills)
        + section_education(profile)
        + section_certifications(profile)
        + section_languages(profile)
    )

    main = (
        section_profile(profile)
        + section_experience(roles)
        + section_differentials(profile)
    )

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CV - {h(name)}</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

        * {{ margin: 0; padding: 0; box-sizing: border-box; }}

        @page {{ size: A4; margin: 0; }}

        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: white;
            color: #1a1a1a;
            line-height: 1.5;
            font-size: 9pt;
            font-weight: 400;
        }}

        .container {{
            max-width: 210mm;
            height: 297mm;
            margin: 0 auto;
            padding: 14mm 16mm;
            background: white;
            overflow: hidden;
        }}

        /* Header */
        .header {{
            margin-bottom: 11pt;
            padding-bottom: 8pt;
            border-bottom: 0.5pt solid #e5e7eb;
        }}
        .header h1 {{
            font-size: 22pt;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 3pt;
            letter-spacing: -0.8pt;
        }}
        .header .subtitle {{
            font-size: 10pt;
            color: #2563eb;
            font-weight: 500;
            letter-spacing: -0.2pt;
        }}
        .contact-bar {{
            display: flex;
            gap: 12pt;
            margin-top: 6pt;
            font-size: 8pt;
            color: #64748b;
        }}
        .contact-bar a {{ color: #2563eb; text-decoration: none; }}
        .contact-bar a:hover {{ text-decoration: underline; }}
        .contact-item {{ display: flex; align-items: center; gap: 4pt; }}

        /* Grid */
        .content-grid {{
            display: grid;
            grid-template-columns: 1fr 2fr;
            gap: 14pt;
        }}

        /* Sidebar */
        .sidebar {{ padding-right: 10pt; }}
        .sidebar-section {{ margin-bottom: 10pt; }}
        .sidebar-section h2 {{
            font-size: 8.5pt;
            font-weight: 700;
            color: #2563eb;
            text-transform: uppercase;
            letter-spacing: 1pt;
            margin-bottom: 5pt;
        }}
        .sidebar-section ul {{ list-style: none; }}
        .sidebar-section li {{
            font-size: 8pt;
            line-height: 1.5;
            color: #475569;
            margin-bottom: 2pt;
            padding-left: 8pt;
            position: relative;
        }}
        .sidebar-section li:before {{
            content: '';
            position: absolute;
            left: 0;
            top: 6pt;
            width: 3pt;
            height: 3pt;
            background: #2563eb;
            border-radius: 50%;
        }}
        .tech-tag {{
            display: inline-block;
            background: #f1f5f9;
            color: #475569;
            padding: 1.5pt 5pt;
            border-radius: 3pt;
            font-size: 7pt;
            margin: 1.5pt 2pt 1.5pt 0;
            font-weight: 500;
        }}
        .education-item {{ margin-bottom: 6pt; }}
        .degree {{ font-weight: 600; color: #0f172a; font-size: 8pt; line-height: 1.3; }}
        .institution {{ color: #64748b; font-size: 7.5pt; line-height: 1.3; }}

        /* Main content */
        .main-content {{
            border-left: 1pt solid #f1f5f9;
            padding-left: 14pt;
        }}
        .section {{ margin-bottom: 9pt; }}
        .section-title {{
            font-size: 9.5pt;
            font-weight: 700;
            color: #0f172a;
            text-transform: uppercase;
            letter-spacing: 0.8pt;
            margin-bottom: 6pt;
            position: relative;
            padding-left: 10pt;
        }}
        .section-title:before {{
            content: '';
            position: absolute;
            left: 0; top: 0; bottom: 0;
            width: 3pt;
            background: #2563eb;
            border-radius: 2pt;
        }}
        .profile-text {{
            font-size: 8.5pt;
            line-height: 1.5;
            color: #334155;
            text-align: justify;
        }}

        /* Jobs */
        .job {{ margin-bottom: 8pt; page-break-inside: avoid; }}
        .job-header {{
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            margin-bottom: 3pt;
        }}
        .job-left {{ flex: 1; }}
        .company {{ font-weight: 700; font-size: 9.5pt; color: #0f172a; }}
        .job-title {{ font-weight: 500; font-size: 8.5pt; color: #2563eb; margin-top: 1pt; }}
        .period {{ font-size: 7.5pt; color: #94a3b8; font-weight: 500; white-space: nowrap; }}
        .job ul {{ margin-top: 3pt; padding-left: 0; list-style: none; }}
        .job li {{
            margin-bottom: 2pt;
            padding-left: 12pt;
            position: relative;
            line-height: 1.4;
            font-size: 8pt;
            color: #475569;
        }}
        .job li:before {{ content: '→'; position: absolute; left: 0; color: #cbd5e1; font-weight: 300; }}

        /* Diferenciales */
        .differentials-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4pt 8pt;
        }}
        .differential-item {{
            background: #f8fafc;
            padding: 5pt 7pt;
            border-radius: 4pt;
            border-left: 2pt solid #2563eb;
            font-size: 7.5pt;
            line-height: 1.3;
            color: #475569;
        }}

        @media print {{
            body {{ print-color-adjust: exact; -webkit-print-color-adjust: exact; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header class="header">
            <h1>{h(name)}</h1>
            <div class="subtitle">{h(title)}</div>
            <div class="contact-bar">
                <div class="contact-item">{h(location)}</div>
                <div class="contact-item"><a href="mailto:{h(email)}">{h(email)}</a></div>
                <div class="contact-item"><a href="{h(linkedin)}" target="_blank">{h(linkedin_display)}</a></div>
            </div>
        </header>

        <div class="content-grid">
            <aside class="sidebar">
                {sidebar}
            </aside>
            <main class="main-content">
                {main}
            </main>
        </div>
    </div>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Generador de CV Minimalista")
    parser.add_argument(
        "--headline",
        default="lider_transformacion",
        choices=["head_plataformas", "lider_transformacion", "gerente_tecnologia", "consultor_senior"],
        help="Variante de título a usar"
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Ruta del archivo de salida (default: outputs/CV_Minimalista_<headline>.html)"
    )
    args = parser.parse_args()

    data = load_all_data()
    html = build_html(data, args.headline)

    output_path = args.output or f"outputs/CV_Minimalista_{args.headline}.html"
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text(html, encoding="utf-8")

    print(f"✓ CV generado: {output_path}")
    print(f"  Headline: {data['profile']['headline_variants'][args.headline]}")
    print(f"  Roles:    {len(data['roles'])}")
    print(f"  Skills:   {sum(len(c['items']) for c in data['skills']['technologies'])} tecnologías")


if __name__ == "__main__":
    main()
