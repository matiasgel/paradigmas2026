(ns tp04.ej10-test
  (:require [clojure.test :refer [deftest is testing]]
            [tp04.ej10 :refer [dividir-seguro raiz-segura operar-cadena]]))

(deftest test-dividir-seguro
  (testing "división exitosa"
    (is (= {:ok true :value 5} (dividir-seguro 10 2))))
  (testing "división por cero"
    (is (= {:ok false :error "División por cero"} (dividir-seguro 10 0))))
  (testing "resultado decimal"
    (let [r (dividir-seguro 7 2)]
      (is (:ok r))
      (is (= 3.5 (:value r))))))

(deftest test-raiz-segura
  (testing "raíz de positivo"
    (is (= {:ok true :value 5.0} (raiz-segura 25))))
  (testing "raíz de cero"
    (is (= {:ok true :value 0.0} (raiz-segura 0))))
  (testing "raíz de negativo"
    (is (= {:ok false :error "Raíz de negativo"} (raiz-segura -4)))))

(deftest test-operar-cadena
  (testing "cadena exitosa: sqrt(100/4) = 5"
    (is (= {:ok true :value 5.0} (operar-cadena 100 4))))
  (testing "error en división"
    (is (= {:ok false :error "División por cero"} (operar-cadena 10 0))))
  (testing "error en raíz (resultado negativo)"
    (is (= {:ok false :error "Raíz de negativo"} (operar-cadena -100 1)))))
