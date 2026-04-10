(ns tp04.ej05-test
  (:require [clojure.test :refer [deftest is testing]]
            [tp04.ej05 :refer [primeros-n-pares fibonacci tomar-mientras-menor]]))

(deftest test-primeros-n-pares
  (testing "4 primeros pares"
    (is (= '(2 4 6 8) (primeros-n-pares 4))))
  (testing "1 par"
    (is (= '(2) (primeros-n-pares 1))))
  (testing "0 pares"
    (is (= '() (primeros-n-pares 0)))))

(deftest test-fibonacci
  (testing "primeros 7 fibonacci"
    (is (= '(0 1 1 2 3 5 8) (take 7 (fibonacci)))))
  (testing "primeros 1"
    (is (= '(0) (take 1 (fibonacci)))))
  (testing "primeros 10"
    (is (= '(0 1 1 2 3 5 8 13 21 34) (take 10 (fibonacci))))))

(deftest test-tomar-mientras-menor
  (testing "toma mientras menor a 6"
    (is (= '(1 3 5) (tomar-mientras-menor [1 3 5 7 2] 6))))
  (testing "todos menores"
    (is (= '(1 2 3) (tomar-mientras-menor [1 2 3] 10))))
  (testing "ninguno menor"
    (is (= '() (tomar-mientras-menor [10 20 30] 5))))
  (testing "lista vacía"
    (is (= '() (tomar-mientras-menor [] 5)))))
