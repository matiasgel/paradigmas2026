# Workflow: Student Feedback Loop

**Module:** edu
**Phase:** 3 — Producción de Temas
**Owner Agent:** student-simulator

---

## Overview

Procesa resultados de encuestas reales de alumnos y calibra el long-term del simulador.

## Steps

### Step 1: Load Survey Data
- **Agent:** student-simulator
- **Input:** Survey results (CSV, form responses, or manual input)
- **Action:** Parse and structure survey data

### Step 2: Compare with Simulation
- **Agent:** student-simulator
- **Input:** Previous simulation predictions (score-pedagogico.md)
- **Action:** Calculate deviation between predicted and actual responses
- **Output:** Comparison report with delta analysis

### Step 3: Calibrate
- **Agent:** student-simulator
- **Action:** Adjust long-term calibration parameters based on real data
- **Output:** Updated `_edu-memory/calibracion-simulador/` — NEVER reset
- **Note:** This data accumulates year over year for improved accuracy

