(ns tp04.ej04-test
  (:require [clojure.test :refer [deftest is testing]]
            [tp04.ej04 :refer [total-activas nombres-activas]]))

(def ordenes
  [{:id 1 :cliente "Ana"   :total 120 :activa? true}
   {:id 2 :cliente "Boris" :total 50  :activa? false}
   {:id 3 :cliente "Carla" :total 200 :activa? true}
   {:id 4 :cliente "Diana" :total 75  :activa? true}])

(deftest test-total-activas
  (testing "suma totales de activas"
    (is (= 395 (total-activas ordenes))))
  (testing "lista vacía"
    (is (= 0 (total-activas []))))
  (testing "ninguna activa"
    (is (= 0 (total-activas (map #(assoc % :activa? false) ordenes))))))

(deftest test-nombres-activas
  (testing "retorna nombres de activas"
    (is (= ["Ana" "Carla" "Diana"] (nombres-activas ordenes))))
  (testing "lista vacía"
    (is (= [] (nombres-activas [])))))
