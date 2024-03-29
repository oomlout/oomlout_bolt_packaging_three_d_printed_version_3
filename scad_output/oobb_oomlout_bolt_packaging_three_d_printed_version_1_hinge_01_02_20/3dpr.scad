$fn = 50;


difference() {
	union() {
		translate(v = [-10.0000000000, 0, 0.0000000000]) {
			rotate(a = [0, 90, 0]) {
				cylinder(h = 20, r = 6.0000000000);
			}
		}
		translate(v = [-10.0000000000, -22.5000000000, -12.5000000000]) {
			cube(size = [20, 22.5000000000, 16]);
		}
		translate(v = [-10.0000000000, -21.0000000000, -12.5000000000]) {
			cube(size = [20, 27, 12.5000000000]);
		}
		translate(v = [25.0000000000, 0, 0.0000000000]) {
			rotate(a = [0, 90, 0]) {
				cylinder(h = 10, r = 5.0000000000);
			}
		}
		translate(v = [25.0000000000, -5.0000000000, 0]) {
			cube(size = [10, 10, 7.5000000000]);
		}
		translate(v = [25.0000000000, -22.5000000000, 7.5000000000]) {
			cube(size = [10, 27.5000000000, 2]);
		}
	}
	union() {
		translate(v = [10.0000000000, 0, 0]) {
			rotate(a = [0, 90, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -20.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										linear_extrude(height = 2.5000000000) {
											polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -20.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										linear_extrude(height = 2.5000000000) {
											polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -20.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										linear_extrude(height = 2.5000000000) {
											polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -20.0000000000]) {
							cylinder(h = 20, r = 1.5000000000);
						}
						translate(v = [0, 0, -1.9000000000]) {
							cylinder(h = 1.9000000000, r1 = 1.8000000000, r2 = 3.6000000000);
						}
						translate(v = [0, 0, -20.0000000000]) {
							cylinder(h = 20, r = 1.8000000000);
						}
						translate(v = [0, 0, -20.0000000000]) {
							cylinder(h = 20, r = 1.5000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-5.5000000000, -6.0000000000, -12.5000000000]) {
			cube(size = [11, 15, 20]);
		}
		translate(v = [25.0000000000, 0, 0]) {
			rotate(a = [0, 90, 0]) {
				cylinder(h = 10, r = 1.8000000000);
			}
		}
	}
}