(ns tp04.ej15
  (:require [clojure.core.async :refer [chan go >! <! <!! close!]]))

;; Ejercicio 15 — core.async canales
;; Trazabilidad: F-26, F-27

(defn pipeline-canal
  "Procesa datos a través de canales core.async:
   1. Crea un canal de entrada y uno de salida
   2. Un go-block productor pone los datos en el canal entrada
   3. Un go-block consumidor lee del canal entrada:
      - Si el dato pasa filtro-fn, aplica transformar-fn y lo pone en salida
      - Si no pasa, lo descarta
   4. Recolecta todos los resultados del canal salida en un vector

   IMPORTANTE: La función debe retornar un vector (operación bloqueante con <!!)."
  [datos filtro-fn transformar-fn]
  ;; TODO: Implementar
  )
