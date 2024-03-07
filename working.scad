

file_bottom = "scad_output\\oobb_oomlout_bolt_packaging_three_d_printed_version_1_main_body_09_09_24\\3dpr.stl";

file_top = "scad_output\\oobb_oomlout_bolt_packaging_three_d_printed_version_1_lid_09_09_02\\3dpr.stl";



//main
if (true){
    translate([-300,0,0]){
        translate([0,-300,0]){
            linear_extrude(height=5){text("main",size=40, font="Arial:style=Bold",halign="center",valign="center");
        }   }
        rotate([0,0,0]){
            translate([0,0,0]){
                bottom();
            }
            color("green")
            translate([0,0,0]){
                top();
            }
            
        }
    }
}

//intersection
if (true){
    translate([300,0,0]){
        translate([0,-300,0]){
            linear_extrude(height=5){text("intersection",size=40, font="Arial:style=Bold",halign="center",valign="center");}
        }
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
        translate([0,-300,0]){
            linear_extrude(height=5){
            text("lid",size=40, font="Arial:style=Bold",halign="center",valign="center");
        }}
        rotate([0,0,0]){
            difference(){  
                union(){
                    translate([-150,-150,24]){
                        cube([300,300,1]);
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
    translate([0,300,0]){
        translate([0,300,0]){
            linear_extrude(height=5){
                text("gap hinge",size=40, font="Arial:style=Bold",halign="center",valign="center");
            }}

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
    translate([0,0,26]){
        rotate([0,0,0]){
            import(file_top);
        }
    }
}
    


