$fn = 50;


difference() {
	union() {
		hull() {
			translate(v = [-17.5000000000, 10.0000000000, 0]) {
				cylinder(h = 12, r = 5);
			}
			translate(v = [17.5000000000, 10.0000000000, 0]) {
				cylinder(h = 12, r = 5);
			}
			translate(v = [-17.5000000000, -10.0000000000, 0]) {
				cylinder(h = 12, r = 5);
			}
			translate(v = [17.5000000000, -10.0000000000, 0]) {
				cylinder(h = 12, r = 5);
			}
		}
	}
	union() {
		translate(v = [0, 0, 1]) {
			#hull() {
				translate(v = [-17.5000000000, 10.0000000000, 0]) {
					cylinder(h = 11, r = 4);
				}
				translate(v = [17.5000000000, 10.0000000000, 0]) {
					cylinder(h = 11, r = 4);
				}
				translate(v = [-17.5000000000, -10.0000000000, 0]) {
					cylinder(h = 11, r = 4);
				}
				translate(v = [17.5000000000, -10.0000000000, 0]) {
					cylinder(h = 11, r = 4);
				}
			}
		}
	}
}