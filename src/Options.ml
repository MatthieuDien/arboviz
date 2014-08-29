type options_record = {
  mutable verbosity : int;
  mutable output_type : string;
  mutable output_name : string;
  mutable width_ratio : float;
  mutable height_ratio : float;
  mutable show_label : bool;
  mutable input_name : string
}

let global_options = {
  verbosity = 1 ;
  output_type = "dot" ;
  output_name = "tree" ;
  width_ratio = 1. ;
  height_ratio = 1. ;
  show_label = false ;
  input_name = "" 
}
