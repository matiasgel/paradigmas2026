(ns tp04.ej12-test
  (:require [clojure.test :refer :all]
            [tp04.ej12 :refer :all]))

(deftest test-sum-list
  (is (= 15 (sum-list [1 2 3 4 5] 0)))
  (is (= 0 (sum-list [] 0)))
  (is (= 42 (sum-list [42] 0))))

(deftest test-factorial
  (is (= 120 (factorial 5 1)))
  (is (= 1 (factorial 0 1)))
  (is (= 1 (factorial 1 1)))
  (is (= 3628800 (factorial 10 1))))

(deftest test-my-reverse
  (is (= [3 2 1] (my-reverse [1 2 3] [])))
  (is (= [] (my-reverse [] [])))
  (is (= [1] (my-reverse [1] []))))

(deftest test-my-count
  (is (= 3 (my-count [10 20 30] 0)))
  (is (= 0 (my-count [] 0)))
  (is (= 1 (my-count [:a] 0))))
