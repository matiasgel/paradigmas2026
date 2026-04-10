(ns tp04.ej12)

;; Ejercicio 12 — Transducer vs pipeline
;; Trazabilidad: F-21

(defn procesar-pipeline
  "Pipeline clásico con ->>:
   filtrar activas con :total > 100, extraer :total, sumar."
  [ordenes]
  ;; TODO: Implementar con ->>
  )

(defn procesar-transducer
  "Mismo resultado que procesar-pipeline, pero usando transduce."
  [ordenes]
  ;; TODO: Implementar con transduce
  )

(defn totales-pipeline
  "Pipeline clásico: vector de totales de activas con :total > 100."
  [ordenes]
  ;; TODO: Implementar con ->> e into []
  )

(defn totales-transducer
  "Mismo resultado que totales-pipeline, pero usando into con transducer."
  [ordenes]
  ;; TODO: Implementar con into y comp de transducers
  )
