$fn = 50;


difference() {
	union() {
		hull() {
			translate(v = [-32.5000000000, 70.0000000000, 0]) {
				cylinder(h = 24, r = 5);
			}
			translate(v = [32.5000000000, 70.0000000000, 0]) {
				cylinder(h = 24, r = 5);
			}
			translate(v = [-32.5000000000, -70.0000000000, 0]) {
				cylinder(h = 24, r = 5);
			}
			translate(v = [32.5000000000, -70.0000000000, 0]) {
				cylinder(h = 24, r = 5);
			}
		}
	}
	union() {
		translate(v = [0, 0, 2]) {
			hull() {
				translate(v = [-32.5000000000, 70.0000000000, 0]) {
					cylinder(h = 22, r = 4);
				}
				translate(v = [32.5000000000, 70.0000000000, 0]) {
					cylinder(h = 22, r = 4);
				}
				translate(v = [-32.5000000000, -70.0000000000, 0]) {
					cylinder(h = 22, r = 4);
				}
				translate(v = [32.5000000000, -70.0000000000, 0]) {
					cylinder(h = 22, r = 4);
				}
			}
		}
	}
}