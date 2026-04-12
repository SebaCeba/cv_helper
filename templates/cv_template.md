# {{full_name}}
**{{title}}**  
{{location}}  
📧 {{email}}  
🔗 {{linkedin}}

---

## PERFIL EJECUTIVO
{{profile_summary}}

---

## EXPERIENCIA PROFESIONAL

{{#each roles}}
### {{company}}  
**{{position}}**  
*{{start_date}} – {{end_date}}*

{{#each responsibilities}}
- {{this}}
{{/each}}

{{/each}}

---

## PROYECTOS DESTACADOS

{{#each projects}}
### {{name}}
**{{company}}** | {{year}}

{{description}}

**Logros:**
{{#each achievements}}
- {{this}}
{{/each}}

**Tecnologías:** {{technologies}}

{{/each}}

---

## ÁREAS DE EXPERTISE
{{#each expertise_areas}}
- {{this}}
{{/each}}

---

## TECNOLOGÍAS & PLATAFORMAS

{{#each technology_categories}}
**{{category}}**
{{#each items}}
- {{name}} ({{proficiency}})
{{/each}}

{{/each}}

---

## FORMACIÓN ACADÉMICA
{{#each education}}
**{{degree}}** — {{institution}} ({{period}})  
{{/each}}

---

## CERTIFICACIONES
{{#each certifications}}
- {{name}} ({{issuer}})
{{/each}}

---

## IDIOMAS
{{#each languages}}
- {{language}}: {{level}}
{{/each}}

---

## DIFERENCIALES PROFESIONALES
{{#each differentials}}
- {{this}}
{{/each}}
