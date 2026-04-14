(ns tp04.ej07
  "Ejercicio 7 — Partial en Clojure (5 pts). Trazabilidad: F-15"
  (:require [clojure.string :as str]))

;; Retorna {:status :ok :value value} si no vacío, {:status :error :error "FIELD es obligatorio"}.
(defn required-field [field-name value]
  ;; TODO: implementar
  )

(def doble
  ;; TODO: (partial * 2)
  )

(def triple
  ;; TODO: (partial * 3)
  )

(def validate-name
  ;; TODO: (partial required-field "nombre")
  )

(def validate-email
  ;; TODO: (partial required-field "email")
  )
