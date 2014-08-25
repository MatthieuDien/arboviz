type 'a t
val empty : 'a t
val push : 'a t -> 'a -> 'a t
val pop : 'a t -> 'a * 'a t
val npop : 'a t -> int -> 'a list * 'a t
val is_empty : 'a t -> bool
val fold : ('a -> 'b -> 'a) -> 'a -> 'b t -> 'a
