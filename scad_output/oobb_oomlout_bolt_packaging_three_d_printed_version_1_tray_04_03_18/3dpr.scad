$fn = 50;


difference() {
	union() {
		hull() {
			translate(v = [-25.0000000000, 17.5000000000, 0]) {
				cylinder(h = 18, r = 5);
			}
			translate(v = [25.0000000000, 17.5000000000, 0]) {
				cylinder(h = 18, r = 5);
			}
			translate(v = [-25.0000000000, -17.5000000000, 0]) {
				cylinder(h = 18, r = 5);
			}
			translate(v = [25.0000000000, -17.5000000000, 0]) {
				cylinder(h = 18, r = 5);
			}
		}
	}
	union() {
		translate(v = [0, 0, 2]) {
			#hull() {
				translate(v = [-25.0000000000, 17.5000000000, 0]) {
					cylinder(h = 16, r = 2);
				}
				translate(v = [25.0000000000, 17.5000000000, 0]) {
					cylinder(h = 16, r = 2);
				}
				translate(v = [-25.0000000000, -17.5000000000, 0]) {
					cylinder(h = 16, r = 2);
				}
				translate(v = [25.0000000000, -17.5000000000, 0]) {
					cylinder(h = 16, r = 2);
				}
			}
		}
	}
}