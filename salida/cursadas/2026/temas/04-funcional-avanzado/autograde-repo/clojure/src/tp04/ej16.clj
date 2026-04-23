(ns tp04.ej16)

;; Ejercicio 16 — STM y transacciones
;; Trazabilidad: F-28

(defn crear-banco
  "Recibe un mapa {:ana 1000 :boris 500 ...} y retorna un mapa
   donde cada valor es un ref con el saldo.
   Ejemplo: {:ana (ref 1000) :boris (ref 500)}"
  [cuentas-map]
  ;; TODO: Implementar
  )

(defn saldo
  "Retorna el saldo actual de una cuenta (deref del ref)."
  [banco cuenta]
  ;; TODO: Implementar
  )

(defn transferir
  "Transfiere monto de la cuenta origen a la cuenta destino.
   Debe ejecutarse dentro de dosync para ser atómica.
   Usa alter para modificar los refs."
  [banco origen destino monto]
  ;; TODO: Implementar con dosync
  )

(defn total-banco
  "Suma todos los saldos del banco.
   El invariante: este total nunca cambia tras transferencias."
  [banco]
  ;; TODO: Implementar
  )
