$fn = 50;


difference() {
	union() {
		hull() {
			translate(v = [-40.0000000000, 2.5000000000, 0]) {
				cylinder(h = 24, r = 5);
			}
			translate(v = [40.0000000000, 2.5000000000, 0]) {
				cylinder(h = 24, r = 5);
			}
			translate(v = [-40.0000000000, -2.5000000000, 0]) {
				cylinder(h = 24, r = 5);
			}
			translate(v = [40.0000000000, -2.5000000000, 0]) {
				cylinder(h = 24, r = 5);
			}
		}
	}
	union() {
		translate(v = [0, 0, 2]) {
			hull() {
				translate(v = [-40.0000000000, 2.5000000000, 0]) {
					cylinder(h = 22, r = 4);
				}
				translate(v = [40.0000000000, 2.5000000000, 0]) {
					cylinder(h = 22, r = 4);
				}
				translate(v = [-40.0000000000, -2.5000000000, 0]) {
					cylinder(h = 22, r = 4);
				}
				translate(v = [40.0000000000, -2.5000000000, 0]) {
					cylinder(h = 22, r = 4);
				}
			}
		}
		#translate(v = [-15.0000000000, -15.0000000000, 2]) {
			cube(size = [30, 30, 22]);
		}
	}
}