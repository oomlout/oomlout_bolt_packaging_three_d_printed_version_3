

file_bottom = "scad_output\\oobb_oomlout_bolt_packaging_three_d_printed_version_1_main_body_02_01_15_ex_tray_size_2_wide_2_high\\3dpr.stl";

file_top = "scad_output\\oobb_oomlout_bolt_packaging_three_d_printed_version_1_lid_02_01_02_ex_tray_size_2_wide_2_high\\3dpr.stl";



//main
if (true){
    translate([-200,0,0]){
        rotate([0,0,0]){
            translate([0,0,0]){
                bottom();
            }
            translate([0,0,16]){
                top();
            }
            
        }
    }
}

//intersection
if (true){
    translate([200,0,0]){
        rotate([0,0,0]){
            intersection(){
                #bottom();
                top();
            }
        }
    }
}

//gaps

// lid
if (true){
    translate([0,0,0]){
        rotate([0,0,0]){
            difference(){  
                union(){
                    translate([-50,-50,13]){
                        cube([100,100,1]);
                    }
                }                    
                union(){
                    bottom();
                    top();
                }

            }
        }
    }
}

//gap hinge
if (true){
    translate([0,200,0]){
        rotate([0,0,0]){
            difference(){  
                union(){
                    translate([-50,-50,9]){
                        cube([100,100,1]);
                    }
                }                    
                union(){
                    bottom();
                    top();
                }

            }
        }
    }
}



module bottom(){
    translate([0,0,0]){
        rotate([0,0,0]){
            import(file_bottom);
        }
    }
}

module top(){
    translate([0,0,16]){
        rotate([0,0,0]){
            import(file_top);
        }
    }
}
    


