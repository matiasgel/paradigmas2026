(ns tp04.ej04-test
  (:require [clojure.test :refer :all]
            [tp04.ej04 :refer :all]))

(def ordenes
  [{:id 1 :cliente "Ana"   :total 120 :activa? true}
   {:id 2 :cliente "Boris" :total 50  :activa? false}
   {:id 3 :cliente "Carla" :total 200 :activa? true}])

(deftest test-total-activas
  (is (= 320 (total-activas ordenes)))
  (is (= 0 (total-activas [])))
  (is (= 0 (total-activas [{:id 1 :total 50 :activa? false}]))))

(deftest test-nombres-activas
  (is (= ["Ana" "Carla"] (nombres-activas ordenes)))
  (is (= [] (nombres-activas []))))

(deftest test-cuadrados-pares
  (is (= 20 (cuadrados-pares [1 2 3 4 5])))
  (is (= 0 (cuadrados-pares [1 3 5 7])))
  (is (= 0 (cuadrados-pares []))))
