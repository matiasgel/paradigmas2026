(ns tp04.ej16-test
  (:require [clojure.test :refer [deftest is testing]]
            [tp04.ej16 :refer [crear-banco saldo transferir total-banco]]))

(deftest test-crear-banco
  (testing "crea banco con saldos correctos"
    (let [banco (crear-banco {:ana 1000 :boris 500})]
      (is (= 1000 (saldo banco :ana)))
      (is (= 500 (saldo banco :boris))))))

(deftest test-transferir
  (testing "transfiere correctamente"
    (let [banco (crear-banco {:ana 1000 :boris 500})]
      (transferir banco :ana :boris 200)
      (is (= 800 (saldo banco :ana)))
      (is (= 700 (saldo banco :boris))))))

(deftest test-total-banco
  (testing "total se preserva tras transferencia"
    (let [banco (crear-banco {:ana 1000 :boris 500 :carla 300})]
      (is (= 1800 (total-banco banco)))
      (transferir banco :ana :boris 200)
      (is (= 1800 (total-banco banco)))
      (transferir banco :boris :carla 100)
      (is (= 1800 (total-banco banco))))))

(deftest test-transferencias-multiples
  (testing "invariante tras múltiples transferencias"
    (let [banco (crear-banco {:a 1000 :b 1000 :c 1000})
          total-inicial (total-banco banco)]
      (dotimes [_ 10]
        (transferir banco :a :b 50)
        (transferir banco :b :c 30)
        (transferir banco :c :a 20))
      (is (= total-inicial (total-banco banco))))))
