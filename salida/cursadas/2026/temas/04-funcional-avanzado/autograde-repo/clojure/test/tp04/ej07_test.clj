(ns tp04.ej07-test
  (:require [clojure.test :refer :all]
            [tp04.ej07 :refer :all]))

(deftest test-doble
  (is (= 10 (doble 5)))
  (is (= 0 (doble 0))))

(deftest test-triple
  (is (= 12 (triple 4)))
  (is (= 0 (triple 0))))

(deftest test-doble-con-map
  (is (= '(2 4 6) (map doble [1 2 3]))))

(deftest test-required-field
  (is (= {:status :ok :value "Ana"} (required-field "nombre" "Ana")))
  (is (= {:status :error :error "nombre es obligatorio"} (required-field "nombre" "")))
  (is (= {:status :error :error "email es obligatorio"} (required-field "email" "   "))))

(deftest test-validate-name
  (is (= {:status :ok :value "Ana"} (validate-name "Ana")))
  (is (= {:status :error :error "nombre es obligatorio"} (validate-name ""))))

(deftest test-validate-email
  (is (= {:status :ok :value "a@b.com"} (validate-email "a@b.com")))
  (is (= {:status :error :error "email es obligatorio"} (validate-email ""))))
