(ns tp04.ej15-test
  (:require [clojure.test :refer [deftest is testing]]
            [tp04.ej15 :refer [pipeline-canal]]))

(deftest test-pipeline-canal
  (testing "filtra pares y duplica"
    (is (= [4 8 12] (pipeline-canal [1 2 3 4 5 6] even? #(* 2 %)))))
  (testing "filtra positivos e incrementa"
    (is (= [11 6 21] (pipeline-canal [10 -3 5 -7 20] pos? inc))))
  (testing "datos vacíos"
    (is (= [] (pipeline-canal [] even? inc))))
  (testing "ninguno pasa el filtro"
    (is (= [] (pipeline-canal [1 3 5] even? inc))))
  (testing "todos pasan el filtro"
    (is (= [2 4 6] (pipeline-canal [1 2 3] (constantly true) inc)))))
