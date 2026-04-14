(ns tp04.ej15-test
  (:require [clojure.test :refer :all]
            [tp04.ej15 :refer :all]))

(deftest test-primeros-n-pares
  (is (= '(2 4 6 8) (primeros-n-pares 4)))
  (is (= '(2) (primeros-n-pares 1)))
  (is (= '() (primeros-n-pares 0))))

(deftest test-fibonacci
  (is (= '(0 1 1 2 3 5 8) (take 7 (fibonacci))))
  (is (= '(0) (take 1 (fibonacci))))
  (is (= 55 (nth (fibonacci) 10))))

(deftest test-tomar-mientras-menor
  (is (= '(1 3 5) (tomar-mientras-menor [1 3 5 7 2] 6)))
  (is (= '() (tomar-mientras-menor [10 20] 5)))
  (is (= '(1 2 3) (tomar-mientras-menor [1 2 3] 100))))
