(ns tp04.ej09-test
  (:require [clojure.test :refer :all]
            [tp04.ej09 :refer :all]))

(deftest test-validate-not-empty
  (is (= {:status :ok :value "Ana"} (validate-not-empty "Ana")))
  (is (= {:status :error :error "campo vacío"} (validate-not-empty "")))
  (is (= {:status :error :error "campo vacío"} (validate-not-empty "   "))))

(deftest test-validate-email-format
  (is (= {:status :ok :value "a@b.com"} (validate-email-format "a@b.com")))
  (is (= {:status :error :error "email inválido"} (validate-email-format "invalid")))
  (is (= {:status :error :error "email inválido"} (validate-email-format "a@b"))))

(deftest test-validate-field-ok
  (is (= {:status :ok :value "ana@test.com"}
         (validate-field "ana@test.com" validate-not-empty validate-email-format))))

(deftest test-validate-field-first-error
  (is (= {:status :error :error "campo vacío"}
         (validate-field "" validate-not-empty validate-email-format))))

(deftest test-validate-field-second-error
  (is (= {:status :error :error "email inválido"}
         (validate-field "invalid" validate-not-empty validate-email-format))))
