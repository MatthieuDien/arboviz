open Tree

module type Backend =
  sig
    val name : string

    (* out channel -> tree -> widht unity -> height unity -> show label -> unit *)
    val write : out_channel -> Tree.t -> float -> float -> bool -> unit
  end
