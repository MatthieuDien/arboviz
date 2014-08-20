module type Frontend =
  sig
    val name : string
    val parse : in_channel -> Tree.t
  end
