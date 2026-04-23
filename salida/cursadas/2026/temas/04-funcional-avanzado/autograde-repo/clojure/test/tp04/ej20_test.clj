(ns tp04.ej20-test
  (:require [clojure.test :refer [deftest is testing]]
            [tp04.ej20 :refer [clasificar-orden total-elect-activos resumen-por-categoria]]))

(def ordenes
  [{:id 1 :cliente "Ana"   :total 250 :categoria "elect" :activa? true}
   {:id 2 :cliente "Boris" :total 80  :categoria "ropa"  :activa? false}
   {:id 3 :cliente "Carla" :total 420 :categoria "elect" :activa? true}
   {:id 4 :cliente "Diana" :total 30  :categoria "ropa"  :activa? true}
   {:id 5 :cliente "Edwin" :total 175 :categoria "elect" :activa? true}])

(deftest test-clasificar-orden
  (testing "aprueba orden válida"
    (is (= {:ok true :value 250} (clasificar-orden (nth ordenes 0)))))
  (testing "rechaza inactiva"
    (is (= {:ok false :error "inactiva"} (clasificar-orden (nth ordenes 1)))))
  (testing "rechaza categoría incorrecta"
    (is (= {:ok false :error "categoría incorrecta"} (clasificar-orden (nth ordenes 3)))))
  (testing "rechaza monto insuficiente"
    (is (= {:ok false :error "monto insuficiente"} (clasificar-orden (nth ordenes 4))))))

(deftest test-total-elect-activos
  (testing "suma los aprobados"
    (is (= 670 (total-elect-activos ordenes))))
  (testing "lista vacía"
    (is (= 0 (total-elect-activos []))))
  (testing "ninguno aprobado"
    (is (= 0 (total-elect-activos [{:id 1 :total 50 :categoria "ropa" :activa? true}])))))

(deftest test-resumen-por-categoria
  (testing "agrupa por categoría (solo activas)"
    (let [r (resumen-por-categoria ordenes)]
      (is (= 845 (get r "elect")))   ;; 250 + 420 + 175
      (is (= 30 (get r "ropa")))))   ;; solo Diana (Boris es inactivo)
  (testing "lista vacía"
    (is (= {} (resumen-por-categoria [])))))
