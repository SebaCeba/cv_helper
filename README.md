# 📄 CV Helper

Sistema modular de generación de CVs profesionales basado en archivos JSON estructurados.

> **Proyecto**: Generador de CV personalizable  
> **Autor**: Sebastián Ceballos  
> **Última actualización**: Abril 2026

## 🎯 Descripción

CV Helper es un sistema de gestión de información profesional que permite mantener toda tu experiencia, habilidades y logros en formato JSON estructurado. Esto facilita:

- ✅ **Generación de múltiples formatos** de CV (HTML, Markdown, PDF)
- ✅ **Personalización por rol** o industria específica
- ✅ **Mantenimiento centralizado** de información profesional
- ✅ **Eliminación de duplicados** y datos inconsistentes
- ✅ **Versionado y control** de tu historia profesional

## 📁 Estructura del Proyecto

```
cv_helper/
├── data/                          # 🗄️ Fuente única de verdad
│   ├── profile_master.json        # Información personal, formación, idiomas
│   ├── roles.json                 # Experiencia profesional
│   ├── projects.json              # Proyectos destacados
│   ├── achievements.json          # Logros profesionales
│   ├── skills.json                # Habilidades técnicas y blandas
│   └── source_notes.md            # Material fuente sin procesar
│
├── prompts/                       # 📝 Instrucciones para el sistema
│   ├── setup_data.md              # Cómo configurar datos
│   └── generate_cv.md             # Cómo generar CVs
│
├── templates/                     # 🎨 Plantillas base
│   └── cv_template.md             # Template Handlebars
│
├── outputs/                       # 📄 CVs generados
│   ├── README.md                  # Documentación de outputs
│   ├── CV_Head_Plataformas.md
│   ├── CV_Ejecutivo_Corporativo.html
│   ├── CV_Ejecutivo_Minimalista.html
│   └── archive/                   # Artefactos históricos
│
├── .gitignore                     # Configuración Git
├── LICENSE                        # Licencia MIT
├── README.md                      # Este archivo
├── INSTRUCCIONES_GIT.md           # Guía Git
└── validate_json.py               # Script de validación
```

## 📊 Organización de Datos

### `/data` - Fuente Única de Verdad

Toda la información profesional está estructurada en archivos JSON:

| Archivo | Contenido |
|---------|-----------|
| `profile_master.json` | Información personal, formación académica, certificaciones, idiomas, diferenciales |
| `roles.json` | Experiencia laboral detallada con responsabilidades y tecnologías |
| `projects.json` | Proyectos destacados vinculados a roles con logros específicos |
| `achievements.json` | Logros profesionales categorizados por tipo de impacto |
| `skills.json` | Áreas de expertise, tecnologías con niveles de proficiencia, soft skills |
| `source_notes.md` | Material fuente sin procesar (referencia temporal) |

**Principio clave**: Cada dato vive en **un solo lugar**. Los CVs generados son outputs derivados de `/data`.

## ✅ Validación

Ejecutar script de validación:
```powershell
python validate_json.py
```

Estado actual: **✓ TODOS LOS ARCHIVOS JSON SON VÁLIDOS**

## 🎯 Principios de Diseño

1. **Sin inventar información**: Solo datos existentes de CVs originales
2. **Sin duplicados**: Información única en cada archivo
3. **Textos concisos**: Información clara y directa
4. **Estructura modular**: Fácil actualización y mantenimiento
5. **JSON válido**: Verificado programáticamente

## 🚀 Inicio Rápido

### 1. Validar datos estructurados

```powershell
python validate_json.py
```

Esto verifica que todos los archivos JSON en `/data` sean válidos.

### 2. Generar un CV

1. Revisa las instrucciones en `/prompts/generate_cv.md`
2. Usa los templates de `/templates` como base
3. Los outputs se guardan en `/outputs`

### 3. Actualizar información

1. Edita los archivos JSON correspondientes en `/data`
2. Valida con `python validate_json.py`
3. Regenera los CVs según necesidad

## 🛠️ Próximas Funcionalidades

- [ ] Generador automático HTML desde JSON
- [ ] Exportación a PDF
- [ ] Templates personalizables
- [ ] Filtros por industria/rol
- [ ] Integración con LinkedIn API
- [ ] Sistema de versionado de CVs

## 📊 Características

- 🔒 **Sin información inventada**: Solo datos verificados
- 🎨 **Modular**: Fácil actualización de secciones individuales
- ✅ **Validado**: JSON validado automáticamente
- 📝 **Documentado**: Cada archivo con propósito claro
- 🔗 **Relacional**: IDs conectan proyectos con roles

## 🤝 Contribuir

Este es un proyecto personal, pero si encuentras útil la estructura, ¡úsala libremente!

## 📝 Licencia

MIT License - Úsalo como plantilla para tu propio CV Helper

## 📞 Contacto

**Sebastián Ceballos**
- LinkedIn: [linkedin.com/in/sebaceba](https://linkedin.com/in/sebaceba)
- Email: sceballost@gmail.com

---

⭐ Si esta estructura te resulta útil, considera darle una estrella al repo
