;; Problema 2

(define (problem pe-ntruca2)
    (:domain trip-to-romania)
    
    (:objects
     car1 car2
     p1 p2 p3
     row1 row2 row3 row4
     col1 col2 col3 col4)
    
    (:init
     (IS-CAR car1)
     (IS-CAR car2)
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
     (is-package p2)
     (is-package p3)
     (package-at p1 row1 col2)
     (package-at p2 row2 col4)
     (package-at p3 row3 col3)
     (empty car1)
     (empty car2)

     ;;initial state
     (car-at car1 row2 col1)
     (car-at car2 row3 col4)

     (rest-at row3 col2)
     (rest-at row4 col1)
     (not (has-eaten car1))
     (not (has-eaten car2))

     (gas-station row1 col1)
     (gas-station row4 col1)
     (not (is-fueled car1))
     (not (is-fueled car2))

     (not (is-fined car1))
     (not (moved-up car1))
     (not (moved-down car1))
     (not (moved-left car1))
     (not (moved-right car1))
     (camera-at row1 col2)

     (not (is-fined car2))
     (not (moved-up car2))
     (not (moved-down car2))
     (not (moved-left car2))
     (not (moved-right car2))
     (camera-at row4 col2)

     (= (total-cost) 0)
     (= (cost car1) 0)
     (= (cost car2) 0)
    )

    (:goal
     (and
      (car-at car1 row4 col4)
      (car-at car2 row1 col4)
      (has-eaten car1)
      (has-eaten car2)
      (is-fueled car1)
      (is-fueled car2)
      ;;(is-fined car2)
      ;;(is-fined car1)
      (package-at p1 row1 col1)
      (package-at p2 row4 col1)
      (package-at p3 row4 col4)
     )
    )

    (:metric minimize (total-cost))
    ;;(:metric minimize (cost car1))
    ;;(:metric minimize (cost car2))
)
