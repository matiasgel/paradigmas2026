(ns tp04.ej12-test
  (:require [clojure.test :refer [deftest is testing]]
            [tp04.ej12 :refer [procesar-pipeline procesar-transducer
                               totales-pipeline totales-transducer]]))

(def datos
  [{:total 300 :activa? true}
   {:total 80  :activa? false}
   {:total 150 :activa? true}
   {:total 50  :activa? true}])

(deftest test-procesar-pipeline
  (testing "suma activas con total > 100"
    (is (= 450 (procesar-pipeline datos))))
  (testing "lista vacía"
    (is (= 0 (procesar-pipeline [])))))

(deftest test-procesar-transducer
  (testing "mismo resultado que pipeline"
    (is (= 450 (procesar-transducer datos))))
  (testing "equivalencia con pipeline"
    (is (= (procesar-pipeline datos) (procesar-transducer datos)))))

(deftest test-totales-pipeline
  (testing "vector de totales filtrados"
    (is (= [300 150] (totales-pipeline datos)))))

(deftest test-totales-transducer
  (testing "mismo resultado que pipeline"
    (is (= [300 150] (totales-transducer datos))))
  (testing "equivalencia"
    (is (= (totales-pipeline datos) (totales-transducer datos)))))
