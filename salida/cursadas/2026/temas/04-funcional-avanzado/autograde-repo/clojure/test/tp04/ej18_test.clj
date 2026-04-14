(ns tp04.ej18-test
  (:require [clojure.test :refer :all]
            [tp04.ej18 :refer :all]))

(def ordenes
  [{:id 1 :cliente "Ana"   :total 250 :categoria "elect" :activa? true}
   {:id 2 :cliente "Boris" :total 80  :categoria "ropa"  :activa? false}
   {:id 3 :cliente "Carla" :total 420 :categoria "elect" :activa? true}
   {:id 4 :cliente "Diana" :total 50  :categoria "ropa"  :activa? true}])

(deftest test-clasificar-orden-ok
  (let [r (clasificar-orden (first ordenes))]
    (is (true? (:ok r)))
    (is (= 250 (:total (:value r))))))

(deftest test-clasificar-orden-inactiva
  (is (= {:ok false :error "orden inactiva"} (clasificar-orden (second ordenes)))))

(deftest test-clasificar-orden-monto
  (is (= {:ok false :error "monto insuficiente"} (clasificar-orden (nth ordenes 3)))))

(deftest test-aplicar-descuento
  (is (= 225 (:total (aplicar-descuento 10 (first ordenes)))))
  (is (= 250 (:total (aplicar-descuento 0 (first ordenes))))))

(deftest test-procesar-ordenes
  (let [result (procesar-ordenes ordenes)]
    (is (= 2 (count (:aprobadas result))))
    (is (= 2 (count (:rechazadas result))))
    (is (= 225 (:total (first (:aprobadas result)))))
    (is (= 378 (:total (second (:aprobadas result)))))
    (is (= 603 (:total-final result)))))

(deftest test-procesar-ordenes-vacio
  (let [result (procesar-ordenes [])]
    (is (= [] (:aprobadas result)))
    (is (= [] (:rechazadas result)))
    (is (= 0 (:total-final result)))))
