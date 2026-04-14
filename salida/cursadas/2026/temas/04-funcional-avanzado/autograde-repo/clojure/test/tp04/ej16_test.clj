(ns tp04.ej16-test
  (:require [clojure.test :refer :all]
            [tp04.ej16 :refer :all]))

(deftest test-validate-all-errors
  (let [errors (validate user-rules {:name "" :email "x" :age 16})]
    (is (= 3 (count errors)))
    (is (some #(= :name (:field %)) errors))
    (is (some #(= :email (:field %)) errors))
    (is (some #(= :age (:field %)) errors))))

(deftest test-validate-all-ok
  (is (= [] (validate user-rules {:name "Ana" :email "ana@test.com" :age 20}))))

(deftest test-validate-partial-errors
  (let [errors (validate user-rules {:name "Ana" :email "bad" :age 20})]
    (is (= 1 (count errors)))
    (is (= :email (:field (first errors))))))

(deftest test-valid?
  (is (true? (valid? user-rules {:name "Ana" :email "a@b.com" :age 18})))
  (is (false? (valid? user-rules {:name "" :email "a@b.com" :age 18}))))
