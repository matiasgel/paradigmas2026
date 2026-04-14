(ns tp04.ej16
  "Ejercicio 16 — DSL data-driven (5 pts). Trazabilidad: F-31"
  (:require [clojure.string :as str]))

;; Vector de reglas: {:field :name, :pred fn, :msg "..."}
(def user-rules
  ;; TODO: definir al menos 3 reglas (nombre no vacío, email con @, edad >= 18)
  [])

;; Aplica todas las reglas a data. Retorna vector de {:field :error} (vacío si ok).
(defn validate [rules data]
  ;; TODO: implementar
  )

;; true si no hay errores.
(defn valid? [rules data]
  ;; TODO: implementar
  )
