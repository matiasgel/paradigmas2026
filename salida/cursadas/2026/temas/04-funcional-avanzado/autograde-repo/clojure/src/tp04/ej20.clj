(ns tp04.ej20)

;; Ejercicio 20 — Integrador Clojure
;; Trazabilidad: F-37

(defn clasificar-orden
  "Clasifica una orden:
   - Si no es :activa?        → {:ok false :error \"inactiva\"}
   - Si :categoria no es \"elect\" → {:ok false :error \"categoría incorrecta\"}
   - Si :total <= 200          → {:ok false :error \"monto insuficiente\"}
   - Si pasa todo              → {:ok true :value (:total orden)}
   Evaluar en ese orden."
  [orden]
  ;; TODO: Implementar
  )

(defn total-elect-activos
  "Clasifica cada orden, filtra los :ok true y suma sus :value."
  [ordenes]
  ;; TODO: Implementar
  )

(defn resumen-por-categoria
  "Retorna un mapa {\"categoria\" total-activas, ...} con la suma de :total
   de las órdenes activas, agrupadas por :categoria."
  [ordenes]
  ;; TODO: Implementar
  )
