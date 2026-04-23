(ns tp04.ej06-test
  (:require [clojure.test :refer [deftest is testing]]
            [tp04.ej06 :refer [agregar-al-vector actualizar-mapa combinar-mapas]]))

(deftest test-agregar-al-vector
  (testing "agrega elemento al final"
    (is (= [1 2 3 4] (agregar-al-vector [1 2 3] 4))))
  (testing "a vector vacío"
    (is (= [1] (agregar-al-vector [] 1))))
  (testing "no modifica el original"
    (let [v [1 2 3]]
      (agregar-al-vector v 4)
      (is (= [1 2 3] v)))))

(deftest test-actualizar-mapa
  (testing "agrega clave nueva"
    (is (= {:a 1 :b 2} (actualizar-mapa {:a 1} :b 2))))
  (testing "actualiza clave existente"
    (is (= {:a 99} (actualizar-mapa {:a 1} :a 99))))
  (testing "no modifica el original"
    (let [m {:a 1}]
      (actualizar-mapa m :b 2)
      (is (= {:a 1} m)))))

(deftest test-combinar-mapas
  (testing "combina sin conflictos"
    (is (= {:a 1 :b 2 :c 3} (combinar-mapas {:a 1 :b 2} {:c 3}))))
  (testing "m2 prevalece en conflictos"
    (is (= {:a 1 :b 99 :c 3} (combinar-mapas {:a 1 :b 2} {:b 99 :c 3}))))
  (testing "mapas vacíos"
    (is (= {:a 1} (combinar-mapas {:a 1} {})))))
