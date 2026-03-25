---
description: 'EDU — Validar archivo GIFT antes de importar a Moodle. Detecta errores críticos y advertencias. Se puede correr sobre un tp-quiz.gift existente o sobre contenido pegado en el chat.'
tools: ['read', 'edit', 'search']
---

1. Load `{project-root}/_edu/config.yaml` and store ALL fields as session variables.
2. Load `{project-root}/_edu/active-topic.yaml` → store `{topic_folder}`, `{topic_number}`, `{topic_name}`.
   Si no existe, continuar sin tema activo (el usuario puede pegar el GIFT directamente).
3. **Determinar qué validar:**
   - Si existe `{topic_folder}/tp-quiz.gift` → preguntar: "¿Validar el GIFT del tema activo (`{topic_folder}/tp-quiz.gift`) o pegar otro contenido?"
   - Si no hay tema activo → "Pegá el contenido del archivo GIFT a validar o indicá la ruta del archivo."
   - Guardar en `{gift_content}` o `{gift_file_path}` según corresponda.
4. **Ejecutar validación GIFT completa** siguiendo todas las reglas del task:
   Load `{project-root}/_edu/tasks/gift-validator.md` y aplicar cada verificación.
5. **Mostrar reporte completo** con el formato definido en el task:
   - ✅ Preguntas válidas
   - ❌ Errores críticos (con número de pregunta, regla, descripción y corrección sugerida)
   - ⚠️  Advertencias
6. **Si hay errores críticos:** preguntar "¿Querés que corrija automáticamente los que son autofix-safe (pesos, BOM, líneas en blanco)?"
   - Si el docente dice sí → aplicar fixes, reportar qué se cambió, guardar el archivo corregido.
   - Para errores que requieren decisión pedagógica → listar claramente y esperar instrucción.
7. **Si todo OK:** confirmar "✅ El archivo GIFT está listo para importar en Moodle 5."
   Recordar el procedimiento de importación:
   > Banco de preguntas → Importar → Formato GIFT → activar "Get category from file" si corresponde.
