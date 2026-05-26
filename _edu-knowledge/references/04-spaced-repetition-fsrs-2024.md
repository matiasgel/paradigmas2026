# Spaced Repetition — FSRS v4 & Evidencia

**Fuente algoritmo:** Ye, J. (2023-2024). *FSRS — Free Spaced Repetition Scheduler*, open-source MIT license.
**Fuentes académicas:**
- Latimier, A. et al. (2021). *A Meta-Analytic Review of the Benefit of Spacing Out Retrieval Practice*, Educational Psychology Review, 33, pp. 959-987
- Toppino, T.C. & Gerbier, E. (2024). *About Practice: Repetition, Spacing, and Abstraction*, Psychology of Learning and Motivation, Vol. 80
- Ebbinghaus, H. (1885/2013). *Memory: A Contribution to Experimental Psychology* — curva del olvido (clásico vigente)
**Relevancia Sprint:** S2.1

## FSRS v4 — Algoritmo (reemplaza SM-2)

### Modelo DSR (Difficulty, Stability, Retrievability)
- **Difficulty (D):** Dificultad intrínseca del material, 1-10. Se ajusta con cada review
- **Stability (S):** Intervalo óptimo en días donde R=90%. Crece con reviews exitosos
- **Retrievability (R):** Probabilidad de recordar. Decae exponencialmente:
  ```
  R(t) = (1 + t/(9*S))^(-1)
  donde t = días desde último review, S = stability
  ```

### Parámetros Default FSRS v4
```python
FSRS_PARAMS = [
    0.40255,  # w0: initial stability (again)
    1.18385,  # w1: initial stability (hard)
    3.173,    # w2: initial stability (good)
    15.69105, # w3: initial stability (easy)
    7.1949,   # w4: difficulty weight
    0.5345,   # w5: stability decay
    1.4604,   # w6: stability increase factor
    0.0046,   # w7: stability decrease factor
    1.54575,  # w8: difficulty after fail
    0.1192,   # w9-w12: review multipliers
    1.01925,
    1.9395,
    0.11,
    0.29605,  # w13: hard penalty
    2.2698,   # w14: easy bonus
    0.2315,   # w15: difficulty revert
    2.9898,   # w16: stability after fail (short-term)
    0.51655,  # w17: stability after fail (long-term)
    0.6621,   # w18: fuzz factor
]
```

### Ventajas sobre SM-2
- **15% menos reviews** para mismo nivel de retención (estudio con 10k+ usuarios Anki)
- Modelo continuo vs. discreto (SM-2 usa intervalos fijos)
- Se adapta al alumno individual, no solo al material
- Código abierto, MIT license, implementaciones en Python, JS, Rust

### Ratings (igual que Anki)
- **1 (Again):** No recordé
- **2 (Hard):** Recordé con dificultad
- **3 (Good):** Recordé correctamente
- **4 (Easy):** Recordé fácilmente

## Evidencia Meta-Analítica

### Latimier et al. (2021)
- 89 estudios post-2006
- Effect size spacing: **d=0.62** (IC 95%: 0.49-0.75)
- El beneficio es mayor para:
  - Material complejo (d=0.73) vs. simple (d=0.38)
  - Intervalos más largos entre reviews
  - Tests con retrieval practice (vs. re-study)

### Toppino & Gerbier (2024)
- El spacing effect es más fuerte para material complejo
- **Relevante para CS:** Conceptos de programación son inherentemente complejos (alta interactividad de elementos)
- Abstracción beneficia el spacing: los repasos deben variar el formato, no repetir exactamente
- **Implementación EDU:** Slides de repaso deben ser socráticas (retrieval), no resúmenes pasivos

### Cepeda et al. (2006→2023)
- Meta-análisis original de 254 estudios confirmado
- Intervalos óptimos Inter-Study Interval (ISI):
  - Test en 1 semana: ISI = 1 día
  - Test en 1 mes: ISI = 7 días
  - Test en 6 meses: ISI = 21 días
- **Implementación EDU:** spaced_repetition.py usa FSRS (no SM-2) con estos intervalos base

## Aplicación Grupal (no individual)
- Anki/SuperMemo = autoaprendizaje individual
- EDU = spaced repetition a nivel de CLASE GRUPAL
- El docente inserta slides de repaso en clases futuras
- Se calibra dificultad promedio del grupo, no individual
- **Implementación:** score del TP = proxy de dificultad grupal para FSRS
