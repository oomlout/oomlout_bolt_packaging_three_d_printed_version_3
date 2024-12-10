$fn = 50;


difference() {
	union() {
		hull() {
			translate(v = [-47.5000000000, 70.0000000000, 0]) {
				cylinder(h = 18, r = 5);
			}
			translate(v = [47.5000000000, 70.0000000000, 0]) {
				cylinder(h = 18, r = 5);
			}
			translate(v = [-47.5000000000, -70.0000000000, 0]) {
				cylinder(h = 18, r = 5);
			}
			translate(v = [47.5000000000, -70.0000000000, 0]) {
				cylinder(h = 18, r = 5);
			}
		}
	}
	union() {
		translate(v = [0, 0, 2]) {
			hull() {
				translate(v = [-47.5000000000, 70.0000000000, 0]) {
					cylinder(h = 16, r = 4);
				}
				translate(v = [47.5000000000, 70.0000000000, 0]) {
					cylinder(h = 16, r = 4);
				}
				translate(v = [-47.5000000000, -70.0000000000, 0]) {
					cylinder(h = 16, r = 4);
				}
				translate(v = [47.5000000000, -70.0000000000, 0]) {
					cylinder(h = 16, r = 4);
				}
			}
		}
	}
}