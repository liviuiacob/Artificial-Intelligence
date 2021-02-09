;; Problema 1

(define (problem pe-ntruca)
    (:domain trip-to-romania)
    
    (:objects
     car1 car2 car3
     p1
     row1 row2 row3 row4
     col1 col2 col3 col4)
    
    (:init
     (IS-CAR car1)
     (IS-CAR car2)
     (IS-CAR car3)
     (IS-ROW row1)
     (IS-ROW row2)
     (IS-ROW row3)
     (IS-ROW row4)
     (NEXT-ROW row1 row2)
     (NEXT-ROW row2 row3)
     (NEXT-ROW row3 row4)
     (IS-COLUMN col1)
     (IS-COLUMN col2)
     (IS-COLUMN col3)
     (IS-COLUMN col4)
     (NEXT-COLUMN col1 col2)
     (NEXT-COLUMN col2 col3)
     (NEXT-COLUMN col3 col4)

     (is-package p1)
     (package-at p1 row2 col4)
     (empty car1)
     (empty car2)
     (empty car3)

     ;;initial state
     (car-at car1 row1 col3)
     (car-at car2 row2 col1)
     (car-at car3 row3 col4)

     (rest-at row3 col3)
     (rest-at row1 col2)
     (rest-at row4 col2)
     (not (has-eaten car1))
     (not (has-eaten car2))
     (not (has-eaten car3))

     (gas-station row1 col1)
     (gas-station row1 col4)
     (gas-station row2 col2)
     (not (is-fueled car1))
     (not (is-fueled car2))
     (not (is-fueled car3))

     (not (is-fined car1))
     (not (moved-up car1))
     (not (moved-down car1))
     (not (moved-left car1))
     (not (moved-right car1))
     (camera-at row2 col3)

     (not (is-fined car2))
     (not (moved-up car2))
     (not (moved-down car2))
     (not (moved-left car2))
     (not (moved-right car2))

     (not (is-fined car3))
     (not (moved-up car3))
     (not (moved-down car3))
     (not (moved-left car3))
     (not (moved-right car3))

     (= (total-cost) 0)
     (= (cost car1) 0)
     (= (cost car2) 0)
    )

    (:goal
     (and
      (car-at car1 row3 col1)
      (car-at car2 row3 col2)
      (car-at car3 row3 col3)
      (has-eaten car1)
      (has-eaten car2)
      (has-eaten car3)
      (is-fueled car1)
      (is-fueled car2)
      (is-fueled car3)
      ;;(is-fined car2)
      ;;(is-fined car1)
      (package-at p1 row4 col4)
     )
    )

    (:metric minimize (total-cost))
    ;;(:metric minimize (cost car1))
    ;;(:metric minimize (cost car2))
)
