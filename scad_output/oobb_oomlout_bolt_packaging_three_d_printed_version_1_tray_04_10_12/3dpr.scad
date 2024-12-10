$fn = 50;


difference() {
	union() {
		hull() {
			translate(v = [-25.0000000000, 70.0000000000, 0]) {
				cylinder(h = 12, r = 5);
			}
			translate(v = [25.0000000000, 70.0000000000, 0]) {
				cylinder(h = 12, r = 5);
			}
			translate(v = [-25.0000000000, -70.0000000000, 0]) {
				cylinder(h = 12, r = 5);
			}
			translate(v = [25.0000000000, -70.0000000000, 0]) {
				cylinder(h = 12, r = 5);
			}
		}
	}
	union() {
		translate(v = [0, 0, 2]) {
			hull() {
				translate(v = [-25.0000000000, 70.0000000000, 0]) {
					cylinder(h = 10, r = 4);
				}
				translate(v = [25.0000000000, 70.0000000000, 0]) {
					cylinder(h = 10, r = 4);
				}
				translate(v = [-25.0000000000, -70.0000000000, 0]) {
					cylinder(h = 10, r = 4);
				}
				translate(v = [25.0000000000, -70.0000000000, 0]) {
					cylinder(h = 10, r = 4);
				}
			}
		}
	}
}