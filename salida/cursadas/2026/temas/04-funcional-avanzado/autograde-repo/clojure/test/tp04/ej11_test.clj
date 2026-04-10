(ns tp04.ej11-test
  (:require [clojure.test :refer [deftest is testing]]
            [tp04.ej11 :refer [xf-activas-totales sumar-activas-xf totales-activas-vec]]))

(def ordenes
  [{:total 100 :activa? true}
   {:total 50  :activa? false}
   {:total 200 :activa? true}
   {:total 75  :activa? true}])

(deftest test-xf-activas-totales
  (testing "el transducer no es nil"
    (is (some? xf-activas-totales))))

(deftest test-sumar-activas-xf
  (testing "suma totales de activas"
    (is (= 375 (sumar-activas-xf ordenes))))
  (testing "lista vacía"
    (is (= 0 (sumar-activas-xf []))))
  (testing "ninguna activa"
    (is (= 0 (sumar-activas-xf [{:total 100 :activa? false}])))))

(deftest test-totales-activas-vec
  (testing "vector de totales de activas"
    (is (= [100 200 75] (totales-activas-vec ordenes))))
  (testing "lista vacía"
    (is (= [] (totales-activas-vec [])))))
