(ns tp04.ej11)

;; Ejercicio 11 — Transducer básico
;; Trazabilidad: F-19, F-20

(def xf-activas-totales
  "Transducer que filtra órdenes activas y extrae :total.
   Definir con comp, filter y map (sin colección)."
  ;; TODO: Implementar — (comp (filter ...) (map ...))
  nil)

(defn sumar-activas-xf
  "Usa transduce con xf-activas-totales y + para sumar los totales de las activas."
  [ordenes]
  ;; TODO: Implementar con transduce
  )

(defn totales-activas-vec
  "Usa into con xf-activas-totales para obtener un vector de totales de activas."
  [ordenes]
  ;; TODO: Implementar con into
  )
