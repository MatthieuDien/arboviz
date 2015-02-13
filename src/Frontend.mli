module type Frontend =
  sig
    val name : string
    val parse : in_channel -> Tree.t
    val parse_from_string : string -> Tree.t
  end
