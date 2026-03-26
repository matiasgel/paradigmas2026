#!/usr/bin/env python3
"""
app_adaptive.py — Streamlit UI para Aprendizaje Adaptativo (S13.3)
===================================================================
Interfaz web opcional para el tutor adaptativo.

Uso:
    streamlit run app_adaptive.py

Dependencias: streamlit, scripts/adaptive_tutor.py
"""

from __future__ import annotations

import sys
from pathlib import Path

# Asegurar que scripts/ esté en el path
_root = Path(__file__).resolve().parent
_scripts = _root / "scripts"
if str(_scripts) not in sys.path:
    sys.path.insert(0, str(_scripts))

try:
    import streamlit as st
except ImportError:
    print("❌ Streamlit no instalado. Ejecutar: pip install streamlit")
    sys.exit(1)

from pipeline_common import find_project_root, load_config


def main() -> None:
    st.set_page_config(page_title="EDU — Aprendizaje Adaptativo", page_icon="🎓", layout="wide")
    st.title("🎓 EDU — Aprendizaje Adaptativo")
    st.caption("Sin currícula fija · Knowledge Space Theory + BKT")

    project_root = find_project_root(Path.cwd())
    config = load_config(project_root)

    if not config.get("knowledge_graph_enabled", False):
        st.error("knowledge_graph_enabled no está habilitado en config.")
        return

    # Sidebar
    with st.sidebar:
        st.header("Configuración")
        course = st.text_input("Curso:", value="leng-2026")
        student_id = st.text_input("ID estudiante:", value="estudiante_01")

    kg_path = project_root / "salida" / "cursadas" / course / "knowledge-graph.json"
    if not kg_path.exists():
        st.warning(f"KG no encontrado para '{course}'. Ejecutar `/edu-build-kg` primero.")
        return

    from adaptive_tutor import AdaptiveTutor

    state_dir = project_root / "salida" / "cursadas" / course / "students"
    state_dir.mkdir(parents=True, exist_ok=True)
    tutor = AdaptiveTutor(student_id, kg_path, state_dir)

    # Main content
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Estado actual")
        summary = tutor.session_summary()
        st.metric("Conceptos dominados", f"{summary['mastered']}/{summary['total_concepts']}")
        st.progress(summary["progress_pct"] / 100)

        if summary["frontier"]:
            st.write("**Frontera de aprendizaje:**")
            for c in summary["frontier"][:8]:
                st.write(f"  • {c}")

    with col2:
        st.subheader("🎯 Recomendación")
        rec = tutor.recommend_next()
        if rec.get("concept"):
            st.success(f"**{rec['concept']}**")
            st.caption(rec.get("why", ""))
            if rec.get("learning_path"):
                st.write("Camino: " + " → ".join(rec["learning_path"]))
        else:
            st.balloons()
            st.success(rec.get("message", "¡Completado!"))

    # Update section
    st.divider()
    st.subheader("📝 Registrar evaluación")
    with st.form("update_form"):
        concept = st.text_input("Concepto evaluado:")
        correct = st.checkbox("¿Respuesta correcta?")
        submitted = st.form_submit_button("Registrar")
        if submitted and concept:
            tutor.update_after_assessment(concept, correct)
            m = tutor.state.mastery.get(concept, 0)
            st.write(f"{'✅' if correct else '❌'} {concept}: mastery = {m:.2f}")
            st.rerun()


if __name__ == "__main__":
    main()
