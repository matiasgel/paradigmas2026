(ns tp04.ej09
  "Ejercicio 9 — Validadores con currying (5 pts). Trazabilidad: F-18"
  (:require [clojure.string :as str]))

;; Retorna fn que valida value con pred. Ok → {:status :ok :value val}, error → {:status :error :error msg}.
(defn make-validator [pred error-msg]
  ;; TODO: implementar — retornar (fn [value] ...)
  )

;; Aplica validators en secuencia; para en el primer error.
(defn validate-field [value & validators]
  ;; TODO: implementar con reduce
  )

(def validate-not-empty
  ;; TODO: (make-validator ... "campo vacío")
  )

(def validate-email-format
  ;; TODO: (make-validator ... "email inválido")
  )
