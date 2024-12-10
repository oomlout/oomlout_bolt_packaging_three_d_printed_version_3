$fn = 50;


difference() {
	union() {
		hull() {
			translate(v = [-55.0000000000, 17.5000000000, 0]) {
				cylinder(h = 21, r = 5);
			}
			translate(v = [55.0000000000, 17.5000000000, 0]) {
				cylinder(h = 21, r = 5);
			}
			translate(v = [-55.0000000000, -17.5000000000, 0]) {
				cylinder(h = 21, r = 5);
			}
			translate(v = [55.0000000000, -17.5000000000, 0]) {
				cylinder(h = 21, r = 5);
			}
		}
	}
	union() {
		translate(v = [0, 0, 2]) {
			hull() {
				translate(v = [-55.0000000000, 17.5000000000, 0]) {
					cylinder(h = 19, r = 4);
				}
				translate(v = [55.0000000000, 17.5000000000, 0]) {
					cylinder(h = 19, r = 4);
				}
				translate(v = [-55.0000000000, -17.5000000000, 0]) {
					cylinder(h = 19, r = 4);
				}
				translate(v = [55.0000000000, -17.5000000000, 0]) {
					cylinder(h = 19, r = 4);
				}
			}
		}
	}
}