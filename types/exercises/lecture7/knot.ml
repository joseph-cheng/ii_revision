let knot f x = 
  let r = ref (fun n -> x) in
  let recur = fun n -> !r n in
  (r := fun n -> f recur n);
  recur;;

type 'a tree = Lf | Br of 'a tree * 'a * 'a tree;;

let t = 
  Br (Br (Lf, 1, Lf), 2, Br (Br (Lf, 3, Lf), 4, Lf));;

let factorial_aux = fun f m ->
  if m = 0 then 1 else m * (f (m-1));;

let factorial = fun n ->
  (knot factorial_aux 0) n;;

let search_aux = fun f (t, x) ->
  match t with
   | Lf -> false 
   | Br (left, d, right) -> if d = x then true else f (left, x) || f (right, x);;

let search = fun t x ->
  (knot search_aux true) (t, x);;


