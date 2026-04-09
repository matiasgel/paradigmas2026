# Learning Analytics — Ifenthaler, Tsai, Yan (2020-2024)

**Fuentes:**
- Ifenthaler, D. & Yau, J.Y-K. (2020). *Utilising Learning Analytics to Support Study Success*, ETR&D, 68, pp. 1961-1990
- Tsai, Y-S. et al. (2020). *The SHEILA Framework*, Journal of Learning Analytics, 7(3)
- Yan, L. et al. (2024). *Practical and Ethical Challenges of LLMs in Education*, BJET, 55(1)
- Arnold, K.E. & Pistilli, M.D. (2012). *Course Signals at Purdue*, LAK '12 (seminal, con notas de cuestionamiento)
- EDUCAUSE Horizon Report (2024)
**Relevancia Sprint:** S5.1

## Framework de Learning Analytics Efectivo (Ifenthaler 2020)

### 3 Condiciones para que LA funcione
1. **Integrar múltiples fuentes de datos** — no solo grades, también engagement, tiempo, patrones
2. **Feedback actionable** — no solo "estás en riesgo", sino "específicamente en tema X, sugerencia Y"
3. **Docente en el loop** — el analytics informa al docente, no toma decisiones solo

### Métricas Recomendadas por Alumno

| Métrica | Cómo calcularla | Umbral de riesgo |
|---------|-----------------|------------------|
| Score promedio ponderado | Promedio de TPs/quizzes ponderado por puntos | <50% |
| Tendencia | Slope de últimos 3 scores | Negativa (decreciente) |
| Engagement index | Entregas a tiempo / total entregas | <60% |
| Asistencia | Presencias / clases dadas | <75% |
| Risk score compuesto | Si 2+ de {bajo score, tendencia baja, inasistencia >25%} | 2+ factores |

### Sistema de Semáforo
- 🟢 **Verde:** Todos los indicadores en rango
- 🟡 **Amarillo:** 1 indicador fuera de rango
- 🔴 **Rojo:** 2+ indicadores fuera de rango → intervención sugerida

## SHEILA Framework (Tsai 2020)

### Implementación Ética de LA
1. **Propósito claro:** ¿para qué se usan los datos?
2. **Transparencia:** el alumno sabe qué se mide
3. **Privacidad:** datos anonimizados en reportes compartidos
4. **Acción:** los datos llevan a intervenciones concretas
5. **Evaluación:** se mide si LA realmente mejora outcomes

### Adoptado por 51 universidades europeas

## Course Signals (Arnold 2012) — Con Matices

### Resultado Original
- Reducción 21% en DFW rates (Drop/Fail/Withdraw) en Purdue

### Cuestionamientos Posteriores
- Caulfield (2013): selección sesgada de cursos
- Bogus & Miltenoff (2019): variables confusoras no controladas
- **Consenso actual:** efecto significativo pero menor (~10-12%) cuando se controlan variables

### Lección para EDU
- NO prometer reducciones de 21% — ser conservador
- El valor está en DETECTAR temprano, no en el modelo predictivo exacto
- Regla simple (2+ factores de riesgo) funciona casi tan bien como modelos complejos

## GenAI + Learning Analytics (Yan 2024)

### Oportunidades
- Personalización de feedback a escala
- Detección de patrones de error comunes via LLM
- Generación automática de intervenciones sugeridas

### Riesgos
- **Privacidad:** datos de alumnos + LLM = riesgo GDPR/LOPD
- **Bias algorítmico:** LMs pueden amplificar sesgos existentes
- **Over-reliance:** docentes que delegan decisiones pedagógicas al sistema

### Recomendaciones para EDU
- Datos de alumnos NUNCA salen del workspace (no se envían a APIs externas)
- Analytics corre localmente con SQLite
- Reportes usan pseudónimos por default
- .gitignore para CSV con datos personales

## EDUCAUSE Horizon (2024)
- LA + AI early alerts: adopción masiva (>2000 instituciones)
- Tendencia: de dashboards retrospectivos a alerts proactivos
- EDU está alineado: genera alertas (🔴) con sugerencias de acción
