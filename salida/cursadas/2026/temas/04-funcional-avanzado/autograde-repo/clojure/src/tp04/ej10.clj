(ns tp04.ej10)

;; Ejercicio 10 — Errores como datos
;; Trazabilidad: F-18

(defn dividir-seguro
  "Divide a / b.
   Retorna {:ok true :value resultado} o {:ok false :error \"División por cero\"}."
  [a b]
  ;; TODO: Implementar
  )

(defn raiz-segura
  "Calcula la raíz cuadrada de n.
   Si n >= 0: {:ok true :value (Math/sqrt n)}
   Si n < 0:  {:ok false :error \"Raíz de negativo\"}"
  [n]
  ;; TODO: Implementar
  )

(defn operar-cadena
  "Divide a/b, luego calcula la raíz del resultado.
   Propaga el primer error encontrado."
  [a b]
  ;; TODO: Implementar (encadenar dividir-seguro y raiz-segura)
  )
